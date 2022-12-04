import pathlib
import sys


def find_maximum_calories(input):
    list_of_addedup_calories = get_list_addedup_calories(input)
    max_calories = max(list_of_addedup_calories)
    return max_calories


def sum_top3_calories_per_elf(input):
    list_of_addedup_calories = get_list_addedup_calories(input)
    list_of_addedup_calories.sort()
    sum_top3_calories = 0
    for i in range(3):
        sum_top3_calories = sum_top3_calories + int(list_of_addedup_calories.pop())
    return sum_top3_calories


def get_list_addedup_calories(input):
    list_of_addedup_calories = []
    calories_per_elf_list = input.split("\n\n")
    for calories_of_elf in calories_per_elf_list:
        calories_list = calories_of_elf.split("\n")
        sum_calories = 0
        for calorie in calories_list:
            sum_calories = sum_calories + int(calorie)
        list_of_addedup_calories.append(sum_calories)
    return list_of_addedup_calories


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text().strip()
        maximum_calories = find_maximum_calories(input)
        sum_top3_calories = sum_top3_calories_per_elf(input)
        print("max_calories: "+str(maximum_calories)+" sum_top3: "+str(sum_top3_calories))
