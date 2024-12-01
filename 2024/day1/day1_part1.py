"""Module containing boilerplate code to be used for each day of advent."""

DATA_FILEPATH = "./2024/day1/"

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

    left_list = []
    right_list = []
    distance_sum = 0

    for line in input_data:
        temp = line.split(" ")
        left_list.append(int(temp[0]))
        right_list.append(int(temp[len(temp)-1]))

    left_list.sort()
    right_list.sort()

    for i, _ in enumerate(left_list):
        distance_sum += abs(left_list[i]-right_list[i])

    output_data = distance_sum
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