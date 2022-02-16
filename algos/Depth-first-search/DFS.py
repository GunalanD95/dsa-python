# Depth-First Search Pseudocode

# Stack: [start_pos]
# Predecessors: {start_pos: None}


# Alogrithm:
# 1. Pop the stack [removeing the last element or top of the stack]
# 2. Check if the popped element is the goal , if yes we are done
# 3. If not, push the popped element's neighbors to the stack and add them to predecessors dictionary
# 4. Repeat step 1 to 3 until the stack is empty


stack = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I']

length = len(stack)

find = 'A'

print(stack.index(find))

for i in range(length):
    start_pos = stack.pop()
    if start_pos == find:
        print(f'Found {find}')
        break