import pathlib
import sys


class Directory:
    def __init__(self, path, parent, dirs, files):
        self._parent = parent
        self._path = path
        self._dirs = dirs
        self._files = files

    def __init__(self, path, parent):
        self._parent = parent
        self._path = path
        self._dirs = []
        self._files = []

    def __init__(self, path):
        self._path = path
        self._dirs = []
        self._files = []

    def get__parent(self):
        return self._parent

    def get__dirs(self):
        return self._dirs

    def get__files(self):
        return self._files

    def get__path(self):
        return self._path

    def set_parent(self, parent):
        self._parent = parent

    def set_dirs(self, dirs):
        self._dirs = dirs

    def set_files(self, files):
        self._files = files

    def set_path(self, path):
        self._path = path

    def get_all_dirs(self):
        all_dirs = []
        for dir in self._dirs:
            all_dirs.extend(dir.get_all_dirs())
        all_dirs.extend(self._dirs)
        return all_dirs

    def size(self):
        return sum(int(file.get__size()) for file in self._files) + sum(int(dir.size()) for dir in self._dirs)


class File:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get__name(self):
        return self._name

    def get__size(self):
        return self._size

    def set_name(self, name):
        self._name = name

    def set_size(self, size):
        self._size = size


def process_dir_content(output, root):
    if output[0] == "dir":
        new_dir = Directory(output[1])
        new_dir.set_parent(root)
        root.get__dirs().append(new_dir)
    else:
        new_file = File(output[1], output[0])
        root.get__files().append(new_file)
    pass


def find_dir(root, param):
    contents = root.get__dirs()
    for content in contents:
        if type(content) is Directory:
            if content.get__path() == param:
                return content


def find_slash(root):
    if hasattr(root, '_parent'):
        return find_slash(root.get__parent())
    else:
        return root


def get_total_size_directories_above_100000(input):
    terminal_output = input.split("\n")

    root = Directory("/")
    current_dir = root
    parse_terminal_output(current_dir, terminal_output)
    all_dirs = root.get_all_dirs()
    target_dirs = [dir for dir in all_dirs if int(dir.size()) <= 100000]
    return sum(dir.size() for dir in target_dirs)


def parse_terminal_output(current_dir, terminal_output):
    for output in terminal_output:
        output = output.split(" ")
        if output[0] != "$":
            process_dir_content(output, current_dir)
        elif output[1] == "cd":
            if output[2] == "..":
                current_dir = current_dir.get__parent()
            else:
                current_dir = find_dir(current_dir, output[2])
    pass


def free_space(input):
    terminal_output = input.split("\n")

    root = Directory("/")
    current_dir = root
    parse_terminal_output(current_dir, terminal_output)

    all_dirs = root.get_all_dirs()
    unused_space = 70000000 - root.size()
    extra_free = 30000000 - unused_space
    looked_up_dirs = [dir for dir in all_dirs if dir.size() >= extra_free]
    smallest_look_up = min(looked_up_dirs, key=lambda x: x.size())
    return smallest_look_up.size()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_total_size_directories_above_100000(input)
        solution_part_two = free_space(input)
        print("solution part one: " + str(solution_part_one) + " solution part two: " + str(solution_part_two))
