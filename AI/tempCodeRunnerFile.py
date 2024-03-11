N = 8

b = [[0 for i in range(N)]for j in range(N)]

def isSafe(b, r, c):
	'''
	If you are going to be placing the queens in a systematic manner...
	Say row by row - 
		You don't have to check the row...
		And you only have to check upper diagonals
	'''
	for col in range(c):
		if b[r][col] == 1 :
			return False

	# for row in range(r):
	# 	if b[row][c] == 1 :
	# 		return False 

	#Upper left diag
	for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
		if b[i][j] == 1:
			return False

	#Upper right diag
	for i, j in zip(range(r, -1, -1), range(c+1, N)):
		if b[i][j] == 1:
			return False

	return True

def SolveCol(b, col):
	if(col>=N):
		return True

	for r in range(N):
		if(isSafe(b, r, col)):
			b[r][col] = 1
			if (SolveCol(b, col+1)):
				return True

			b[r][col] = 0

	return False



SolveCol(b, 0)
for i in range(N):
	for j in range(N):
		print(b[i][j], end = '\t')
	print("\n")

# r = 7
# c = 3
# for i, j in zip(range(r, -1, -1), range(c, N)):
# 	print(i, j, b[i][j])