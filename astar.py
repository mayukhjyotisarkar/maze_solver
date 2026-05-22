import heapq


def heuristic(a, b):

    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(position, maze):

    row, col = position

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if (
            0 <= new_row < len(maze)
            and
            0 <= new_col < len(maze[0])
            and
            maze[new_row][new_col] != "#"
        ):

            neighbors.append((new_row, new_col))

    return neighbors


def reconstruct_path(came_from, current, start):

    path = []

    while current in came_from:

        path.append(current)
        current = came_from[current]

    path.append(start)

    path.reverse()

    return path


def astar(maze, start, goal):

    open_list = []

    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {
        start: 0
    }

    visited = set()

    while open_list:

        current_f, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:

            path = reconstruct_path(
                came_from,
                current,
                start
            )

            return path

        neighbors = get_neighbors(current, maze)

        for neighbor in neighbors:

            tentative_g = g_cost[current] + 1

            if (
                neighbor not in g_cost
                or
                tentative_g < g_cost[neighbor]
            ):

                came_from[neighbor] = current

                g_cost[neighbor] = tentative_g

                f_cost = (
                    tentative_g
                    + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_list,
                    (f_cost, neighbor)
                )

    return None