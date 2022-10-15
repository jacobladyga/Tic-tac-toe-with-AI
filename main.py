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

    def get_coords_ai(self, condition):
        """
        Return coordinates for AI.
        
        """
        coords = [k for k, v in self.cells.items() if v == condition]
        return coords[0]

    def ai_medium(self, symbol):
        """
        Makes a move by a medium AI.
        
        """
        msg = 'Making move level "medium"'
        while True:
            if self.can_win_row("X"):
                print(msg)
                self.update_grid(self.can_win_row("X"), symbol)
                break
            elif self.can_win_col("X"):
                print(msg)
                self.update_grid(self.can_win_col("X"), symbol)
                break
            elif self.can_win_diag("X"):
                print(msg)
                self.update_grid(self.can_win_diag("X"), symbol)
                break
            elif self.can_win_row("O"):
                print(msg)
                self.update_grid(self.can_win_row("O"), symbol)
                break
            elif self.can_win_diag("O"):
                print(msg)
                self.update_grid(self.can_win_diag("O"), symbol)
                break
            elif self.can_win_col("O"):
                print(msg)
                self.update_grid(self.can_win_col("O"), symbol)
                break
            else:
                random_index = random.randint(0, (len(self.grid) - 1))
                coords = self.get_coords_ai(random_index)
                if self.grid[random_index] == " ":
                    print(msg)
                    self.update_grid(coords, symbol)
                    break

    def ai_easy(self, symbol):
        """
        Makes a move by an easy AI.
        
        """
        while True:
            random_index = random.randint(0, (len(self.grid) - 1))
            coords = self.get_coords_ai(random_index)

            if self.grid[random_index] == " ":
                print('Making move level "easy"')
                self.update_grid(coords, symbol)
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

    def can_win_row(self, symbol):
        """
        Checks if there are 2 symbols in a row and returns coordinates
        of the empty cell as a tuple.
        
        """
        first_row = self.grid[0:3]
        second_row = self.grid[3:6]
        third_row = self.grid[6:9]
        if first_row.count(symbol) > 1 and " " in first_row:
            if first_row.index(" ") == 0:
                return self.get_coords_ai(first_row.index(" ")) 
            if first_row.index(" ") == 1:
                return self.get_coords_ai(first_row.index(" "))  
            if first_row.index(" ") == 2:
                return self.get_coords_ai(first_row.index(" ")) 
        elif second_row.count(symbol) > 1 and " " in second_row:
            if second_row.index(" ") == 0:
                return self.get_coords_ai(second_row.index(" ") + 3)
            if second_row.index(" ") == 1:
                return self.get_coords_ai(second_row.index(" ") + 3) 
            if second_row.index(" ") == 2:
                return self.get_coords_ai(second_row.index(" ") + 3) 
        elif third_row.count(symbol) > 1 and " " in third_row:
            if third_row.index(" ") == 0:
                return self.get_coords_ai(third_row.index(" ") + 6)
            if third_row.index(" ") == 1:
                return self.get_coords_ai(third_row.index(" ") + 6)
            if third_row.index(" ") == 2:
                return self.get_coords_ai(third_row.index(" ") + 6)
        else:
            return False   

    def can_win_col(self, symbol):
        """
        Checks if there are 2 symbols in a column. Method takes
        each cell from each column and adds it to a new list(Each list
        represents specific column). Method returns the exact coordinates
        of the empty cell or returns False if there are no 2 symbols in the column.
        
        """
        col1 = []
        col2 = []
        col3 = []

        col1.extend([self.grid[0], self.grid[3], self.grid[6]])
        col2.extend([self.grid[1], self.grid[4], self.grid[7]])
        col3.extend([self.grid[2], self.grid[5], self.grid[8]])

        if col1.count(symbol) > 1 and " " in col1:
            if col1.index(" ") == 0:
                return self.get_coords_ai(col1.index(" ")) 
            if col1.index(" ") == 1:
                return self.get_coords_ai(col1.index(" ") + 2) 
            if col1.index(" ") == 2:
                return self.get_coords_ai(col1.index(" ") + 4)
        elif col2.count(symbol) > 1 and " " in col2:
            if col2.index(" ") == 0:
                return self.get_coords_ai(col2.index(" ") + 1)
            if col2.index(" ") == 1:
                return self.get_coords_ai(col2.index(" ") + 3)
            if col2.index(" ") == 2:
                return self.get_coords_ai(col2.index(" ") + 5)
        elif col3.count(symbol) > 1 and " " in col3:
            if col3.index(" ") == 0:
                return self.get_coords_ai(col3.index(" ") + 2)
            if col3.index(" ") == 1:
                return self.get_coords_ai(col3.index(" ") + 4)
            if col3.index(" ") == 2:
                return self.get_coords_ai(col3.index(" ") + 6)
        else:
            return False  

    def can_win_diag(self, symbol):
        """
        Checks if there are 2 symbols on the diagonal. Method takes
        each cell from each diagonal and adds it to a new list(Each list
        represents specific diagonal). Method returns the exact coordinates
        of the empty cell or returns False if there are no 2 symbols on the diagonal.
        
        """
        diag1 = []
        diag2 = []

        diag1.extend([self.grid[0], self.grid[4], self.grid[8]])
        diag2.extend([self.grid[6], self.grid[4], self.grid[2]])

        if diag1.count(symbol) > 1 and " " in diag1:
            if diag1.index(" ") == 0:
                return self.get_coords_ai(diag1.index(" "))
            elif diag1.index(" ") == 1:
                return self.get_coords_ai(diag1.index(" ") + 3)
            elif diag1.index(" ") == 2:
                return self.get_coords_ai(diag1.index(" ") + 6)
        elif diag2.count(symbol) > 1 and " " in diag2:
            if diag2.index(" ") == 0:
                return self.get_coords_ai(diag2.index(" ") + 6)
            elif diag2.index(" ") == 1:
                return self.get_coords_ai(diag2.index(" ") + 3)
            elif diag2.index(" ") == 2:
                return self.get_coords_ai(diag2.index(" ")) 
        else:
            return False

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
        """
        Method starts a game.
        
        """
        mode = list(self.get_mode())
        self.clear_grid()
        self.display()
        while True:
            if mode[0] == 'user':
                self.player_move("X")
            elif mode[0] == 'medium':
                self.ai_medium("X")
            else:
                self.ai_easy("X")

            if self.check_winner():
                self.play()

            if mode[1] == 'user':
                self.player_move("O")
            elif mode[1] == 'medium':
                self.ai_medium("O")
            else:
                self.ai_easy("O")

            if self.check_winner():
                self.play()

                 
d = TicTacToe()
d.play()
