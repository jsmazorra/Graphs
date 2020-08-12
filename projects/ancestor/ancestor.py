# from util import Stack
from util import Queue
# Decided to go with the breadth-first search approach since the functionality of it is faster for this search tree of ancestors.

def earliest_ancestor(ancestors, starting_node):
    cache = {}
    for i in ancestors:
        parent = i[0]
        child = i[1]
        if child not in cache:
            cache[child] = []
        cache[child].append(parent)
    
    queue = Queue()
    # stack = Stack()
    queue.enqueue([starting_node])
    # stack.push([starting_node])
    length = [1, -1]
    while len(queue) > 0:
    # while len(stack) > 0:
        current = queue.dequeue()
        # current = stack.pop()
        last = current[-1]
        if last not in cache:
            if len(current) > length[0]:
                length = [len(current), last]
            
            if len(current) == length[0] and last < length[1]:
                length = [len(current), last]
 
        else:
            for i in cache[last]:
                queue.enqueue(current + [i])
                # stack.push(current + [i])
    
    # For testing purposes.
    print("OUTPUT:", length[1]) 
    return length[1]
