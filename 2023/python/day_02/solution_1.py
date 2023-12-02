MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_cube_count():
    pass


def check_valid_game():
    pass


def get_valid_games(lines: list[str]) -> list[int]:
    for line in lines:
        cube_count = get_cube_count(line)
        is_valid_game = check_valid_game(cube_count)

    pass


def main():
    with open("train_input_1.txt", "r") as f:
        data = f.read()
    lines = data.split("\n")

    valid_games = get_valid_games(lines)


if __name__ == "__main__":
    main()