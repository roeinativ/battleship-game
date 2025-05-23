class Drawings:
    def __init__(self, board):
        self.board = board
        self.blue = "\033[34m"
        self.red = "\033[31m"
        self.yellow = "\033[33m"
        self.reset = "\033[0m"

    def get_colored_cell(self, val):
        if val == "S":
            return f"{self.blue} {val} {self.reset}"
        elif val == "X":
            return f"{self.red} {val} {self.reset}"
        elif val == "*":
            return f"{self.yellow} {val} {self.reset}"
        elif val == "~":
            return f"{self.reset} ~ {self.reset}"
        elif val in [0, None, ""]:
            return "   "
        else:
            return f" {val} "

    def draw_board(self, rows, columns):
        def build_header(columns):
            header = "   "
            for col in range(columns):
                col_num = col + 1
                header += f" {col_num}" if col_num < 10 else f" {col_num}"
                if col < columns - 1:
                    header += " |"
            return header

        your_header = build_header(columns)
        enemy_header = build_header(columns)

        mid_space = " " * 10
        print("\n YOUR BOARD " + " " * (len(your_header) - 11) + mid_space + "ENEMY BOARD")
        print(your_header + mid_space + enemy_header)

        for r in range(rows):
            row_label = f" {r + 1}" if r + 1 < 10 else f"{r + 1}"
            row_str = row_label + " "

            for c in range(columns):
                val = self.board.get_matrix()[r + 1][c + 1]
                row_str += self.get_colored_cell(val)
                if c < columns - 1:
                    row_str += "|"

            row_str += mid_space
            row_str += row_label + " "
            for c in range(columns):
                val = self.board.get_enemy_board()[r + 1][c + 1]
                row_str += self.get_colored_cell(val)
                if c < columns - 1:
                    row_str += "|"

            print(row_str)

            if r < rows - 1:
                sep = "   " + ("----" * columns)[:-1]
                sep += mid_space + "   " + ("----" * columns)[:-1]
                print(sep)

    def draw_welcome(self):
        print("""
         __        __   _                            _____     
         \ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__  
          \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
           \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |
         __ \_/\_/ \___|_|\___\___/|_| |_|_|_|\___|   |_|\___/ 
        | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __         
        |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \        
        | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |       
        |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/        
                                                |_|           
        """)


    def draw_game_over(self):
        print("""
          ____                         ___                 
         / ___| __ _ _ __ ___   ___   / _ \\__   _____ _ __ 
        | |  _ / _` | '_ ` _ \\ / _ \\ | | | \\ \\ / / _ \\ '__|
        | |_| | (_| | | | | | |  __/ | |_| |\\ V /  __/ |   
         \\____|\\__,_|_| |_| |_|\\___|  \\___/  \\_/ \\___|_|   
        """)
