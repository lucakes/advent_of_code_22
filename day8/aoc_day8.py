import pathlib
import sys


def get_x_before(tree_matrix, x, y):
    x_before_list = tree_matrix[:x]
    result = []
    for x in x_before_list:
        result.append(x[y])
    return result


def get_x_behind(tree_matrix, x, y):
    x_before_list = tree_matrix[x+1:]
    result = []
    for x in x_before_list:
        result.append(x[y])
    return result


def get_visible_trees(input):
    lines = input.split("\n")
    tree_matrix = []
    for line in lines:
        tree_matrix.append(list(line))
    visible = []
    for x in range(0, len(tree_matrix[0]), 1):
        for y in range(0, len(tree_matrix), 1):
            if x == 0 or x == len(tree_matrix)-1 or y == 0 or y == len(tree_matrix)-1:
                visible.append(tree_matrix[x][y])
            else:
                size = tree_matrix[x][y]
                max_up = max(get_x_before(tree_matrix, x, y))
                max_down = max(get_x_behind(tree_matrix, x, y))
                max_left = max(tree_matrix[x][:y])
                max_right = max(tree_matrix[x][y+1:])
                if size > max_up or size > max_down or size > max_left or size > max_right:
                    visible.append(tree_matrix[x][y])
    return visible


def get_scenic_up(param, size):
    scenic = 0
    for i in param:
        if i < size:
            scenic += 1
        if i >= size:
            scenic += 1
            break
    return scenic


def get_scenic_reverse(param, size):
    scenic = 0
    param.reverse()
    for i in param:
        if i < size:
            scenic += 1
        if i >= size:
            scenic += 1
            break
    return scenic


def get_scenic_scores(input):
    lines = input.split("\n")
    tree_matrix = []
    for line in lines:
        tree_matrix.append(list(line))
    scenic_scores = []
    for x in range(0, len(tree_matrix[0]), 1):
        for y in range(0, len(tree_matrix), 1):
            if x == 0 or x == len(tree_matrix)-1 or y == 0 or y == len(tree_matrix)-1:
                continue
            else:
                size = tree_matrix[x][y]
                scenic_up = get_scenic_reverse(get_x_before(tree_matrix, x, y), size)
                scenic_down = get_scenic_up(get_x_behind(tree_matrix, x, y), size)
                scenic_left = get_scenic_reverse(tree_matrix[x][:y], size)
                scenic_right = get_scenic_up(tree_matrix[x][y+1:], size)
                scenic_scores.append(scenic_up * scenic_down * scenic_left * scenic_right)
    return scenic_scores


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_visible_trees(input)
        solution_part_two = get_scenic_scores(input)
        print("solution part one: " + str(len(solution_part_one)) + " solution part two: " + str(max(solution_part_two)))
