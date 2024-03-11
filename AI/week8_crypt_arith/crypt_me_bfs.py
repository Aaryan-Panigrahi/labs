from collections import deque

def get_val(word, dic):
    return sum(dic[ch] * (10 ** i) for i, ch in enumerate(word[::-1]))

def is_correct(dic, w1, w2, wr):
    # No two letters mapped to the same number, and all in range [0, 9]
    mapped = set()
    for v in dic.values():
        if v in mapped or v not in range(10):
            return False
        mapped.add(v)

    # No word begins with 0
    if dic[w1[0]] == 0 or dic[w2[0]] == 0 or dic[wr[0]] == 0:
        return False

    # w1 + w2 = wr
    return get_val(w1, dic) + get_val(w2, dic) == get_val(wr, dic)

def solve_crypt(w1, w2, wr, dic):
    queue = []
    visited = []

    queue.append(dic)

    while queue:
        current = queue.pop(0)

        if is_correct(current, w1, w2, wr):
            dic = list(current)
            return True

        for i in range(len(w1)):
            

    return False

if __name__ == "__main__":
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")
    wr = input("Enter result word: ")

    # Initialize Dictionary
    dic = {}
    for ch in w1 + w2 + wr:
        if ch not in dic.keys():
            dic[ch] = None

    # Solve the puzzle
    if solve_crypt(w1, w2, wr, dic):
        print("Cryptarithmetic puzzle solved successfully!")
        # Result
        for k, v in dic.items():
            print(k, v)
    else:
        print("No solution found for the given puzzle.")
