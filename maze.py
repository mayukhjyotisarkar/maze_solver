maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", "G", "."]
]


def find_positions(maze):

    start = None
    goal = None

    for i in range(len(maze)):
        for j in range(len(maze[0])):

            if maze[i][j] == "S":
                start = (i, j)

            elif maze[i][j] == "G":
                goal = (i, j)

    return start, goal