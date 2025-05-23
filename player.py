import random


class Player:
    def __init__(self,draw,board,submarine_size):
        self.draw = draw
        self.board = board
        self.submarine_size = submarine_size

    def choose_submarine_position(self):
            check1 = True
            while check1:
                player_choice = input("Welcome to battleship for 2 players, choose to place your ships manually or randomize their position [r/p]: ")
                if player_choice == "p":
                    check1 = False
                    for i in range(len(self.submarine_size)):
                        points = 0
                        check2 = True
                        while check2:
                            check_full = True
                            print(f"Ship size of {self.submarine_size[i]}")
                            while check_full:
                                arr = self.place_submarine(i,self.place_row(),self.place_column(),self.place_direction())
                                if not arr:
                                    print("You must place the submarine in a different location")
                                else:
                                    check_full = False
                                    for j in range(len(arr)):
                                        row,col = arr[j]
                                        if self.board.get_matrix()[row][col] == "S" or not self.check_surrounding(arr) or not arr:
                                            print("You must place the submarine in a different location")
                                            break
                                        else:
                                            points += 1
                                    if points == len(arr):
                                        check2 = False
                                        for k in range(len(arr)):
                                            self.board.get_matrix()[arr[k][0]][arr[k][1]] = "S"
                                        self.board.add_arr_pos(arr)
                                        self.draw.draw_board(self.board.get_rows() - 2,self.board.get_columns() - 2)
                    return True


                elif player_choice == "r":
                    try_pos = True
                    while try_pos:
                        self.board.clean_board(12,12)
                        successful_placements = 0


                        for i in range(len(self.submarine_size)):
                            place = True
                            while place:
                                arr = self.place_submarine(i, self.random_pos(), self.random_pos(), self.random_direction())

                                if arr and self.check_surrounding(arr):
                                    position_free = True
                                    for row,col in arr:
                                        if self.board.get_matrix()[row][col] == "S":
                                            position_free = False
                                            break
                                    if position_free:
                                        for row,col in arr:
                                            self.board.get_matrix()[row][col] = "S"
                                        self.board.add_arr_pos(arr)
                                    successful_placements += 1
                                    break

                        if successful_placements == len(self.submarine_size):
                            self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                            try_pos = False

                    return True



                else:
                    print("You must enter p or r")




    def place_row(self):
        check = True
        while check:
            try:
                place_row = int(input("Choose a row to place a part of the ship: "))
                if place_row <= 0 or place_row > self.board.get_rows() - 2:
                    print("You cant type a number bigger or lower than the number of rows on the board")
                else:
                    check = False
                    return place_row
            except ValueError:
                print("You cant type a number bigger or lower than the number of rows on the board")



    def place_column(self):
        check = True
        while check:
            try:
                place_column = int(input("Choose a column to place a part of the ship: "))
                if place_column <= 0 or place_column > self.board.get_columns() - 2:
                    print("You cant type a number bigger or lower than the number of columns on the board")
                else:
                    check = False
                    return place_column
            except ValueError:
                print("You cant type a number bigger or lower than the number of columns on the board")


    def random_pos(self):
        return random.randint(1,10)

    def random_direction(self):
        directions = ["right","left","up","down"]
        return random.choice(directions)

    def place_direction(self):
        check = True
        while check:
            place_direction = input("Enter the direction of the ship: ")
            if place_direction.isalpha() and place_direction == "right" or place_direction == "left" or place_direction == "up" or place_direction == "down":
                return place_direction
            else:
                print("You must type the direction of the ship")

    def place_submarine(self,i,row,column,direction):
        arr = [(row, column)]

        if self.submarine_size[i] > 1:
            for j in range(1, self.submarine_size[i]):
                if direction == "right":
                    column += 1
                    arr.append((row, column))
                elif direction == "left":
                    column -= 1
                    arr.append((row, column))
                elif direction == "up":
                    row -= 1
                    arr.append((row, column))
                elif direction == "down":
                    row += 1
                    arr.append((row, column))

        for i in range(len(arr)):
            if arr[i][0] >= self.board.get_rows() or arr[i][0] < 0 or arr[i][1] >= self.board.get_columns()  or arr[i][
                1] < 0:
                return []

        return arr

    def check_surrounding(self, arr):
        for row, col in arr:

            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1), (0, 1),
                          (1, -1), (1, 0), (1, 1)]

            for dr, dc in directions:
                r, c = row + dr, col + dc


                if 0 <= r < self.board.get_rows() and 0 <= c < self.board.get_columns():
                    if self.board.get_matrix()[r][c] == "S":
                        return False

        return True

    def fire_row(self):
        check = True
        while check:
            try:
                fire_row = int(input("Enter a row to fire: "))
                if fire_row <= 0 or fire_row > self.board.get_rows() - 2:
                    print("You can not enter a number bigger or lower than the number of rows on the board")
                else:
                    check = False
                    return fire_row
            except ValueError:
                print("You must enter a number")

    def fire_column(self):
        check = True
        while check:
            try:
                fire_column = int(input("Enter a column to fire: "))
                if fire_column <= 0 or fire_column > self.board.get_columns() - 2:
                    print("You can not enter a number bigger or lower than the number of rows on the board")
                else:
                    check = False
                    return fire_column
            except ValueError:
                print("You must enter a number")

    def play_again(self):
        check = True
        while check:
            play_again = input("Game over, do you want to play again [y/n] / you can type stat to se the statistics of the game: ")
            if play_again.isalpha():
                if play_again == "y":
                    return True
                elif play_again == "n":
                    return False
                elif play_again == "stat":
                    with open("stat.csv","r") as file:
                        print(file.read())


            else:
                print("You must enter a letter")



    def random_position(self):
        try_pos = True
        while try_pos:
            self.board.clean_board()
            placement_success = False
            for i in range(len(self.submarine_size)):
                arr = self.place_submarine(i,self.random_pos(),self.random_pos(),self.random_direction())
                for j in range(len(arr)):
                    row,col = arr[j]
                    if arr[row][col] == "S" or not self.check_surrounding(arr) or not arr:
                        print("You must place the submarine in a different location")
                        break
                    else:
                        for k in range(len(arr)):
                            self.board.get_matrix()[arr[k][0]][arr[k][1]] = "S"
                            self.board.add_arr_pos(arr)

                else:
                    print("Could not place ship restarting placement")

            if placement_success:
                break







