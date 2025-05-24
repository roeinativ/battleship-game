import random


class Player:
    def __init__(self,draw,board,submarine_size):
        self.draw = draw
        self.board = board
        self.submarine_size = submarine_size

    # A function that puts the player through the process of placing their submarines, if their placement is valid and returns true if all submarines placed.
    def choose_submarine_position(self):
            try_pos = True
            while try_pos:
                player_choice = input("Welcome to battleship for 2 players, choose to place your ships manually or randomize their position [r/p]: ")

                # Place manually
                if player_choice == "p":
                    for i in range(len(self.submarine_size)):
                        successful_placement = 0
                        place = True
                        while place:
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
                                            successful_placement += 1
                                    if successful_placement == len(arr):
                                        place = False
                                        for k in range(len(arr)):
                                            self.board.get_matrix()[arr[k][0]][arr[k][1]] = "S"
                                        self.board.add_arr_pos(arr)
                                        self.draw.draw_board(self.board.get_rows() - 2,self.board.get_columns() - 2)
                    return True

                # Randomize their positions.
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
                                    place = False

                        if successful_placements == len(self.submarine_size):
                            self.draw.draw_board(self.board.get_rows() - 2, self.board.get_columns() - 2)
                            try_pos = False

                    return True



                else:
                    print("You must enter p or r")



    # A function that inputs the placements row from the player and returns it.
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


    # A function that inputs the placements column from the player and returns it.
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

    # A function that randomizes a position that could be used as a random row and colum, and returns it.
    def random_pos(self):
        return random.randint(1,10)

    # A function that randomizes a direction and returns it.
    def random_direction(self):
        directions = ["right","left","up","down"]
        return random.choice(directions)

    # A function that inputs a direction from the player and returns it.
    def place_direction(self):
        check = True
        while check:
            place_direction = input("Enter the direction of the ship: ")
            if place_direction.isalpha() and place_direction == "right" or place_direction == "left" or place_direction == "up" or place_direction == "down":
                return place_direction
            else:
                print("You must type the direction of the ship")

    # A function that gets a row column and the direction the player chose and if the list created is within the boundaries of the board returns it.
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

    # A function that gets an arr and returns true if there are no ships around it.
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

    # A function that inputs a row to fire from the player and returns it.
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

    # A function that inputs a column to fire from the player and returns it.
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

    # A function that asks the player if he wants to play again if yes returns true and if no returns false. The function also lets you input stat to see the date and moves played of each match.
    def play_again(self):
        check = True
        while check:
            play_again = input("Game over, do you want to play again [y/n] / you can type stat to see the statistics of the game: ")
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