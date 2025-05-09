class Board:
    def __init__(self,rows,columns):
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        self.submarine_position_list = []

    def get_rows(self):
        return len(self.matrix)

    def get_columns(self):
        return len(self.matrix[0])

    def get_matrix(self):
        return self.matrix

    def get_sub_pos(self):
        return self.submarine_position_list

    def add_arr_pos(self,arr):
        self.submarine_position_list.append(arr)

    def add_shape(self,pos,shape):
        row, column = pos
        self.matrix[row][column] = shape

    def check_hit(self,pos):
        row, column = pos
        for i in range(len(self.submarine_position_list)):
            for j in range(len(self.submarine_position_list[i])):
                if self.submarine_position_list[i][j][0] == row and self.submarine_position_list[i][j][1] == column:
                    self.submarine_position_list[i][j] = (-1,-1)
                    self.add_shape(pos,"X")
                    return True

        if self.matrix[row][column] == "X" or self.matrix[row][column] == "*":
            return "again"



