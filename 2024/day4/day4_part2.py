"""Module containing boilerplate code to be used for each day of advent."""
import re
import numpy as np

DATA_FILEPATH = "./2024/day4/"

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


# =============================Helper Functions END============================


def get_solution(input_data):
    """Takes the input data and returns the solution."""
    # Put the actual logic here
    num_xmas = 0
    letters = [list(chars) for chars in input_data]
    word_search_mat = np.array(letters)

    last_row = word_search_mat.shape[0] - 3
    last_col = word_search_mat.shape[1] - 3

    for i in range(last_row+1):
        for j in range(last_col+1):
            # Get the current area to check for X-MAS
            curr_x = word_search_mat[i:i+3, j:j+3]

            # Convert to string
            check_str = "".join(curr_x.flatten())

            # Check all possible permutations of X-MAS
            perm_1 = bool(re.search("M.S.A.M.S", check_str))
            perm_2 = bool(re.search("M.M.A.S.S", check_str))
            perm_3 = bool(re.search("S.S.A.M.M", check_str))
            perm_4 = bool(re.search("S.M.A.S.M", check_str))

            if perm_1 or perm_2 or perm_3 or perm_4:
                num_xmas += 1

    output_data = num_xmas
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
