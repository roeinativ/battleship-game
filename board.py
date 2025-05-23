import copy

class Board:
    def __init__(self,rows,columns):
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        self.enemy_board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.submarine_position_list = []
        self.save_submarine_position_list = []

    # A function that get the board rows.
    def get_rows(self):
        return len(self.matrix)

    # A function that gets the board columns.
    def get_columns(self):
        return len(self.matrix[0])

    # A function that gets the board.
    def get_matrix(self):
        return self.matrix

    # A function that gets the submarine position list.
    def get_sub_pos(self):
        return self.submarine_position_list

    # A function that gets the enemy board.
    def get_enemy_board(self):
        return self.enemy_board

    # A function that gets a list and adds its position to the submarine position list.
    def add_arr_pos(self,arr):
        self.submarine_position_list.append(arr)

    # A function that gets a position and a shape and adds it to the board.
    def add_shape(self,pos,shape):
        row, column = pos
        self.matrix[row][column] = shape

    # A function that creates a complete separate copy of the submarine position list on order to save it.
    def set_save_pos(self,arr):
        self.save_submarine_position_list = copy.deepcopy(arr)

    # A function that fills all the spaces that are not submarine to be water.
    def fill_water(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != "S":
                    self.matrix[i][j] = "~"
        for i in range(len(self.enemy_board)):
            for j in range(len(self.enemy_board[i])):
                self.enemy_board[i][j] = "~"

    # A function that checks if a list is placed horizontally if yes returns true.
    def check_horizontal(self,arr):
        if len(arr) > 1:
            if arr[0][0] - arr[1][0] == 0:
                return True
        return False

    # A function that gets the position the other player fired at, checks if it hit and returns a message based on that.
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
                            return "hit"

                    self.surround_stars(self.save_submarine_position_list[i],self.matrix)
                    return self.save_submarine_position_list[i]

        if self.matrix[row][column] == "X" or self.matrix[row][column] == "*":
            return "again"

        elif self.matrix[row][column] == "~":
            print("Enemy has missed")
            self.add_shape(pos,"*")
            return "miss"

    # A function that gets a list a board and surrounds that submarine with stars.
    def surround_stars(self, arr, board):
        for row, col in arr:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    r, c = row + dr, col + dc
                    if (r, c) not in arr and 0 <= r < len(board) and 0 <= c < len(board[0]):
                            board[r][c] = "*"

    # A function that checks if there are no submarines on the board anymore and returns true or false based on that.
    def check_game_over(self):
        for i in range(len(self.submarine_position_list)):
            for j in range(len(self.submarine_position_list[i])):
                if self.submarine_position_list[i][j][0] != -1 or self.submarine_position_list[i][j][1] != -1:
                    return False
        return True

    # A function that cleans the board.
    def clean_board(self,rows,columns):
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        self.enemy_board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.submarine_position_list = []
        self.save_submarine_position_list = []