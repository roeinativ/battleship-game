import socket
from _thread import start_new_thread
import time

class Client:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.last_message = None


    def receive_messages(self):
        while True:
            data = self.s.recv(1024)
            if not data:
                self.s.close()
                break
            print(f"Received message: {data.decode()}")
            self.last_message = data.decode()

    def send_messages(self,message):
        if message:
            self.s.sendall(message.encode())


    def use_client(self):
            self.s.connect((self.host,self.port))
            print(f"Connected on port {self.port}")
            start_new_thread(self.receive_messages, ())

    def await_for_message(self):
        while self.last_message is None:
            time.sleep(0.5)

    def clean_message(self):
        self.last_message = None