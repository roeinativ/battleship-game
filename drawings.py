class Drawings:
    def __init__(self, board, enemy_board=None):
        self.board = board
        self.enemy_board = enemy_board

    def draw_board(self, rows, columns):
        # Draw header
        header = "   "
        for col in range(columns):
            col_num = col + 1
            if col_num < 10:
                header += f" {col_num} "
            else:
                header += f"{col_num} "
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
                    header += f"{col_num} "
                if col < columns - 1:
                    header += "|"

        print(header)

        # Draw rows
        for r in range(rows):
            actual_row = r + 1  # Convert to 1-based indexing for display
            row_str = f" {actual_row} " if actual_row < 10 else f"{actual_row} "

            for c in range(columns):
                actual_col = c + 1  # Convert to 1-based indexing for display
                shape = self.board.get_matrix()[actual_row][actual_col]
                if not shape:
                    row_str += "   "
                else:
                    row_str += f" {shape} "
                if c < columns - 1:
                    row_str += "|"

            # Draw enemy board if present
            if self.enemy_board is not None:
                row_str += "          "
                row_str += f" {actual_row} " if actual_row < 10 else f"{actual_row} "
                for c in range(columns):
                    actual_col = c + 1  # Convert to 1-based indexing for display
                    if isinstance(self.enemy_board, list):
                        # For list type, use r and c (0-based)
                        shape = self.enemy_board[r][c]
                    else:
                        # For Board object type, use actual_row and actual_col (1-based)
                        shape = self.enemy_board.get_matrix()[actual_row][actual_col]
                    if not shape:
                        row_str += " ~ "
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

    def fill_empty_spaces_with_water(self):
        rows = len(self.board.get_matrix())
        cols = len(self.board.get_matrix()[0]) if rows > 0 else 0

        for i in range(rows):
            for j in range(cols):
                current_value = self.board.get_matrix()[i][j]
                if not current_value or str(current_value).strip() == "":
                    self.board.get_matrix()[i][j] = "~"

        if self.enemy_board is not None and not isinstance(self.enemy_board, list):
            enemy_rows = len(self.enemy_board.get_matrix())
            enemy_cols = len(self.enemy_board.get_matrix()[0]) if enemy_rows > 0 else 0

            for i in range(enemy_rows):
                for j in range(enemy_cols):
                    current_value = self.enemy_board.get_matrix()[i][j]
                    if not current_value or str(current_value).strip() == "":
                        self.enemy_board.get_matrix()[i][j] = "~"