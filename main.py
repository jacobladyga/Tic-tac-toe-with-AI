import random

class TicTacToe:
    """
    A class to represent a Tic Tac Toe game.

    """

    def __init__(self):
        self.possible_modes = ['easy', 'user', 'medium']
        self.grid = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "
            ]
        self.cells = {
            (1, 1): 0,
            (1, 2): 1,
            (1, 3): 2,
            (2, 1): 3,
            (2, 2): 4,
            (2, 3): 5,
            (3, 1): 6,
            (3, 2): 7,
            (3, 3): 8,
        }

    def display(self):
        """
        Displays a grid of symbols.

        """
        print(9 * "-")
        print(f"| {self.grid[0]} {self.grid[1]} {self.grid[2]} |")
        print(f"| {self.grid[3]} {self.grid[4]} {self.grid[5]} |")
        print(f"| {self.grid[6]} {self.grid[7]} {self.grid[8]} |")
        print(9 * "-")

    def clear_grid(self):
        """
        Clears a grid.
        
        """
        self.grid = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "
            ]

    def ai_easy(self, symbol):
        """
        Makes a move by an AI.
        
        """
        while True:
            random_index = random.randint(0, (len(self.grid) - 1))
            coords = [k for k, v in self.cells.items() if v == random_index]

            if self.grid[random_index] == " ":
                print('Making move level "easy"')
                self.update_grid(coords[0], symbol)
                break
              
    def player_move(self, symbol):
        """
        Makes a move by a player.
        
        """
        while True:
            coords = []
            try:
                coord1, coord2 = input("Enter the coordinates: ").split()
                c1 = int(coord1)
                c2 = int(coord2)   
                if (c1 > 3 or c1 < 1) or (c2 > 3 or c2 < 1):
                    print("Coordinates should be from 1 to 3!")
                    continue
                else:
                    coords.append(c1)
                    coords.append(c2)
                    if self.grid[self.cells[tuple(coords)]] != " ":
                        print("This cell is occupied! Choose another one!")
                        continue
                    else:
                        self.update_grid(coords, symbol)
                        return tuple(coords)
            except ValueError:
                print("You should enter numbers!")
                
    def update_grid(self, coords, symbol):
        """
        Takes coordinates from user or ai and updates a grid.
        
        """     
        if self.grid[self.cells[tuple(coords)]] == " ":
            self.grid[self.cells[tuple(coords)]] = symbol
            self.display()       

    def check_row(self, symbol):
        """
        Checks if there are three same symbols on a row.
        
        """
        if self.grid[0] == symbol and self.grid[1] == symbol and self.grid[2] == symbol:
            return True
        elif self.grid[3] == symbol and self.grid[4] == symbol and self.grid[5] == symbol:
            return True
        elif self.grid[6] == symbol and self.grid[7] == symbol and self.grid[8] == symbol:
            return True
        else:
            return False

    def check_col(self, symbol):
        """
        Checks if there are three same symbols in a column.
        
        """
        if self.grid[0] == symbol and self.grid[3] == symbol and self.grid[6] == symbol:
            return True
        elif self.grid[1] == symbol and self.grid[4] == symbol and self.grid[7] == symbol:
            return True
        elif self.grid[2] == symbol and self.grid[5] == symbol and self.grid[8] == symbol:
            return True
        else:
            return False

    def check_diag(self, symbol):
        """
        Checks if there are three same symbols on a diagonal line.
        
        """
        if self.grid[0] == symbol and self.grid[4] == symbol and self.grid[8] == symbol:
            return True
        elif self.grid[6] == symbol and self.grid[4] == symbol and self.grid[2] == symbol:
            return True
        else:
            return False
    
    def check_winner(self):
        """
        Checks if there is a winner.
        
        """
        wins = 0
        if self.check_col('X') or self.check_diag('X') or self.check_row('X'):
             wins += 1

        if self.check_col('O') or self.check_diag('O') or self.check_row('O'):
            wins += 1

        if self.check_col('X') or self.check_diag('X') or self.check_row('X'):
            if not self.check_col('O') or not self.check_diag('O') or not self.check_row('O'):
                print("X wins")
                return True
        elif self.check_col('O') or self.check_diag('O') or self.check_row('O'):
            if not self.check_col('X') or not self.check_diag('X') or not self.check_row('X'):
                print("O wins")
                return True
        elif self.grid.count(" ") == 0 and wins == 0:
            print("Draw")
            return True
        else:
            return False

    def get_mode(self):
        """
        Takes command from a user and return a mode.
        
        """
        error_msg = "Bad parameters!"
        while True:
            command = input("Input command: ").split()
            if command[0] == "exit":
                exit()
            elif command[0] == "start":
                try:
                    if command[1] not in self.possible_modes or command[2] not in self.possible_modes:
                        print(error_msg)
                    else:     
                        return command[1], command[2]                 
                except IndexError:
                    print(error_msg)
            else:
                print(error_msg)
    
    def play(self):
        mode = list(self.get_mode())
        self.clear_grid()
        self.display()
        while True:
            if mode[0] == 'user':
                self.player_move("X")
            else:
                self.ai_easy("X")
            if self.check_winner():
                self.play()
            if mode[1] == 'user':
                self.player_move("O")
            else:
                self.ai_easy("O")
            if self.check_winner():
                self.play()

                 
d = TicTacToe()
d.play()
