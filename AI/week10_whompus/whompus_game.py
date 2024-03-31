
class Whompus:
	def __init__(self):
		self.state_dic = {
		    0:"Nothing here, but you're alive...",
		    1:"Glitter!",
		    2:"Stench!",
		    3:"Breeeze",
		    5:"Stench and Breeze!",
		    6:"Stench, Breeze and Glitter!",
		    7:"You got eaten by the WhomPus :()",
		    9:"You fell into a pit! :[]"
		}

		self.world = [
		    [2, 0, 3, 9],
		    [7, 6, 9, 3],
		    [2, 0, 3, 0],
		    [0, 3, 9, 3]
		]

		self.agent_pos = [3, 0]

		self.has_gold = False

		self.end_game = False

	def get_state_no(self):
		return self.world[self.agent_pos[0]][self.agent_pos[1]]

	def print_state(self):
		print(self.state_dic[self.get_state_no()])

	def state_step(self):
		n = self.get_state_no()
		self.print_state()
		if n in [7, 9]:
			print("Game Over. Better luck next time!")
			self.end_game = True

		if n == 6:
			print("You found the Gold!")
			has_gold = True

		if self.agent_pos is [3, 0] and has_gold == True:
			print("** Congrats! ** You Won! OoO **")
			self.end_game = True

	def move(self, move):
		X, Y = self.agent_pos
		if move == 'w':
			X -= 1
		elif move == 's':
			X += 1
		elif move == 'a':
			Y -= 1
		elif move == 'd':
			Y += 1
		else:
			print("Invalid move")
			return
		for i in [X, Y]:
			if i not in range(4):
				print("You'd go out of range!")
				return 

		#Execute Validated move ~    	
		self.agent_pos = [X, Y]
		self.state_step()
    	

    











