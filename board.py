import copy

class Board:
    def __init__(self,rows,columns):
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        self.enemy_board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.submarine_position_list = []
        self.save_submarine_position_list = []


    def get_rows(self):
        return len(self.matrix)

    def get_columns(self):
        return len(self.matrix[0])

    def get_matrix(self):
        return self.matrix

    def get_sub_pos(self):
        return self.submarine_position_list

    def get_enemy_board(self):
        return self.enemy_board

    def add_arr_pos(self,arr):
        self.submarine_position_list.append(arr)

    def add_shape(self,pos,shape):
        row, column = pos
        self.matrix[row][column] = shape

    def set_save_pos(self,arr):
        self.save_submarine_position_list = copy.deepcopy(arr)

    def fill_water(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != "S":
                    self.matrix[i][j] = "~"
        for i in range(len(self.enemy_board)):
            for j in range(len(self.enemy_board[i])):
                self.enemy_board[i][j] = "~"

    def check_horizontal(self,arr):
        if len(arr) > 1:
            if arr[0][0] - arr[1][0] == 0:
                return True
        return False

    def check_hit(self,pos):
        row, column = pos
        for i in range(len(self.submarine_position_list)):
            for j in range(len(self.submarine_position_list[i])):
                if self.submarine_position_list[i][j][0] == row and self.submarine_position_list[i][j][1] == column:
                    self.submarine_position_list[i][j] = (-1,-1)
                    self.add_shape(pos,"X")
                    print("Enemy has hit a ship")

                    for c in range(len(self.submarine_position_list[i])):
                        if self.submarine_position_list[i][c] != (-1,-1):
                            return "true"

                    self.surround_stars(self.save_submarine_position_list[i],self.matrix)
                    return self.save_submarine_position_list[i]

        if self.matrix[row][column] == "X" or self.matrix[row][column] == "*":
            return "again"

        elif self.matrix[row][column] == "~":
            print("Enemy has missed")
            self.add_shape(pos,"*")
            return "false"

    def surround_stars(self, arr, board):
        for i in range(len(arr)):
            row = arr[i][0]
            col = arr[i][1]

            if self.check_horizontal(arr):
                if i == 0:
                    board[row][col - 1] = "*"
                    board[row - 1][col - 1] = "*"
                    board[row + 1][col - 1] = "*"

                if i == len(arr) - 1 or len(arr) == 1:
                    board[row][col + 1] = "*"
                    board[row + 1][col + 1] = "*"
                    board[row - 1][col + 1] = "*"

                board[row + 1][col] = "*"
                board[row - 1][col] = "*"

            else:
                if i == 0:
                    board[row - 1][col] = "*"
                    board[row - 1][col - 1] = "*"
                    board[row - 1][col + 1] = "*"

                if i == len(arr) - 1 or len(arr) == 1:
                    board[row + 1][col] = "*"
                    board[row + 1][col + 1] = "*"
                    board[row + 1][col - 1] = "*"

                board[row][col + 1] = "*"
                board[row][col - 1] = "*"

    def check_game_over(self):
        for i in range(len(self.submarine_position_list)):
            for j in range(len(self.submarine_position_list[i])):
                if self.submarine_position_list[i][j][0] != -1 or self.submarine_position_list[i][j][1] != -1:
                    return False
        return True