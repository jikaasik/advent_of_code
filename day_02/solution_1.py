import re

MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_cube_counts(line: str) -> dict:
    cube_count = {}
    for color in MAX_CUBES.keys():
        pattern = f"(\d+) ({color})"
        matches = re.findall(pattern, line)
        cube_count[color] = sum([int(n[0]) for n in matches])

    return cube_count


def check_valid_game(cube_count):
    is_valid_game = True
    for color in MAX_CUBES.keys():
        if cube_count[color] > MAX_CUBES[color]:
            is_valid_game = False
    
    return is_valid_game



def get_valid_games(lines: list[str]) -> list[int]:
    valid_games = []
    for line in lines:
        line_index = re.search("\d+", line).group(0)

        draws = line.split(": ")[-1].split(";")
        valid_draws = []
        for draw in draws:
            cube_count = get_cube_counts(draw)
            is_valid_game = check_valid_game(cube_count)
            valid_draws.append(is_valid_game)

        if all(valid_draws):
            valid_games.append(int(line_index))
    
    return set(valid_games)


def main():

    response = []
    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read()
        lines = data.split("\n")

        valid_games = get_valid_games(lines)
        sum_valid_games = sum(valid_games)
        print(f"Valid game indices in {input_type} data sum to {sum_valid_games}")

        response.append(sum_valid_games) 
    
    return response



if __name__ == "__main__":
    main()