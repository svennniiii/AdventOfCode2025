INPUT = "src/1/part1.txt"

TOTAL = 100
INITIAL_VALUE = 50

value = INITIAL_VALUE
number_zeros = 0
number_zero_clicks = 0

with open(INPUT, "r") as file:
    for direction, *rotations in file:
        rot = int("".join(rotations[:-1]))

        number_zero_clicks += abs(rot) // TOTAL
        
        rot %= TOTAL

        if direction == "L":
            rot *= -1

        old_value = value
        value += rot

        if (old_value != 0) and ((value <= 0) or (TOTAL <= value)):
            number_zero_clicks += 1

        value %= TOTAL

        if value == 0:
            number_zeros += 1

print(f"Part 1: {number_zeros}")
print(f"Part 2: {number_zero_clicks}")
