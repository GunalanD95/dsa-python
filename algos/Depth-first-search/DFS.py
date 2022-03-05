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



offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

def read_maze(filename):
    """
    Reads a maze from a file and returns a 2D list of its contents.
    """
    try:
        with open(filename) as f:
            mase = [[char for char in line.strip("\n")] for line in f]
            
            top_col = len(mase[0])
            for row in mase:
                if len(row) != top_col:
                    raise ValueError("Maze is not rectangular.")
            return mase
    except OSError:
        print("File not found.")
        raise SystemExit


def is_legal_pos(maze,pos):
    i,j = pos
    num_row = len(maze)
    num_col = len(maze[0])
    return 0 <= i < num_row and 0 <= j < num_col and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


