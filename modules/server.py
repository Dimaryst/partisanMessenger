import socket
import threading
import socketserver
import time


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.server.queue.add(data)


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

    def send(self, ip, port, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        try:
            sock.sendall(bytes(message, 'utf-8'))
            print(self)
        finally:
            sock.close()

    def handle(self, message):
        """
        Prototype
        """
        pass


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
