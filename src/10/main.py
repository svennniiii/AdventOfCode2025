from itertools import product
import z3

input_file = "src/10/input.txt"

total_presses = 0
with open(input_file, "r") as file:
    for line in file:
        lights_str, *buttons_str, _ =line.strip().split(" ")

        final_config = 0
        for i, light in enumerate(lights_str[1:-1]):
            if light == "#":
                final_config += 2**i
        
        buttons: set[int] = set()
        for button_str in buttons_str:
            button = 0
            for i in button_str[1:-1].split(","):
                button += 2**int(i)

            buttons.add(button)

        presses = 0
        lights_configs = {0}
        while final_config not in lights_configs:
            presses += 1

            new_lights_configs = set()
            for lights_config, button in product(lights_configs, buttons):
                new_lights_config = lights_config ^ button
                new_lights_configs.add(new_lights_config)
                if new_lights_config == final_config:
                    break
                
            lights_configs = new_lights_configs
        total_presses += presses

print(f"Part 1: {total_presses}")
    
total_presses = 0
with open(input_file, "r") as file:
    for line_number, line in enumerate(file):
        _, *buttons_str, joltages_str =line.strip().split(" ")
    
        final_node: tuple[int, ...] = tuple(
            [int(i) for i in joltages_str[1:-1].split(",")])
        
        buttons: list[tuple[int, ...]] = []
        for button_str in buttons_str:
            buttons.append(tuple(int(i) for i in button_str[1:-1].split(",")))

        n = len(final_node)
        presses = z3.IntVector('x', len(buttons))

        s = z3.Optimize()
        for k in range(len(buttons)):
            s.add([x >= 0 for x in presses])

        A = []
        for button in buttons:
            A.append([1 if i in button else 0 for i in range(n)])

        for i in range(n):
            s.add(z3.Sum(presses[k]*A[k][i] for k in range(len(buttons))) == final_node[i])
        
        s.minimize(z3.Sum(presses))
        s.check()
        total_presses += sum(s.model()[k].as_long() for k in s.model())  # type: ignore

print(f"Part 2: {total_presses}")