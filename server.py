import socket
from _thread import start_new_thread


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.ready_clients = []
        self.game_over_clients = []

    def threaded_client(self, conn, addr):
        print(f"Connected {addr}")
        self.clients.append(conn)

        while True:
            data = conn.recv(1024)

            if not data:
                print("Disconnected")
                break

            print(f"Received from {addr}: {data.decode()}")

            if data.decode() == "ready":
                self.ready_clients.append(conn)
                if len(self.ready_clients) == 2:
                    self.ready_clients[0].sendall("1".encode())
                    self.ready_clients[1].sendall("0".encode())

            elif data.decode() == "yes" or data.decode() == "no":  # replace freetext yes/no with boolean values or enums
                self.game_over_clients.append(conn)
                if data.decode() == "no":
                    n = 1  # what's n? use indicative names and values
                else:
                    n = 0

                if len(self.game_over_clients) == 2:
                    if n == 1:
                        for client in self.game_over_clients:
                            client.sendall("stop".encode())
                    else:
                        for client in self.game_over_clients:
                            client.sendall(" ".encode())
                            self.ready_clients = []
                            self.game_over_clients = []

            else:
                for client in self.clients:
                    if client != conn:
                        client.sendall(data)
                        print(f"Sending to other client {data.decode()}")

    def run_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server started listening on {self.port}")

            while True:
                conn, addr = s.accept()
                start_new_thread(self.threaded_client, (conn, addr))


s = Server("127.0.0.1",
           2222)  # server should be initialized in a bootstrap/main file, host ip and port should be taken from .env file/be constants
s.run_server()
