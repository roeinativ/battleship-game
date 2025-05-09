class Drawings:
    def __init__(self, board, enemy_board=None):
        self.board = board
        self.enemy_board = enemy_board

    def draw_board(self, rows, columns):
        # Column headers with better alignment
        header = "   "
        for col in range(columns):
            col_num = col + 1
            if col_num < 10:
                header += f" {col_num} "
            else:
                header += f" {col_num}"

            if col < columns - 1:
                header += "|"

        if self.enemy_board is not None:
            header += "          "
            header += "   "
            for col in range(columns):
                col_num = col + 1
                if col_num < 10:
                    header += f" {col_num} "
                else:
                    header += f" {col_num}"

                if col < columns - 1:
                    header += "|"

        print(header)

        for r in range(rows):
            row_str = f" {r + 1} " if r + 1 < 10 else f"{r + 1} "

            for c in range(columns):
                shape = self.board.get_matrix()[r + 1][c + 1]

                if not shape:
                    row_str += "   "
                else:
                    row_str += f" {shape} "

                if c < columns - 1:
                    row_str += "|"

            if self.enemy_board is not None:
                row_str += "          "
                row_str += f" {r + 1} " if r + 1 < 10 else f"{r + 1} "

                for c in range(columns):
                    if isinstance(self.enemy_board, list):
                        shape = self.enemy_board[r][c]  # Use r and c directly for list indices
                    else:
                        shape = self.enemy_board.get_matrix()[r + 1][c + 1]

                    if not shape:
                        row_str += "   "
                    else:
                        row_str += f" {shape} "

                    if c < columns - 1:
                        row_str += "|"

            print(row_str)

            if r < rows - 1:
                separator = "   "
                for c in range(columns):
                    separator += "---"
                    if c < columns - 1:
                        separator += "+"

                if self.enemy_board is not None:
                    separator += "          "
                    separator += "   "
                    for c in range(columns):
                        separator += "---"
                        if c < columns - 1:
                            separator += "+"

                print(separator)