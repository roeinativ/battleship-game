import socket
from _thread import start_new_thread
from datetime import datetime



class Server:

    def __init__(self,host,port):
        self.host =  host
        self.port = port
        self.clients = []
        self.ready_clients = []
        self.game_over_clients = []
        self.turn = 0


    # A function that updates the moves statistics file of the game, adds current date and number of moves.
    def update_stat_file(self):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("stat.csv","a") as file:
            file.write(f"{date},{self.turn}\n")


    # A function that makes so the server listens from messages from other clients and knows what to do with them and where send them.
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

                # Checks if the player finished placing the submarines.
                if data.decode() == "ready":
                    self.ready_clients.append(conn)
                    if len(self.ready_clients) == 2:
                        self.ready_clients[0].sendall("1".encode())
                        self.ready_clients[1].sendall("0".encode())

                # Checks if the player wants to play again.
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

                # Check if the entire submarine was destroyed.
                elif data.decode() == "destroyed":
                    self.turn += 1



                # Passes the positions of where the client shot the other client, and adds to the turn counter.
                else:
                    if data.decode() in ["hit","miss"]:
                        self.turn += 1
                        print(self.turn)
                    for client in self.clients:
                        if client != conn:
                            client.sendall(data)
                            print(f"Sending to other client {data.decode()}")

                    # Checks if the game has ended.
                    if data.decode() == "over":
                        self.update_stat_file()
                        self.turn = 0
            except ConnectionResetError:
                conn.close()
                break




    # A function that runs the server, listens for clients and opens a thread to those who connect.
    def run_server(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((self.host,self.port))
            s.listen()
            print(f"Server started listening on {self.port}")

            while True:
                conn, addr = s.accept()
                start_new_thread(self.threaded_client,(conn, addr))


# Give the server the ip and port and run it.
s = Server("127.0.0.1",2222)
s.run_server()