from board import Board
from player import Player
from drawings import Drawings
from client import Client
from game_manager import GameManager

# Creates all the game instances and starts the game.

HOST = "127.0.0.1"
PORT = 3333
submarine_size = [1,1,1,1,2,2,2,3,3,4]

rows = 10
columns = 10

board = Board(12,12)
draw = Drawings(board)
player = Player(draw,board,submarine_size)
client = Client(HOST,PORT)

game_manager = GameManager(board,player,client,draw)

game_manager.start_game()