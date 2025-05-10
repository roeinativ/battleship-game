from tabnanny import check


class Player:
    def __init__(self,draw,board,submarine_size):
        self.draw = draw
        self.board = board
        self.submarine_size = submarine_size

    def choose_submarine_position(self):
            player_choice = input("Welcome to battleship for 2 players, choose to place your ships manually or randomize their position [r/p]: ")
            if player_choice == "p":
                for i in range(len(self.submarine_size)):
                    points = 0
                    check = True
                    while check:
                        check_full = True
                        print(f"Ship size of {self.submarine_size[i]}")
                        while check_full:
                            arr = self.place_submarine(i)
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
                                    check = False
                                    for k in range(len(arr)):
                                        self.board.get_matrix()[arr[k][0]][arr[k][1]] = "S"
                                    self.board.add_arr_pos(arr)
                                    self.draw.draw_board(self.board.get_rows() - 2,self.board.get_columns() - 2)
                return True




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


    def place_direction(self):
        check = True
        while check:
            place_direction = input("Enter the direction of the ship: ")
            if place_direction.isalpha() and place_direction == "right" or place_direction == "left" or place_direction == "up" or place_direction == "down":
                return place_direction
            else:
                print("You must type the direction of the ship")

    def place_submarine(self, i):
        row = self.place_row()
        column = self.place_column()
        arr = [(row, column)]

        if self.submarine_size[i] > 1:
            direction = self.place_direction()
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
        for i in range(len(arr)):
            row = arr[i][0]
            col = arr[i][1]

            if i == 0:
                if col - 1 < 0:
                    return False
                if self.board.get_matrix()[row][col - 1] == "S":
                    return False
                if row - 1 < 0 or self.board.get_matrix()[row - 1][col - 1] == "S":
                    return False
                if row + 1 >= self.board.get_rows() or self.board.get_matrix()[row + 1][col - 1] == "S":
                    return False

            elif i == len(arr) - 1:
                if col + 1 >= self.board.get_columns():
                    return False
                if self.board.get_matrix()[row][col + 1] == "S":
                    return False
                if row - 1 < 0 or self.board.get_matrix()[row - 1][col + 1] == "S":
                    return False
                if row + 1 >= self.board.get_rows() or self.board.get_matrix()[row + 1][col + 1] == "S":
                    return False

            else:
                if row + 1 >= self.board.get_rows() or self.board.get_matrix()[row + 1][col] == "S":
                    return False
                if row - 1 < 0 or self.board.get_matrix()[row - 1][col] == "S":
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
            play_again = input("Game over, do you want to play again [y/n]: ")
            if play_again.isalpha():
                if play_again == "y":
                    return True
                elif play_again == "n":
                    return False
            else:
                print("You must enter a letter")









