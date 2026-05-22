from maze import maze, find_positions
from astar import astar
from visualize import print_maze, draw_path


def main():

    print("Original Maze:\n")

    print_maze(maze)

    start, goal = find_positions(maze)

    path = astar(maze, start, goal)

    if path:

        print("Shortest Path Found!\n")

        print("Path:")
        print(path)
        print()

        updated_maze = draw_path(maze, path)

        print("Solved Maze:\n")

        print_maze(updated_maze)

    else:

        print("No path found!")


if __name__ == "__main__":
    main()
    