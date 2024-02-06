
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def push(self, item, path, cost):
        self.queue.append((item, path, cost))
    
    def pop(self):
        min_cost = float('inf')
        min_item = None
        for i in range(len(self.queue)):
            if self.queue[i][2] < min_cost:
                min_cost = self.queue[i][2]
                min_item = i
        return self.queue.pop(min_item)
    
    def print_queue(self):
        for item, cost in self.queue:
            print(item, cost)
        print()