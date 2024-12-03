"""Module containing boilerplate code to be used for each day of advent."""

import copy

DATA_FILEPATH = "./2024/day2/"

# =============================Helper Functions START==========================


def read_data_file(filename):
    """Reads the data file and returns a list of strings for each line."""
    data = None
    with open(DATA_FILEPATH+filename, "r") as data_file:
        lines = data_file.readlines()

        # Need to remove unneeded new line characters
        for i, line in enumerate(lines):
            line = line.replace("\n", "")
            lines[i] = line

        data = lines

    return data


def check_lvls(lvls, num_issues):

    safe = True
    if (abs(lvls[1] - lvls[0]) > 3) or (lvls[1] == lvls[0]):
        if num_issues == 1:
            return False
        else:
            lvls_0 = copy.deepcopy(lvls)
            lvls_0.pop(1)
            lvls_1 = copy.deepcopy(lvls)
            lvls_1.pop(0)
            safe = check_lvls(
                lvls_0, 1) or check_lvls(lvls_1, 1)
            return safe

    if ((lvls[1] > lvls[0]) != (lvls[2] > lvls[1])):
        if num_issues == 1:
            return False
        else:
            lvls_01 = copy.deepcopy(lvls)
            lvls_01.pop(2)
            lvls_02 = copy.deepcopy(lvls)
            lvls_02.pop(1)
            lvls_12 = copy.deepcopy(lvls)
            lvls_12.pop(0)
            safe = check_lvls(
                lvls_01, 1) or check_lvls(lvls_02, 1) or check_lvls(lvls_12, 1)
            return safe

    lvls_increasing = lvls[1] > lvls[0]
    for j in range(2, len(lvls)):
        if abs(lvls[j] - lvls[j-1]) > 3 or (lvls[j] == lvls[j-1]):
            if num_issues == 1:
                return False
            else:
                lvls_0 = copy.deepcopy(lvls)
                lvls_0.pop(j)
                lvls_1 = copy.deepcopy(lvls)
                lvls_1.pop(j-1)
                safe = check_lvls(
                    lvls_0, 1) or check_lvls(lvls_1, 1)
                break
        if (lvls[j] > lvls[j-1] and not lvls_increasing) or (lvls[j] < lvls[j-1] and lvls_increasing):
            if num_issues == 1:
                return False
            else:
                lvls_0 = copy.deepcopy(lvls)
                lvls_0.pop(j)
                lvls_1 = copy.deepcopy(lvls)
                lvls_1.pop(j-1)
                safe = check_lvls(
                    lvls_0, 1) or check_lvls(lvls_1, 1)
                break
    return safe

# =============================Helper Functions END============================


def get_solution(input_data):
    """Takes the input data and returns the solution."""
    # Put the actual logic here
    num_safe = 0
    for i, line in enumerate(input_data):
        lvls = line.split(" ")
        lvls = [int(val) for val in lvls]

        safe = check_lvls(lvls, 0)

        if safe:
            num_safe += 1

    output_data = num_safe
    return output_data


def main():
    """Imports data then gets and prints the solution."""
    data_filename = "data.txt"
    # data_filename = "testcase.txt"
    input_data = read_data_file(data_filename)
    solution = get_solution(input_data)

    print(solution)


if __name__ == "__main__":
    main()
