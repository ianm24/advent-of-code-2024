"""Module containing boilerplate code to be used for each day of advent."""
import numpy as np
import math

DATA_FILEPATH = "./2024/day5/"

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


def parse_rules(rules):
    rules_dict = {}

    for rule in rules:
        nums = rule.split("|")
        num_before = int(nums[0])
        num_after = int(nums[1])

        if num_before not in rules_dict:
            rules_dict[num_before] = np.array([num_after])
        else:
            rules_dict[num_before] = np.append(
                rules_dict[num_before], num_after)

    return rules_dict


# =============================Helper Functions END============================


def get_solution(input_data):
    """Takes the input data and returns the solution."""
    # Put the actual logic here
    middle_num_sum = 0
    break_idx = input_data.index("")
    rules = input_data[0:break_idx]
    updates = input_data[break_idx+1:]

    rules_dict = parse_rules(rules)

    # Check each update for validity
    for update_str in updates:
        update = [int(num) for num in update_str.split(",")]

        rev_update = list(reversed(update))
        valid_update = True
        for i, num in enumerate(rev_update):
            if num not in rules_dict or i == len(update)-1:
                continue

            # Get intersection of nums prior in update and nums in rule
            intersection = list(set(rev_update[i+1:]) & set(rules_dict[num]))
            if len(intersection) > 0:
                valid_update = False
                break

        if valid_update:
            # Get middle number from update and add to sum
            middle_num_idx = math.ceil(len(update) / 2) - 1
            middle_num_sum += update[middle_num_idx]

    output_data = middle_num_sum
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
