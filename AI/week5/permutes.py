def swap(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    return s.copy()  # Create a copy of the list to avoid modifying the original

def explore_permutations(initial_state):
    visited = set()
    queue = []
    all_permutations = []

    all_permutations.append(initial_state)
    queue.append(initial_state)

    while queue:
        current_state = queue.pop(0)

        # Generate next states by swapping elements
        for i in range(len(current_state)):
            for j in range(i + 1, len(current_state)):
                next_state = swap(current_state, i, j)

                if tuple(next_state) not in visited: 
                    all_permutations.append(next_state)
                    visited.add(tuple(next_state))
                    queue.append(next_state)

    print(len(all_permutations))

# Example usage:
initial_permutation = [1, 2, 3, 4]
explore_permutations(initial_permutation)
