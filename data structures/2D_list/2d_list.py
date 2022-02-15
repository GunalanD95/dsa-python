

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


if __name__ == "__main__":
    maze = read_maze("data structures/2D_list/mazes.txt")
    for j in maze:
        print(j)
