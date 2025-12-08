from functools import cache

FILEPATH = "src/2/part1.txt"

with open(FILEPATH, "r") as file:
    raw_input = list(map(lambda x: x.split("-"), file.readline().split(",")))

result_1 = 0
for min_id, max_id in raw_input:
    for i in range(int(min_id), int(max_id) + 1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len % 2:
            continue
 
        if i_str[:i_len // 2] == i_str[i_len // 2:]:
            result_1 += i

print(f"Part 1: {result_1}")

@cache
def get_sub_string_indices(string_length: int):
    result = []
    for i in range(1, string_length // 2 + 1):
        if string_length % i:
            continue

        result_i = []
        for j in range(string_length // i):
            result_i.append((j*i, j*i+i))    
        result.append(tuple(result_i))

    return tuple(result)

result_2 = 0
for min_id, max_id in raw_input:
    for current_id in range(int(min_id), int(max_id) + 1):
        id_string = str(current_id)
        id_length = len(id_string)
        for sub_string_length in get_sub_string_indices(id_length):
            sub_strings = set()
            for min_index, max_index in sub_string_length:
                sub_strings.add(id_string[min_index:max_index])
            
            if len(sub_strings) == 1:
                # print(current_id)
                result_2 += current_id   
                break     

print(f"Part 2: {result_2}")
