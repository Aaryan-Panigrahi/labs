def simple_hill_climb():
     
    step = 1
    curr_x = 0 
    nexts = []
    while True:

        nexts.extend([curr_x + step, curr_x - step])

        found_better = 0
        for nx in nexts:
            if f(nx) > f(curr_x):
                curr_x = nx
                found_better += 1
        
        if found_better == 0 or curr_x not in range(-10, 11):
            print("Found a maxima at x = ", curr_x, " value = ", f(curr_x))
            return

#Define the function to maximize
def f(x):
    y = -(x*x)+8*x-3
    return y

simple_hill_climb()
