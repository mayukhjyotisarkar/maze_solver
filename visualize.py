def print_maze(maze):

    for row in maze:
        print(" ".join(row))

    print()


def draw_path(maze, path):

    for row, col in path:

        if maze[row][col] not in ["S", "G"]:
            maze[row][col] = "*"

    return maze