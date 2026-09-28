import math
import heapq

# 0 = jalan, 1 = obstacle/dinding
DUNGEON = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

ENEMY = (0, 0)
PLAYER = (6, 6)
DETECTION_RANGE = 10


# Menghitung jarak Euclidean
def calculate_distance(start, goal):
    x1, y1 = start
    x2, y2 = goal

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Heuristic untuk algoritma A*
def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal

    return abs(x1 - x2) + abs(y1 - y2)


# Mendapatkan tetangga yang bisa dilewati
def get_neighbors(node):
    x, y = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        if (
            0 <= new_x < len(DUNGEON)
            and 0 <= new_y < len(DUNGEON[0])
            and DUNGEON[new_x][new_y] == 0
        ):
            neighbors.append((new_x, new_y))

    return neighbors


# Algoritma A*
def a_star(start, goal):
    open_list = []

    # (nilai f, posisi)
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current != start:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        for neighbor in get_neighbors(current):
            new_cost = cost_so_far[current] + 1

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost

                priority = new_cost + heuristic(neighbor, goal)

                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None


# Program utama
print("=== DUNGEON ENEMY PATHFINDING ===")

print("Posisi Enemy :", ENEMY)
print("Posisi Player:", PLAYER)

distance = calculate_distance(ENEMY, PLAYER)

print("Jarak Enemy ke Player:", round(distance, 2))
print("Detection Range:", DETECTION_RANGE)

# Mengecek apakah Player berada dalam jangkauan
if distance <= DETECTION_RANGE:
    print("\nPlayer terdeteksi!")

    # Mencari jalur menggunakan A*
    path = a_star(ENEMY, PLAYER)

    if path:
        print("Jalur ditemukan menggunakan A*:")
        print(path)

        print("\nEnemy bergerak menuju Player:")

        for step in path:
            print("Enemy bergerak ke", step)

        print("\nEnemy berhasil mencapai Player.")
    else:
        print("Jalur menuju Player tidak ditemukan.")

else:
    print("\nPlayer berada di luar jangkauan.")
    print("Enemy tetap melakukan patroli.")
