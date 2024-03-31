import random

class ConnectFour:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]
        self.player_turn = "X"  # X will start, O is the second player

    def print_grid(self):
        for row in self.grid:
            print("|" + "|".join(row) + "|")
        print("-" * (2 * self.columns + 1))

    def drop_disc(self, column):
        if column < 0 or column >= self.columns or self.grid[0][column] != " ":
            return False
        for row in reversed(range(self.rows)):
            if self.grid[row][column] == " ":
                self.grid[row][column] = self.player_turn
                return True
        return False

    def check_win(self):
        # Horizontal, vertical, and diagonal checks
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] == " ":
                    continue
                for d_row, d_col in directions:
                    count = 0
                    for i in range(4):
                        r, c = row + i*d_row, col + i*d_col
                        if 0 <= r < self.rows and 0 <= c < self.columns and self.grid[r][c] == self.player_turn:
                            count += 1
                        else:
                            break
                    if count == 4:
                        return True
        return False

    def switch_turn(self):
        self.player_turn = "O" if self.player_turn == "X" else "X"

    def play_game(self):
        # This will be the game loop where players take turns
        while True:
            self.print_grid()
            try:
                column = int(input(f"Player {self.player_turn}, choose column (0-6): "))
            except ValueError:
                print("Please enter a valid column number.")
                continue
            if not self.drop_disc(column):
                print("Invalid move, try again.")
                continue
            if self.check_win():
                self.print_grid()
                print(f"Player {self.player_turn} wins!")
                break
            self.switch_turn()
            
    def get_grid_copy(self):
        return [[cell for cell in row] for row in self.grid]

    def ai_drop_disc(self, column):
        if self.drop_disc(column):
            if self.check_win():
                self.undo_move(column)
                return True
            self.undo_move(column)
        return False

    def undo_move(self, column):
        for row in range(self.rows):
            if self.grid[row][column] != " ":
                self.grid[row][column] = " "
                break


def simple_ai_best_first(game):
    # Attempt to find a winning move for AI or block player's winning move
    for column in range(game.columns):
        # Check if AI can win in the next move
        game.player_turn = "O"
        if game.ai_drop_disc(column):
            return column

        # Check if Player can win in the next move and block
        game.player_turn = "X"
        if game.ai_drop_disc(column):
            game.player_turn = "O"  # Switch back to AI
            return column

    # If no immediate win or block, choose a random column
    game.player_turn = "O"
    return random.choice([c for c in range(game.columns) if game.grid[0][c] == " "])


game = ConnectFour()
# simple_ai_best_first(game)
game.play_game()