
import copy

class Jug:
	def __init__(self, name, capacity):
		self.name = name
		self.cap = capacity
		self.curr = 0

	def fill(self):
		self.curr = self.cap

	def empty(self):
		self.curr = 0

	def air(self):
		return self.cap - self.curr

	def pour_to(self, dest):
		amount_to_pour = min(self.curr, dest.air())  # Determine the amount of water to pour
		self.curr -= amount_to_pour  # Update the remaining water in the source jug
		dest.curr += amount_to_pour

	def copy(self):
		return copy.deepcopy(self)

moves = {
	1:"Fill A",
	2:"Fill B",
	3:"Empty A",
	4:"Empty B",
	5:"Pour from A to B",
	6:"Pour from B to A"
}

# Two jugs are enough if the gcd is divisible by target.
# If multiple jugs are ever given, I'd prolly choose two s.t target will multiple of their gcd.

class State:
	def __init__(self, j1, j2):
		self.j1 = j1
		self.j2 = j2
	def pop(self):
		return self.j1, self.j2
	def print(self):
		print(self.j1.curr, self.j2.curr)
	def __eq__(self, other):
		return isinstance(other, State) and self.j1.curr == other.j1.curr and self.j2.curr == other.j2.curr

def ifdo(m, S):
	'''
	S is the current state
	will not affect your actual j1, j2
	'''
	A = S.j1.copy()
	B = S.j2.copy()

	if(m==1):
		A.fill()
	if(m==2):
		B.fill()
	if(m==3):
		A.empty()
	if(m==4):
		B.empty()
	if(m==5):
		A.pour_to(B)
	if(m==6):
		B.pour_to(A)

	return State(A, B)

def dfs_jugs(j1, j2, target):
	visited = []
	stack = []
	init = State(j1, j2)
	stack.append(init)
	visited.append(init)

	for mno in moves.keys():
		next = ifdo(mno, init)
		if next not in visited:
			search(next, visited, stack, target)

def search(S, visited, stack, target):
	visited.append(S)
	stack.append(S)
	
	# Goal Test
	if(S.j2.curr == target):
		print("Got ", target, " in ", S.j2.name)
		return

	for mno in moves.keys():
		next = ifdo(mno, S)
		if next not in visited:
			search(next, visited, stack)
	stack.pop()                                           


def solve2jugs(j1, j2, target):
	'''
	target must be a multiple of the gcd of capacity of j1 and j2
	j2 > j1

	path - stores move numbers - keys of the moves dict
	explored and queue are lists of State's
	'''
	print("Solving 2 jugs ...\n")
	
	explored = []
	queue = []

	init = State(j1, j2)
	queue.append(([], init))
	explored.append(init)
	
	while queue:
		path, curr = queue.pop()
		# curr.print()

		# print("queue", len(queue))
		# for i in queue:
		# 	i.print()

		# Goal Test
		if(curr.j2.curr == target):
			i = 1
			for m in path:
				print(i, ". ", moves[m])
				i+=1
			print("Final state - ")
			curr.print()
			print("Got ", target, " in ", curr.j2.name)
			return path

		# Neighbours
		for mno in moves.keys():
			np = path.copy()
			np.append(mno)
			next = ifdo(mno, curr)
			if next not in explored:
				explored.append(next)
				if next not in queue:
					queue.append((np, next))
					# print("Enqueuing - ")
					# next.print()

def inputJug():
	name = input("Enter name - ")
	cap = int(input("Enter capacity"))
	return Jug(name, cap)

if __name__ == "__main__":
	j1 = Jug('A', 3)
	j2 = Jug('B', 4)
	target = 2
	# solve2jugs(j1, j2, target)
	dfs_jugs(j1, j2, target)

	print("Enter Your own two jug details - ")
	j1 = inputJug()
	j2 = inputJug()
	target = int(input("Enter target - "))

	solve2jugs(j1, j2, target)

				
