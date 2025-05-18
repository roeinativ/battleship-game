import ast
import time

from board import Board


class GameManager:

    def __init__(self,board,player,client,draw):
        self.board = board
        self.player = player
        self.client = client
        self.draw = draw




    def start_game(self):
        self.client.use_client()
        game_on = True
        while game_on:
            if self.player.choose_submarine_position():
                self.board.fill_water()
                print()
                self.draw.draw_board(self.board.get_rows() - 2,self.board.get_columns() - 2)
                arr = self.board.submarine_position_list
                self.board.set_save_pos(arr)
                self.client.send_messages("ready")

            print("Waiting for enemy to respond...")
            self.client.await_for_message()

            t = int(self.client.last_message)
            self.client.clean_message()
            print("Game begins")
            game_loop = True
            while game_loop:

                if t == 1:
                    print("Your turn")
                    fire_row = self.player.fire_row()
                    fire_column = self.player.fire_column()
                    self.client.send_messages(str((fire_row,fire_column)))
                    self.client.clean_message()
                    self.client.await_for_message()


                    if self.client.last_message not in ["true","false","again","over"]:
                        self.board.get_enemy_board()[fire_row][fire_column] = "X"
                        print("reached")
                        self.board.surround_stars(ast.literal_eval(self.client.last_message),self.board.get_enemy_board())
                        self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                        print("You have destroyed a ship!")



                    elif self.client.last_message == "true":
                        self.board.get_enemy_board()[fire_row][fire_column] = "X"
                        self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                        print("HIT!, you have another turn")

                    elif self.client.last_message == "again":
                        print("You have already hit that place")

                    elif self.client.last_message == "false":
                        self.board.get_enemy_board()[fire_row][fire_column] = "*"
                        self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                        self.client.send_messages("miss")
                        print("You have missed")
                        t = 0

                    time.sleep(0.5)
                    if self.client.last_message == "over":
                        print("You have won the game!")
                        if self.player.play_again():
                            self.client.send_messages("yes")
                            self.board.clean_board(self.board.get_rows(),self.board.get_columns())
                            game_loop = False

                            self.client.clean_message()
                            self.client.await_for_message()


                            if self.client.last_message == "stop":
                                game_loop = False
                                game_on = False

                            self.client.clean_message()
                        else:
                            self.client.send_messages("no")
                            print("Waiting for enemy to respond...")
                            self.client.clean_message()
                            self.client.await_for_message()
                            self.client.s.close()


                            game_loop = False
                            game_on = False


                elif t == 0:
                    print("Enemy turn, waiting for his move...")
                    self.client.clean_message()
                    self.client.await_for_message()

                    if self.client.last_message == "miss":
                        self.client.clean_message()
                        t = 1

                    else:
                        message = self.board.check_hit(ast.literal_eval(self.client.last_message))
                        self.client.send_messages(str(message))


                        if message != "again":
                            self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                        self.client.clean_message()



                        if self.board.check_game_over():
                            time.sleep(0.5)
                            self.client.send_messages("over")
                            print("You have lost the game")

                            if self.player.play_again():
                                self.client.send_messages("yes")
                                self.board.clean_board(self.board.get_rows(), self.board.get_columns())
                                game_loop = False


                                self.client.clean_message()
                                self.client.await_for_message()

                                if self.client.last_message == "stop":
                                    game_loop = False
                                    game_on = False

                                self.client.clean_message()
                            else:
                                self.client.send_messages("no")
                                print("Waiting for enemy to respond...")
                                self.client.clean_message()
                                self.client.await_for_message()
                                self.client.s.close()


                                game_loop = False
                                game_on = False



