class Whompus:
    def __init__(self):
        self.state_dic = {
            0: "Nothing here, but you're alive...",
            1: "Glitter!",
            2: "Stench!",
            3: "Breeze",
            5: "Stench and Breeze!",
            6: "Stench, Breeze and Glitter!",
            7: "You got eaten by the Whompus :()",
            9: "You fell into a pit! :[]"
        }

        self.world = [
            [2, 0, 3, 9],
            [7, 6, 9, 3],
            [2, 0, 3, 0],
            [0, 3, 9, 3]
        ]

        self.agent_pos = [3, 0]  # Agent's starting position
        self.has_gold = False  # Flag to check if the agent has the gold
        self.end_game = False  # Flag to check if the game has ended

    def get_state_no(self):
        return self.world[self.agent_pos[0]][self.agent_pos[1]]

    def print_state(self):
        print(self.state_dic[self.get_state_no()])

    def state_step(self):
        n = self.get_state_no()
        self.print_state()
        if n in [7, 9]:  # Check for game-ending states
            print("Game Over. Better luck next time!")
            self.end_game = True

        if n == 6:  # Check if the agent found the gold
            print("You found the Gold!")
            self.has_gold = True  # Corrected to refer to the instance variable

        # Check if the agent has returned to the start position with the gold
        if self.agent_pos == [3, 0] and self.has_gold:
            print("** Congrats! ** You Won! OoO **")
            self.end_game = True

    def move(self, move):
        if self.end_game:  # Prevent moves after the game has ended
            print("Game has already ended.")
            return

        X, Y = self.agent_pos
        if move == 'w':
            X -= 1
        elif move == 's':
            X += 1
        elif move == 'a':
            Y -= 1
        elif move == 'd':
            Y += 1
        else:
            print("Invalid move")
            return

        if X not in range(4) or Y not in range(4):
            print("You'd go out of range!")
            return

        # Execute Validated move
        self.agent_pos = [X, Y]
        self.state_step()

def play_whompus():
    game = Whompus()
    print("Welcome to Whompus World!\n")
    print("Current state: ")
    game.print_state()
    while not game.end_game:
        move = input("\nMove (w, a, s, d) or 'q' to quit: ").lower()
        if move == 'q':
            print("\nExiting game. Goodbye!\n\n")
            break
        game.move(move)

# Uncomment the next line to play the game when this script is executed

play_whompus()
