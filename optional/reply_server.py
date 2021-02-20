import json
import os
import socket
import threading
import socketserver
import time
import configparser
from datetime import datetime


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.server.queue.add(data)
        print(f"Received: {data.decode('utf-8')}")


class Queue:
    def __init__(self, ip, port):
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server.queue = self
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.ip = ip
        self.port = port
        self.messages = []

    def start_server(self):
        self.server_thread.start()
        print("Server loop running in thread:", self.server_thread.name)
        print(f"Server: \n[{self.ip}]::{self.port}")

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

    def add(self, message):
        self.messages.append(message)

    def view(self):
        return self.messages

    def get(self):
        return self.messages.pop()

    def exists(self):
        return len(self.messages)


class Server:
    def __init__(self, ip, port):
        self.queue = Queue(ip, port)

    def start_server(self):
        self.queue.start_server()

    def stop_server(self):
        self.queue.stop_server()

    def loop(self):
        while True:
            time.sleep(1)
            if self.queue.exists():
                self.handle(self.queue.get())

    def handle(self, message):
        """
        Prototype
        """
        pass


class MessagesServer(Server):
    def handle(self, message):
        date = str(datetime.now())
        print(message.decode('utf-8'))
        received_package = json.loads(message.decode('utf-8'))
        if os.path.exists('reply_config.ini'):
            server_config = configparser.ConfigParser()
            server_config.read("reply_config.ini")
            server_uuid = server_config["Server"]["server_uuid"]
            reply_uuid, reply_ip, reply_port = server_config["Reply"]["uuid"], \
                                               server_config["Reply"]["ip"], server_config["Reply"]["port"]

            reply_package = (server_uuid, reply_uuid,
                             f'I got your message! {received_package[2]}', date)

            print("Trying to reply:", reply_package)
            sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            try:
                sock.connect((reply_ip, int(reply_port)))
                print("Trying to send to recipient: ", reply_ip, socket.SOCK_STREAM)
                print(reply_package)
                sock.send(str(reply_package).encode('utf-8'))

            except Exception as e:
                print(f"Failed ({e})")
            finally:
                sock.close()
        else:
            print("Configuration not found!")


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def run(ip, port):
    try:
        if is_valid_ipv4_address(ip) or is_valid_ipv6_address(ip) or ip == "localhost":
            if 1024 <= port <= 65536:
                server = MessagesServer(ip, port)
                server.start_server()
                server.loop()
                server.stop_server()
            else:
                print("Bad PORT")
        else:
            print("Bad IP")

    except KeyboardInterrupt:
        print(f"Stopped")

    except Exception as e:
        print(f"Failed ({e})")


# Start Server Example
if os.path.exists('reply_config.ini'):
    config = configparser.ConfigParser()
    config.read("reply_config.ini")
    IP = config["Server"]["server_ip"]
    PORT = int(config["Server"]["server_port"])
else:
    IP = 'localhost'
    PORT = 8090

print(IP, PORT)
run(IP, PORT)
