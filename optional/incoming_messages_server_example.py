from modules.server import Server, is_valid_ipv4_address, is_valid_ipv6_address


class MessagesServer(Server):
    def handle(self, message):
        print(message.decode('utf-8'))


def run(ip, port):
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


# Start
IP = 'localhost'
PORT = 8090
run(IP, PORT)
