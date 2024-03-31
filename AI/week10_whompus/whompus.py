'''
1. Glitter
2. Stench
3. Breeze

5 = Stench + Breeze
6 = Stench + Breeze + Glitter

7 = Whompus
8 = Agent
9 = Pit
'''

state_dic = {
    0:"Nothing here, but you're alive...",
    1:"Glitter!",
    2:"Stench!",
    3:"Breeeze",
    5:"Stench and Breeze!",
    6:"Stench, Breeze and Glitter!",
    7:"You got eaten by the WhomPus :(",
    9:"You fell into a pit"
}

world = [
    [2, 0, 3, 9],
    [7, 6, 9, 3],
    [2, 0, 3, 0],
    [0, 3, 9, 3]
]

agent = [3, 0]
gold = False

def get_msg(agent):
    n = world[agent[0]][agent[1]]
    print(dic[n])
    if n == 6:
        print("Press 'G' to grab Gold")

# moves = w, a, s, d

def move(agent, move):
    init = list(agent)
    if move == 'w':
        agent[0] -= 1
    else if move == 's':
        agent[0] += 1
    else if move == 'a':
        agent[1] -= 1
    else if move == 'd':
        agent[1] += 1
    else:
        print("Invalid move")
        return init

    for i in agent:
        if i not in range(4):
            print("You'd go out of range!")
            return init

    print("Move Accomplished")
    get_msg(agent)
    return agent

while True:

