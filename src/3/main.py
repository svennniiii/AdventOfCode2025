input = "src/3/input.txt"

total_joltage = 0
with open(input, "r") as file:
    for line in file:
        line = line.strip()
        first_digit = max(*line[:-1])
        position = line.find(first_digit)
        second_digit = max(*line[position+1:])
        total_joltage += int(first_digit) * 10 + int(second_digit)

print(f"Part 1: {total_joltage}")

def find_max_joltage(bank: str, number_of_batteries: int):
    if number_of_batteries == 1:
        return  int(max(*bank))
    
    first_digit = max(*bank[:-(number_of_batteries - 1)])
    position = bank.find(first_digit)

    other_batteries = find_max_joltage(bank[position+1:], number_of_batteries - 1)
    return int(first_digit) * 10 ** (number_of_batteries - 1) + other_batteries

number_of_batteries = 12
total_joltage = 0
with open(input, "r") as file:
    for line in file:
        total_joltage += find_max_joltage(line.strip(), number_of_batteries)

print(f"Part 2: {total_joltage}")
