import socket
from _thread import start_new_thread
import time

class Client:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.last_message = None


    # A function that listens for messages and saves the last one into one variable.
    def receive_messages(self):
        while True:
            try:
                data = self.s.recv(1024)
                if not data:
                    break
                self.last_message = data.decode()
            except:
                break

    # A function that send a message to the other client through the server, the message is passed as parameter.
    def send_messages(self,message):
        if message:
            self.s.sendall(message.encode())

    # A function that connects the client onto the server using the ip and port of the server and opens a new thread.
    def use_client(self):
            self.s.connect((self.host,self.port))
            start_new_thread(self.receive_messages, ())

    # A function that makes the client wait until he gets a message.
    def await_for_message(self):
        while self.last_message is None:
            time.sleep(0.5)

    # A function that cleans the last message the client has received.
    def clean_message(self):
        self.last_message = None