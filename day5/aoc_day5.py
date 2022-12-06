import pathlib
import sys


class MoveCommand:
    def __init__(self, quantity, begin, target):
        self._quantity = quantity
        self._begin = begin
        self._target = target

    def get__quantity(self):
        return self._quantity

    def get__begin(self):
        return self._begin

    def get__target(self):
        return self._target


def clean_commands(commands_rare):
    commands = []
    for command_rare in commands_rare:
        split_command = command_rare.split(" ")

        quantity_container = split_command[1]
        begin_stack = split_command[3]
        target_stack = split_command[5]
        command = MoveCommand(quantity_container, begin_stack, target_stack)
        commands.append(command)
    return commands


def move(clear_command, stackdict):
    for i in range(0, int(clear_command.get__quantity()), 1):
        var = stackdict[int(clear_command.get__begin())]
        removed_item = var[0]
        var.remove(removed_item)
        target_stack = stackdict[int(clear_command.get__target())]
        target_stack.insert(0, removed_item)


def move_other_crane(clear_command, stackdict):
    list_moved_container = []
    for i in range(0, int(clear_command.get__quantity()), 1):
        var = stackdict[int(clear_command.get__begin())]
        removed_item = var[0]
        var.remove(removed_item)
        list_moved_container.append(removed_item)
    list_moved_container.reverse()
    for moved_container in list_moved_container:
        target_stack = stackdict[int(clear_command.get__target())]
        target_stack.insert(0, moved_container)
    pass


def get_top_chars(stackdict):
    count_stacks = len(stackdict)
    top_chars = []
    for i in range(1, count_stacks + 1, 1):
        top_chars.append(stackdict[i][0])
    return top_chars


def process_initial_state(stacks_rare, character_digits_to_split):
    stacks_containers = dict()
    for stack_rare in stacks_rare:
        for character_digit in character_digits_to_split:
            if character_digit <= len(stack_rare):
                character = list(stack_rare)[character_digit]
                stack = character_digits_to_split.index(character_digit) + 1
                if character.strip():
                    stacks_containers.setdefault(stack, []).append(character)
    return stacks_containers


def get_top_of_stacks(input):
    lines = input.split("\n")
    index_begin_commands = lines.index('')
    stack_count = max(lines[index_begin_commands - 1].split(" "))
    stacks_rare = lines[:index_begin_commands - 1]
    commands_rare = lines[index_begin_commands + 1:]

    character_digits_to_split = []
    for n in range(1, 4 * int(stack_count), 4):
        character_digits_to_split.append(n)

    stacks_containers = process_initial_state(stacks_rare, character_digits_to_split)

    clear_commands = clean_commands(commands_rare)

    for clear_command in clear_commands:
        move(clear_command, stacks_containers)

    return ''.join(get_top_chars(stacks_containers))


def get_top_of_stacks_different_crane(input):
    lines = input.split("\n")
    beginn_commands = lines.index('')
    stack_count = max(lines[beginn_commands - 1].split(" "))
    stacks_rare = lines[:beginn_commands - 1]
    commands_rare = lines[beginn_commands + 1:]

    character_digits_to_split = []
    for n in range(1, 4 * int(stack_count), 4):
        character_digits_to_split.append(n)

    stacks_containers = process_initial_state(stacks_rare, character_digits_to_split)

    clear_commands = clean_commands(commands_rare)

    for clear_command in clear_commands:
        move_other_crane(clear_command, stacks_containers)

    return ''.join(get_top_chars(stacks_containers))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_top_of_stacks(input)
        solution_part_two = get_top_of_stacks_different_crane(input)
        print("solution part one: " + str(solution_part_one) + " solution part two: " + str(solution_part_two))
