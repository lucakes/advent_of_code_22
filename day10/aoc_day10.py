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
    while cycle <= max_cycle + 1:
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


def draw(cycle, register):
    sprite_pos = (cycle - 1) % 40

    if register in range(sprite_pos - 1, sprite_pos + 2):
        if cycle % 40 == 0:
            return "#\n"
        return '#'

    else:
        if cycle % 40 == 0:
            return ".\n"
        return '.'


def paint_output(input):
    lines = input.split("\n")
    register = 1
    cycle = 1
    line = ""
    while len(lines) > 0:
        command = lines.pop(0).split(" ")
        if command[0] != "noop":
            cycle += 1
            line = line + draw(cycle, register)
            register += int(command[1])
            cycle += 1
            line = line + draw(cycle, register)
        else:
            cycle += 1
            line = line + draw(cycle, register)
    print(line)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_signal_strength(input, [20, 60, 100, 140, 180, 220])
        print("solution part one " + str(sum(solution_part_one)))
        print("solution part two")
        paint_output(input)
