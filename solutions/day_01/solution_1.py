import re


def parse_input(lines: list[str]) -> list[int]:
    parsed_input = []
    for line in lines:
        line = line.replace("\n", "")

        line_as_list = list(line)
        line_as_list.reverse()
        reversed_line = "".join(line_as_list)

        parsed_input.append([line, reversed_line])
    
    return parsed_input


def get_digits_and_combine(line: list[str]) -> list[int]:

    line, reversed_line = [*line]

    first_digit = re.search('(\d)', line)
    last_digit = re.search('(\d)', reversed_line)
    digits = [first_digit.group(0), last_digit.group(0)]
    return int("".join(digits))


def get_calibration_values(lines: list[str]) -> list[int]:

    calibration_values = []
    parsed_input = parse_input(lines)
    
    for line in parsed_input:
        calibration_value = get_digits_and_combine(line)
        calibration_values.append(calibration_value)

    return calibration_values


def main():

    with open(f"train_input_1.txt", "r") as f:
        train_data = f.readlines()
    train_calibration_values = get_calibration_values(train_data)
    train_sum = sum(train_calibration_values)
    print(f"Training calibration values sum to: {train_sum}")

    with open(f"test_input_1.txt", "r") as f:
        test_data = f.readlines()
    test_calibration_values = get_calibration_values(test_data)
    test_sum = sum(test_calibration_values)
    print(f"Testing calibration values sum to: {test_sum}")

    print(f"Total sum: {train_sum + test_sum}")

    return (train_sum, test_sum)


if __name__ == "__main__":
    main()