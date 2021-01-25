from modules.server_queue import Queue
import time


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
            while self.queue.exists():
                self.handle(self.queue.get())

    def handle(self, message):
        """    Prototype    """
        pass

