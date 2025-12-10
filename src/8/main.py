import math
import time

start = time.time()

input_file = "src/8/input.txt"

boxes: list[tuple[int, int, int]] = []
with open(input_file, "r") as file:
    boxes = [tuple(map(int, line.strip().split(","))) for line in file]  # type: ignore

distances: dict[tuple[int, int], float] = dict()

for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        distance = math.sqrt(
            (boxes[i][0] - boxes[j][0])**2
            + (boxes[i][1] - boxes[j][1])**2
            + (boxes[i][2] - boxes[j][2])**2
        )
        distances[(i,j)] = distance

circuits: set[tuple[int, ...]] = set([(box,) for box in range(len(boxes))])

n_closest = 10 if input_file.endswith("example.txt") else 1000

for i, j in sorted(distances.keys(), key=lambda k: distances[k])[:n_closest]:
    
    circuit_i = filter(lambda x: tuple.__contains__(x, i), circuits).__next__()
    circuit_j = filter(lambda x: tuple.__contains__(x, j), circuits).__next__()

    if circuit_i == circuit_j:
        continue

    circuits.remove(circuit_i)
    circuits.remove(circuit_j)

    circuits.add(circuit_i + circuit_j)


lengths = sorted([len(circuit) for circuit in circuits])

size_three_largest = lengths[-3] * lengths[-2] * lengths[-1]

print(f"Part 1: {size_three_largest} ({int((time.time() - start) * 1000)} ms)")

start = time.time()
result = 0
for i, j in sorted(distances.keys(), key=lambda k: distances[k]):
    
    circuit_i = filter(lambda x: tuple.__contains__(x, i), circuits).__next__()
    circuit_j = filter(lambda x: tuple.__contains__(x, j), circuits).__next__()

    if circuit_i == circuit_j:
        continue

    circuits.remove(circuit_i)
    circuits.remove(circuit_j)

    circuits.add(circuit_i + circuit_j)

    if len(circuits) == 1:
        result = boxes[i][0] * boxes[j][0]
        break

print(f"Part 2: {result} ({int((time.time() - start) * 1000)} ms)")