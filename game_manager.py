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
            self.board.fill_water()
            self.draw.fill_empty_spaces_with_water()
            print()
            self.draw.draw_board(self.board.get_rows() - 2,self.board.get_columns() - 2)
            self.client.send_messages("ready")

        self.client.await_for_message()

        t = int(self.client.last_message)
        self.client.clean_message()
        print("Game begins")
        game_on = True
        while game_on:
            if t == 1:
                fire_row = self.player.fire_row()
                fire_column = self.player.fire_column()
                self.client.send_messages(str((fire_row,fire_column)))
                self.client.clean_message()
                self.client.await_for_message()
                if self.client.last_message == "true":
                    self.board.get_enemy_board()[fire_row][fire_column] = "X"
                    self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                    print("HIT!, you have another turn")

                elif self.client.last_message == "again":
                    print("You have already hit that place")

                else:
                    print("You have missed")
                    self.board.get_enemy_board()[fire_row][fire_column] = "*"
                    self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                    self.client.send_messages("miss")
                    t = 0


            elif t == 0:
                print("Enemy turn, waiting for his move...")
                self.client.clean_message()
                self.client.await_for_message()

                if self.client.last_message == "miss":
                    self.client.clean_message()
                    t = 1

                else:
                    self.client.send_messages(self.board.check_hit(ast.literal_eval(self.client.last_message)))
                    self.client.clean_message()


