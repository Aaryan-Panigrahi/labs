import random

def generate_board():
    return [random.randint(0, 7) for _ in range(8)]

def calculate_cost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                cost += 1
            if abs(i - j) == abs(board[i] - board[j]):
                cost += 1
    return cost

def print_board(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def hill_climb():
    current_board = generate_board()
    current_cost = calculate_cost(current_board)

    #This iterates through all possible next moves and execute the on with the least cost..
    while current_cost > 0:
        next_board = list(current_board)
        for col in range(8):
            for row in range(8):
                if current_board[row] != col:
                    next_board[row] = col
                    cost = calculate_cost(next_board)
                    if cost < current_cost:
                        current_cost = cost
                        current_board = list(next_board)
        if current_cost == calculate_cost(current_board):
            break

    return current_board

if __name__ == "__main__":
    solution = hill_climb()
    print("Some Solution found:")
    print_board(solution)
    print("Cost = ", calculate_cost(solution))
    print("Note - simple hill climb does not gaurentee optimal solution")
