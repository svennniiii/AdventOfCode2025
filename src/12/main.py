input_file = "src/12/input.txt"

sizes = {
    0: 7, 
    1: 7,
    2: 5,
    3: 7,
    4: 6,
    5: 7,
}

possible_fits = 0
with open(input_file, "r") as file:
    for line in file:
        if "x" not in line:
            continue

        size_str, counts_str = line.strip().split(":")

        width, height = map(int, size_str.split("x"))
        presents = list(map(int, counts_str.strip().split(" ")))

        # available_space = width * height
        # needed_space = sum(sizes[i]*presents[i] for i in range(6))
        # total_space_check = available_space >= needed_space
        
        three_by_three_check = (width // 3) * (height // 3) >= sum(presents)

        if three_by_three_check:
            possible_fits += 1

print(f"Part 1: {possible_fits}")
