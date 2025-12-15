from functools import cache
import time

start = time.time()

input_file = "src/11/input.txt"

connections: dict[str, tuple[str, ...]] = {}

with open(input_file, "r") as file:
    for line in file:
        device, *outputs = line.strip().split(" ")
        connections[device[:-1]] = tuple(outputs)

@cache
def number_of_paths(start: str, previous: tuple[str, ...]) -> int:
    if start == "out":
        return 1
    
    n = 0
    for device in  connections[start]:
        if device in previous:
            continue

        n += number_of_paths(device, (previous + (device,)))

    return n

if not "example_2" in input_file:
    print(f"Part 1: {number_of_paths("you", tuple())}")

devices = set(connections.keys())
reachable_devices: dict[str, set[str]] = {}

for device in devices:
    devices_to_check = set([device])
    reachable = set()

    while(devices_to_check):
        device_i = devices_to_check.pop()
        if device_i == "out":
            continue

        for device_j in connections[device_i]:
            if device_j in reachable:
                continue

            reachable.add(device_j)
            devices_to_check.add(device_j)

    reachable_devices[device] = reachable

@cache
def number_of_paths_2(start: str, fft: bool, dac: bool) -> int:
    if (not fft) and ("fft" not in reachable_devices[start]):
        return 0
    elif (not dac) and ("dac" not in reachable_devices[start]):
        return 0
    elif start == "out":
        if fft and dac:
            return 1
        else:
            return 0
    elif "out" not in reachable_devices[start]:
        return 0

    n = 0
    for device in connections[start]:
        fft_i = True if device == "fft" else fft
        dac_i = True if device == "dac" else dac
        n += number_of_paths_2(device, fft=fft_i, dac=dac_i)

    return n

print(f"Part 2: {number_of_paths_2("svr", False, False)}")
print(f"Total time: {int((time.time() - start) * 1000)} ms")