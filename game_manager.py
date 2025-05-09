import ast

class GameManager:

    def __init__(self,board,player,client,draw):
        self.board = board
        self.player = player
        self.client = client
        self.draw = draw




    def start_game(self):
        self.client.use_client()
        if self.player.choose_submarine_position():
            self.client.send_messages("ready")

        self.client.await_for_message()

        t = int(self.client.last_message)
        self.client.clean_message()
        game_on = True
        while game_on:
            if t == 1:
                fire_row = self.player.fire_row()
                fire_column = self.player.fire_column()
                self.client.send_messages(str((fire_row,fire_column)))
                self.client.clean_message()
                self.client.await_for_message()
                if bool(self.client.last_message):
                    print("HIT!")


            if t == 0:
                self.client.await_for_message()
                if self.board.check_hit(ast.literal_eval(self.client.last_message)):
                    self.client.send_messages(str(True))
                    self.client.clean_message()
