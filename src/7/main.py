from functools import cache

input_file = "src/7/input.txt"

total_splits = 0
with open(input_file, "r") as file:
    line = file.readline().strip()
    beams = {line.find("S")}

    for line in file:
        old_beams = beams.copy()
        beams.clear()
        for beam in old_beams:
            if line[beam] == ".":
                beams.add(beam)
            elif line[beam] == "^":
                beams.add(beam - 1)
                beams.add(beam + 1)
                total_splits += 1

print(f"Part 1: {total_splits}")

manifold: list[str] = []
total_timelines = 0

with open(input_file, "r") as file:
    line = file.readline().strip()
    beam = line.find("S")
    manifold = [line.strip() for line in file]

@cache
def count_timelines(beam: int, manifold: tuple[str]):
    if not manifold:
        return 1
    
    if manifold[0][beam] == ".":
        return count_timelines(beam, manifold[1:])
    else:
        return count_timelines(beam - 1, manifold[1:]) + count_timelines(beam + 1, manifold[1:])

total_timelines = count_timelines(beam, tuple(manifold))

print(f"Part 2: {total_timelines}")