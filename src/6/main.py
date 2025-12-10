input_file = "src/6/input.txt"

problems: list[list[str]] = []
with open(input_file, "r") as file:
    for line in file:
        line = line.strip().split(" ")
        line = list(filter(("").__ne__, line))
        problems.append(line)

result = 0

for i in range(len(problems[0])):
    if problems[-1][i] == "*":
        result_i = 1
        for j in range(len(problems) - 1):
            result_i *= int(problems[j][i])
    elif problems[-1][i] == "+":
        result_i = 0
        for j in range(len(problems) - 1):
            result_i += int(problems[j][i])
    result += result_i
        
print(f"Part 1: {result}")

problems_2: list[str] = []
with open(input_file, "r") as file:
    for line in file:
        problems_2.append(line[:-1])

result = 0
index = 0
while index != len(problems_2[0]) + 1:
    next_sum = problems_2[-1].find("+", index + 1)
    next_pro = problems_2[-1].find("*", index + 1)

    if next_sum == -1 and next_pro == -1:
        next_index = len(problems_2[0]) + 1
    elif next_sum == -1:
        next_index = next_pro
    elif next_pro == -1:
        next_index = next_sum
    else:
        next_index = min(next_sum, next_pro)

    numbers: list[int] = []
    for i in range(next_index - index - 1):
        number = ""
        for j in range(len(problems_2) - 1):
            number += problems_2[j][index + i]
        numbers.append(int(number))
    
    if problems_2[-1][index] == "*":
        result_i = 1
        for number in numbers:
            result_i *= number
    elif problems_2[-1][index] == "+":
        result_i = 0
        for number in numbers:
            result_i += number

    result += result_i
    index = next_index

print(f"Part 2 {result}")