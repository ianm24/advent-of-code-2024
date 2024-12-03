"""Module containing boilerplate code to be used for each day of advent."""
import re

DATA_FILEPATH = "./2024/day3/"

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


def remove_invalid_chars(line):
    clean_line = line
    invalid_char_chunks = re.findall(r"don't\(\).*?do\(\)", clean_line)

    for chunk in invalid_char_chunks:
        clean_line = clean_line.replace(chunk, "")

    clean_line = re.sub(r"don't\(\).*", "", clean_line)

    return clean_line

# =============================Helper Functions END============================


def get_solution(input_data):
    """Takes the input data and returns the solution."""
    # Put the actual logic here
    fixed_input_data = "".join(input_data)
    muls_sum = 0
    all_muls = []
    clean_line = remove_invalid_chars(fixed_input_data)

    all_muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", clean_line)

    for mul in all_muls:
        mul = re.findall(r"[0-9]{1,3},[0-9]{1,3}", mul)
        mul_nums = mul[0].split(",")
        muls_sum += int(mul_nums[0]) * int(mul_nums[1])

    output_data = muls_sum
    return output_data


def main():
    """Imports data then gets and prints the solution."""
    data_filename = "data.txt"
    # data_filename = "testcase.txt"
    # data_filename = "testcase2.txt"
    input_data = read_data_file(data_filename)
    solution = get_solution(input_data)

    print(solution)


if __name__ == "__main__":
    main()
