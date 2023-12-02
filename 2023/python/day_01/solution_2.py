import re

FIRST_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eleven": "1",
    "twelve": "1",
    "thirteen": "1",
    "fourteen": "1",
    "fifteen": "1",
    "twenty": "2",
    "thirty": "3",
    "forty": "4",
    "fifty": "5"
}

def parse_input(lines: list[str]) -> list[int]:
    parsed_input = []
    for line in lines:
        line = line.replace("\n", "")
        parsed_input.append(line)
    
    return parsed_input


def get_digits_and_combine(line: list[str]) -> int:

    all_matches = []

    # Get digit matches
    for i in range(10):
        matches = re.finditer(f"{i}", line)
        for m in matches:
            all_matches.append((m.start(), m.group()))
    
    # Get spelled matches
    for k in FIRST_DIGIT.keys():
        matches = re.finditer(f"{k}", line)
        for m in matches:
            all_matches.append((m.start(), FIRST_DIGIT[m.group()]))
    
    first_digit = sorted(all_matches)[0][1]
    last_digit = sorted(all_matches)[-1][1]
    combined_number = int("".join([first_digit, last_digit]))

    import pdb; pdb.set_trace()

    return combined_number


def get_calibration_values(lines: list[str]) -> list[int]:

    calibration_values = []
    parsed_input = parse_input(lines)
    
    for line in parsed_input:
        calibration_value = get_digits_and_combine(line)
        calibration_values.append(calibration_value)

    return calibration_values


def main():

    with open(f"train_input_2.txt", "r") as f:
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