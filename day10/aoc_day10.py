import pathlib
import sys


def execute_command(command) -> int:
    if len(command) > 0:
        next_command = command.pop()
        if next_command[0] != "noop":
            value = int(next_command[1])
            return value
        else:
            return 0
    else:
        return 0


def get_signal_strength(input, cycles):
    lines = input.split("\n")
    register = 1
    strengths = []
    max_cycle = max(cycles)
    cycle = 1
    while cycle <= max_cycle+1:
        if len(lines) > 0:
            command = lines.pop(0).split(" ")
            if command[0] != "noop":
                cycle += 1
                if cycle in cycles:
                    strengths.append(cycle * register)
                register += int(command[1])
                cycle += 1
                if cycle in cycles:
                    strengths.append(cycle * register)
            else:
                cycle += 1
                if cycle in cycles:
                    strengths.append(cycle * register)
    return strengths


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_signal_strength(input, [20, 60, 100, 140, 180, 220])
        solution_part_two = get_signal_strength(input, [20, 60, 100, 140, 180, 220])
        print(
            "solution part one: " + sum(solution_part_one) + " solution part two: " + sum(solution_part_one))
