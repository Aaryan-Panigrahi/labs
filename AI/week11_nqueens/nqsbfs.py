def is_valid_state(state):
    # Check if the current state is valid (no queens attack each other)
    current_row = len(state) - 1
    for i in range(current_row):
        diff = abs(state[i] - state[current_row])
        if diff == 0 or diff == current_row - i:  # Same column or diagonal
            return False
    return True

def get_children(state, n):
    # Generate all possible next states from the current state
    if not state:
        return [[i] for i in range(n)]
    children = []
    for i in range(n):
        new_state = state + [i]
        if is_valid_state(new_state):
            children.append(new_state)
    return children

def bfs(n):
    # Perform BFS to find all solutions
    solutions = []
    queue = get_children([], n)  # Initialize queue with possible positions for the first queen
    
    while queue:
        state = queue.pop(0)  # Dequeue the first state
        if len(state) == n:
            solutions.append(state)  # Found a solution
        else:
            children = get_children(state, n)
            queue.extend(children)  # Enqueue possible states
    
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(' '.join('Q' if col == row else '.' for col in range(len(solution))))
        print("")

n = 8  # Size of the chessboard (n x n)
solutions = bfs(n)
for solution in solutions:
    print("solution:", solution)
print(f"Found {len(solutions)} solutions.")

