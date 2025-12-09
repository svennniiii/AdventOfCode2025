input_file = "src/4/input.txt"

rolls: list[str] = []
with open(input_file, "r") as file:
    for line in file:
        rolls.append(line.strip())

directions = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    ( 0, -1),
]

rows = len(rolls)
columns = len(rolls[0])
accessible_rolls = 0

for i in range(rows):
    for j in range(columns):
        if rolls[i][j] == ".":
            continue

        neighbours = 0
        for di, dj in directions:
            n_i = i + di
            n_j = j + dj
            if n_i < 0 or rows <= n_i:
                continue
            if n_j < 0 or columns <= n_j:
                continue
            
            if rolls[n_i][n_j] == ".":
                continue

            neighbours += 1
        if neighbours < 4:
            accessible_rolls += 1
               
print(f"Part 1: {accessible_rolls}")


def remove_rolls(rolls: list[str]) -> int:
    remaining_rolls: list[str] = []
    rolls_removed = 0

    for i in range(rows):
        current_row: list[str] = []
        for j in range(columns):
            if rolls[i][j] == ".":
                current_row.append(".")
                continue

            neighbours = 0
            for di, dj in directions:
                n_i = i + di
                n_j = j + dj
                if n_i < 0 or rows <= n_i:
                    continue
                if n_j < 0 or columns <= n_j:
                    continue
                
                if rolls[n_i][n_j] == ".":
                    continue

                neighbours += 1
            if neighbours < 4:
                current_row.append(".")
                rolls_removed += 1
            else:
                current_row.append("@")
        remaining_rolls.append("".join(current_row))

    if rolls_removed == 0:
        return 0

    return rolls_removed + remove_rolls(remaining_rolls)

rolls_removed = remove_rolls(rolls)

print(f"Part 2 {rolls_removed}")