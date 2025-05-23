import socket
import time
from _thread import start_new_thread
from ctypes import c_char
from datetime import datetime
from distutils.command.clean import clean


class Server:

    def __init__(self,host,port):
        self.host =  host
        self.port = port
        self.clients = []
        self.ready_clients = []
        self.game_over_clients = []
        self.turn = 0


    def update_stat_file(self):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("stat.csv","a") as file:
            file.write(f"{date},{self.turn}\n")



    def threaded_client(self,conn,addr):
        print(f"Connected {addr}")
        self.clients.append(conn)

        while True:
            try:
                data = conn.recv(1024)

                if not data:
                    print("Disconnected")
                    conn.close()
                    self.clients.remove(conn)
                    break


                print(f"Received from {addr}: {data.decode()}")

                if data.decode() == "ready":
                    self.ready_clients.append(conn)
                    if len(self.ready_clients) == 2:
                        self.ready_clients[0].sendall("1".encode())
                        self.ready_clients[1].sendall("0".encode())


                elif data.decode() in ["True", "False"]:
                    game_over = False
                    self.game_over_clients.append(conn)
                    if data.decode() == "False":
                        game_over = True

                    if len(self.game_over_clients) == 2:
                        for client in self.game_over_clients:
                            if game_over:
                                client.sendall("disconnect".encode())
                                request = client.recv(1024).decode()

                                if request == "requested_disconnect":
                                    print(f"Client {client} disconnected")
                                    client.close()

                            else:
                                client.sendall("True".encode())

                        self.ready_clients = []
                        self.game_over_clients = []

                        break


                elif data.decode() == "destroyed":
                    self.turn += 1




                else:
                    if data.decode() in ["hit","miss"]:
                        self.turn += 1
                        print(self.turn)
                    for client in self.clients:
                        if client != conn:
                            client.sendall(data)
                            print(f"Sending to other client {data.decode()}")

                    if data.decode() == "over":
                        self.update_stat_file()
                        self.turn = 0
            except ConnectionResetError:
                conn.close()
                break





    def run_server(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((self.host,self.port))
            s.listen()
            print(f"Server started listening on {self.port}")

            while True:
                conn, addr = s.accept()
                start_new_thread(self.threaded_client,(conn, addr))



s = Server("127.0.0.1",2222)
s.run_server()