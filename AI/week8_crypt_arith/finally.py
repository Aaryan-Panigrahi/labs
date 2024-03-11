def get_val(dic, w):
    return sum(dic[w[i]] * (10 ** (len(w) - i - 1)) for i in range(len(w)))

def is_correct(dic, w1, w2, wr):
    mapped = set()
    for v in dic.values():
        if v in mapped or v not in range(10):
            return False
        mapped.add(v)

    if dic[w1[0]] == 0 or dic[w2[0]] == 0 or dic[wr[0]] == 0:
        return False

    if get_val(dic, w1) + get_val(dic, w2) != get_val(dic, wr):
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

    dic = {}
    for ch in w1 + w2 + wr:
        if ch not in dic:
            dic[ch] = None

    used = set()
    if solve_crypt(w1, w2, wr, dic, used):
        print("Cryptarithmetic puzzle solved successfully!")
        for k, v in dic.items():
            print(f"{k} = {v}")
    else:
        print("No solution found for the given puzzle.")
