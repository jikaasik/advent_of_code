import re


def get_lines(data: list[str]) -> int:
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


def get_sum_cards(lines: list[list]) -> list[int]:
    matches = []
    for line in lines:
        my, winning = [*line]
        num_matches = len(set(my).intersection(set(winning)))
        matches.append(num_matches)
    num_cards = get_num_cards(matches)

    return sum(num_cards)


def get_num_cards(matches: list[int]) -> list[int]:
    num_cards = [1] * len(matches)
    for i in range(len(num_cards)):
        current_card = matches[i]
        for j in range(1, matches[i]+1):
            num_cards[i+j] += num_cards[i]

    return num_cards

def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read()
        
        lines = get_lines(data)
        sum_cards = get_sum_cards(lines)
        solutions.append(sum_cards)
        print(f"The total number of cards is: {sum_cards}")
    
    return solutions


if __name__ == "__main__":
    main()