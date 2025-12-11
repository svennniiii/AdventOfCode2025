import time
input_file = "src/9/input.txt"

tiles: list[tuple[int, int]] = []
            
with open(input_file, "r") as file:
    for line in file:
        tiles.append(tuple(map(int, line.strip().split(","))))  # type: ignore

largest_rectangle = 0
for i in range(len(tiles) - 1):
    x1, y1 = tiles[i]
    for j in range(i + 1, len(tiles)):
        x2, y2 = tiles[j]
        size_rectangle = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

        largest_rectangle = max(largest_rectangle, size_rectangle)

print(f"Part 1: {largest_rectangle}")

start = time.time()
x_edges: list[tuple[int, int, int]] = []

for i in range(len(tiles)):
    x1, y1 = tiles[i]
    x2, y2 = tiles[(i + 1) % len(tiles)]

    if x1 == x2:
        continue
    x_edges.append((y1, min(x1, x2), max(x1, x2)))

x_edges.sort(key=lambda y: y[0])
    
largest_rectangle = 0
for i in range(len(tiles) - 1):
    x1, y1 = tiles[i]
    for j in range(i + 1, len(tiles)):
        x2, y2 = tiles[j]

        size_rectangle = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

        if size_rectangle <= largest_rectangle:
            continue

        if x1 == x2: continue # FIXME
        if y1 == y2: continue # FIXME

        y_min, y_max = min(y1, y2) + .5, max(y1, y2) - .5
        x_min, x_max = min(x1, x2) + .5, max(x1, x2) - .5
        valid = True

        outer_edges = 0
        for y_edge, x_edge_1, x_edge_2 in x_edges:
            if not (x_min <= x_edge_2 and x_edge_1 <= x_max):
                continue
            
            if y_min < y_edge < y_max:
                valid = False
                break

            if y_edge < y_min:
                outer_edges += 1

            elif (y_edge > y_min) and (outer_edges % 2 == 0):
                valid = False
                break

        if not valid:
            continue
                
        size_rectangle = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest_rectangle = max(largest_rectangle, size_rectangle)

print(f"Part 2: {largest_rectangle} ({(time.time() - start) * 1000} ms)")

