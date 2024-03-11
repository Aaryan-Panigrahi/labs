def get_val(w1):
    return sum( dic[w1[i]] * (10 ** i) for i in range(len(w1)) )

def is_correct(dic, w1, w2, wr):
    #No two letters mapped to the same number, and all = (0, 9)
    mapped = set()
    for v in dic.values():
        if v in mapped:
            return False
        if v not in range(10):
            return False
        mapped.add(v)

    #No word begins with 0
    if(dic[w1[0]] == 0 or dic[w2[0]] == 0 or dic[wr[0]] == 0):
        return False

    #w1 + w2 = wr
    if get_val(w1) + get_val(w2) != get_val(wr):
        return False

    return True

def solve_crypt(w1, w2, wr, dic, used, index=0):
    if index == len(dic):
        return is_correct(dic, w1, w2, wr)

    letters = list(dic.keys())
    for num in range(10):
        if num not in used:
            dic[letters[index]] = num
            used.add(num)
            if solve_crypt(w1, w2, wr, dic, used, index + 1):
                return True
            used.remove(num)
            dic[letters[index]] = None
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
