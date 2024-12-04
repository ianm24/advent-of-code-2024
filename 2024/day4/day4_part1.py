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


# Direction 0 for horizontal, 1 for vertical
def get_cardinal_xmas_matches(word_search_mat, direction):
    num_xmas = 0
    if direction == 1:
        word_search_mat = word_search_mat.transpose()

    for i in range(word_search_mat.shape[direction]):
        forward = "".join(word_search_mat[i])
        forward_matches = re.findall("XMAS", forward)
        forward_count = len(forward_matches)

        backward = "".join(reversed(word_search_mat[i]))
        backward_matches = re.findall("XMAS", backward)
        backward_count = len(backward_matches)

        num_xmas += forward_count + backward_count

    return num_xmas

# Direction 0 for axis1=0, 1 for axis1=1


def get_diagonal_xmas_matches(word_search_mat, direction):
    num_xmas = 0
    if direction == 1:
        word_search_mat = np.fliplr(word_search_mat)

    first_diagonal = 4 - word_search_mat.shape[direction]
    last_diagonal = word_search_mat.shape[direction] - 4

    for i in range(first_diagonal, last_diagonal+1):

        working_line = word_search_mat.diagonal(offset=i)
        forward = "".join(working_line)
        forward_matches = re.findall("XMAS", forward)
        forward_count = len(forward_matches)

        backward = "".join(reversed(working_line))
        backward_matches = re.findall("XMAS", backward)
        backward_count = len(backward_matches)

        num_xmas += forward_count + backward_count

    return num_xmas


# =============================Helper Functions END============================


def get_solution(input_data):
    """Takes the input data and returns the solution."""
    # Put the actual logic here
    num_xmas = 0
    letters = [list(chars) for chars in input_data]
    word_search_mat = np.array(letters)

    # Horizontal checks
    num_xmas += get_cardinal_xmas_matches(word_search_mat, 0)

    # Vertical checks
    num_xmas += get_cardinal_xmas_matches(word_search_mat, 1)

    # Diagonal checks
    num_xmas += get_diagonal_xmas_matches(word_search_mat, 0)
    num_xmas += get_diagonal_xmas_matches(word_search_mat, 1)

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
