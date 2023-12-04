import re


def get_lines(data: list[str]) -> list[list]:
    cleaned_lines = []
    lines = data.split("\n")
    for line in lines:
        my_string, winning_string = line.split(": ")[-1].split("|")
        pattern = r"(\d+)"
        my_matches = re.finditer(pattern, my_string)
        winning_matches = re.finditer(pattern, winning_string)
        my_nums = []
        winning_nums = []
        for m in my_matches:
            my_nums.append(int(m.group()))
        for m in winning_matches:
            winning_nums.append(int(m.group()))
        cleaned_lines.append([my_nums, winning_nums])
    
    return cleaned_lines


def get_winnings(lines: list[list]) -> list[int]:
    winnings = []
    for line in lines:
        my, winning = [*line]
        num_matches = len(set(my).intersection(set(winning)))
        card_value = calculate_winnings(num_matches)
        winnings.append(card_value)

    return winnings


def calculate_winnings(num_matches: int) -> int:
    if num_matches < 3:
        return num_matches
    else:
        return 2**(num_matches - 1)



def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read()
        
        lines = get_lines(data)
        winnings = get_winnings(lines)
        solutions.append(sum(winnings))
    
    
    return solutions


if __name__ == "__main__":
    main()