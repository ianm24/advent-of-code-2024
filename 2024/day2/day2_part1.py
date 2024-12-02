"""Module containing boilerplate code to be used for each day of advent. 10:42"""

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

# =============================Helper Functions END============================


def get_solution(input_data):
    """Takes the input data and returns the solution."""
    # Put the actual logic here
    num_safe = 0
    for i, line in enumerate(input_data):
        nums = line.split(" ")
        nums = [int(val) for val in nums]
        safe = True
        if (abs(nums[1] - nums[0]) > 3) or (nums[1] == nums[0]):
            continue
        nums_increasing = nums[1] > nums[0]
        for j in range(2, len(nums)):
            if abs(nums[j] - nums[j-1]) > 3 or (nums[j] == nums[j-1]):
                safe = False
                break
            if (nums[j] > nums[j-1] and not nums_increasing) or (nums[j] < nums[j-1] and nums_increasing):
                safe = False
                break
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
