import numpy as np
import re


def get_schematic_dimensions(data: str) -> list[int]:

    lines = data.split("\n")
    height = len(lines)
    width = len(lines[0])
    # Ensure that width is consistent
    try:
        assert len(set([len(n) for n in lines])) == 1
    except:
        raise Exception("Inconsistent schematic width.")
    
    return (height, width)


def get_target_locations(data: str, type: str) -> list[list]:
    lines = data.split("\n")
    target_locations = []
    if type == "part":
        pattern = r"(\d+)"
    elif type == "gear":
        pattern = r"(\*)"
    else:
        raise Exception("No valid type provided.")

    for i in range(len(lines)):
        matches = re.finditer(pattern, lines[i])

        for m in matches:
            number = m.group()
            start = m.start()
            end = m.end() - 1
            target_locations.append((i, number, start, end))
    
    return target_locations


def get_adjacent_sections(number: tuple, lines: list[str], dimensions: tuple) -> list:
    """
    Iterate through lines by index. In each case, get the locations of number digits,
    then search for the same indicex +/- 1 on the prior and subsequent lines"""
    _, width = dimensions
    begin, end = number[2:4]    
    relevant_rows = set([number[0]-1, number[0], number[0]+1]).intersection(set(range(0, len(lines))))
    relevant_indices = set(range(begin-1, end+2)).intersection(set(range(0, width)))
    adjacent_sections = []
    for row in relevant_rows:
        adjacent_sections.append([row, min(relevant_indices), max(relevant_indices)])
    
    return adjacent_sections
    

def get_adjacent_target(sections: list[list], lines: list[str]) -> bool:
    relevant_lines = [n[0] for n in sections]

    line_index = 0
    for i in relevant_lines:
        line = lines[i]
        begin = sections[line_index][-2]
        end = sections[line_index][-1]
        substring = line[begin:end+1]
        pattern = r"[\!\@\#\$\%\^\&\*\(\)\-\=\\\`\_\+\|\~\{\}\;\'\:\"\<\>\/\[\]]"
        matches = [re.search(pattern, substring)]
        match = next((value for value in matches if value is not None), None)
        line_index += 1
        if match:
            return True

    return False


def identify_parts(numbers: list[tuple], lines: list[str], data: str, dimensions: tuple) -> list:
    valid_parts = []
    for i in range(len(lines)):
        potential_parts = [n for n in numbers if n[0] == i]
        if len(potential_parts):
            for number in potential_parts:
                adjacent_sections = get_adjacent_sections(number, lines, dimensions)
                adjacent_symbol = get_adjacent_target(adjacent_sections, lines)

                if adjacent_symbol:
                    valid_parts.append(int(number[1]))


    return valid_parts


def identify_gears(gears: list[tuple], numbers: list[tuple], lines: list[str], dimensions: tuple) -> list:
    valid_gears = []
    for i in range(len(lines)):
        potential_gears = [n for n in gears if n[0] == i]
        if len(potential_gears):
            for gear in potential_gears:
                adjacent_numbers = []
                adjacent_sections = get_adjacent_sections(gear, lines, dimensions)
                for number in numbers:
                    relevant_sections = [n for n in adjacent_sections if n[0] == number[0]]
                    for section in relevant_sections:
                        overlap = set(range(section[1], section[2]+1)).intersection(set(range(number[2], number[3]+1)))
                        if len(overlap):
                            adjacent_numbers.append(int(number[1]))
                if len(adjacent_numbers) == 2:
                    valid_gears.append(np.product(adjacent_numbers))
    
    return valid_gears



def main():
    response = []
    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read()

        lines = data.split("\n")
        dimensions = get_schematic_dimensions(data)

        numbers = get_target_locations(data, "part")
        valid_parts = identify_parts(numbers, lines, data, dimensions)
        # valid_gears = identify_parts(gears, lines, data, dimensions, "number")
        gears = get_target_locations(data, "gear")
        gear_ratios = identify_gears(gears, numbers, lines, dimensions)
        response.append([sum(valid_parts), sum(gear_ratios)])
        print(f"The valid parts for the {input_type} data sum to: {sum(valid_parts)}")
        print(f"The gear ratios for the {input_type} data sum to: {sum(gear_ratios)}")

    return response


if __name__ == "__main__":
    main()