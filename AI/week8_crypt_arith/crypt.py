def n(ch):
	return ord(ch) - ord('A')

def solver(words, result, map):
	used = [0]*10
	Hash = [0]*26
	chrfront = [0]*26
	uniq = ""

	for wi in range(len(words)):
		for i in range(len(words[wi])):
			ch = words[wi][i]
			Hash[n(ch)] += pow(10, len(words[wi]) - i - 1)

			if map[n(ch)] == -1:
				map[n(ch)] = 0
				uniq += str(ch)

			if i==0 and len(words[wi])>1:
				charfront[n(ch)] = 1

	for i in range(len(result)):
		ch = result[i]
		Hash[n(ch)] -=pow(10, len(result) - i -1)

		if map[n(ch)] == -1:
			map[n(ch)] = 0
			uniq += str(ch)

		if i==0 and len(result)>1:
			charfront[n(ch)] = 1

	map

	pass

if __name__ == "__main__":
	map = [-1]*26

	print(ord('A'))

