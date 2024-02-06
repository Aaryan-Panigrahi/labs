import math
# n = int(input("How many elements?"))

# X = []
# print("Enter elements of X -")
# for i in range(n):
# 	t = int(input("element", i))
# 	X.append(t)


# Y = []
# print("Enter elements of Y -")
# for i in range(n):
# 	t = int(input("element", i))
# 	Y.append(t)

Y = [1, 2, 3, 6]
X = [6, 4, 4, 6]

# Start here
X = [(1, 2), (3, 2), (7, 2), (11, 23)]
Y = [(3, 49), (4, 2), (9, 10), (22, 12)]
n = 4

D = []
for i in range(n):
	d2 = 0
	for j in range(2):
		t = X[i][j] - Y[i][j]
		d2 = d2 + t*t
	d = round(math.sqrt(d2), 2)
	D.append(d)



print(D)

#Bubble Sort
for i in range(n):
	for j in range(n-i-1):
		if(D[j] > D[j+1]):
			t = D[j]
			D[j] = D[j+1]
			D[j+1] = t
print(D)






