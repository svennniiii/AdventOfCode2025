input_file = "src/5/input.txt"

ranges: list[tuple[int, int]] = []

fresh_ids = 0
with open(input_file, "r") as file:
    for line in file:
        if line == "\n":
            break
            
        ranges.append(tuple(map(int, line.strip().split("-"))))  # type: ignore

    for line in file:
        id = int(line)

        for min_id, max_id in ranges:
            if min_id <= id <= max_id:
                fresh_ids += 1
                break

print(f"Part 1: {fresh_ids}")

ranges.sort()
merged_ranges = []

for current_start, current_end in ranges:
    if not merged_ranges:
        merged_ranges.append((current_start, current_end))
    else:
        last_start, last_end = merged_ranges[-1]

        if current_start <= last_end + 1: 
            new_end = max(last_end, current_end)
            merged_ranges[-1] = (last_start, new_end)
        else:
            merged_ranges.append((current_start, current_end))

fresh_ids = 0
for start, end in merged_ranges:
    fresh_ids += end - start + 1

print(f"Part 2: {fresh_ids}")