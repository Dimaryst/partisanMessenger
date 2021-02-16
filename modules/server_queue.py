import threading
import socketserver
import time


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """    Prototype    """
        pass


class Queue:
    def __init__(self, ip, port):
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server.queue = self
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.messages = []
        self.ip = ip
        self.port = port

    def start_server(self):
        self.server_thread.start()
        print(f"\nIncoming messages server\nIP: {self.ip}\nPORT: {self.port}")

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
    def __init__(self, ip, port, main_window):
        self.ip = ip
        self.port = port
        self.main_window = main_window
        self.queue = Queue(self.ip, self.port)

    def start_server(self):
        self.queue.start_server()

    def stop_server(self):
        self.queue.stop_server()

    def loop(self):
        while True:
            time.sleep(1)
            while self.queue.exists():
                self.handle(self.queue.get())

    def handle(self, message):
        """    Prototype    """
        pass
