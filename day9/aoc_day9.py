import pathlib
import sys


def check_two_knots(follower, leader):
    if leader == follower:
        return follower

    if abs(leader["x"] - follower["x"]) <= 1 and abs(leader["y"] - follower["y"]) <= 1:
        return follower

    if follower["x"] == leader["x"]:
        if follower["y"] > leader["y"]:
            follower["y"] -= 1
        else:
            follower["y"] += 1
        return follower
    elif follower["y"] == leader["y"]:
        if follower["x"] > leader["x"]:
            follower["x"] -= 1
        else:
            follower["x"] += 1
        return follower

    if follower["x"] > leader["x"] and follower["y"] > leader["y"]:
        follower["x"] -= 1
        follower["y"] -= 1
    elif follower["x"] > leader["x"] and follower["y"] < leader["y"]:
        follower["x"] -= 1
        follower["y"] += 1
    elif follower["x"] < leader["x"] and follower["y"] > leader["y"]:
        follower["x"] += 1
        follower["y"] -= 1
    elif follower["x"] < leader["x"] and follower["y"] < leader["y"]:
        follower["x"] += 1
        follower["y"] += 1
    return follower


def get_visited(input, list_knots):
    lines = input.split("\n")
    visited = []
    head = list_knots[0]
    tail = list_knots[len(list_knots)-1]
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        for i in range(distance):
            if direction == "U":
                head["y"] += 1
            elif direction == "D":
                head["y"] -= 1
            elif direction == "L":
                head["x"] -= 1
            elif direction == "R":
                head["x"] += 1
            for i in range(0, len(list_knots)-1, 1):
                check_two_knots(list_knots[i+1], list_knots[i])
                if (tail["x"], tail["y"]) not in visited:
                    visited.append((tail["x"], tail["y"]))
    return visited


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_visited(input, [{"x": 0, "y": 0}, {"x": 0, "y": 0}])
        solution_part_two = get_visited(input, [{"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}])
        print(
            "solution part one: " + str(len(solution_part_one)) + " solution part two: " + str(len(solution_part_two)))
