
def parse_data(data: str) -> tuple[list, list]:
    key, raw_paths = data.split("\n\n")
    directions = {"L": 0, "R": 1}
    key = [directions[n] for n in key]
    paths = [n for n in raw_paths.split("\n")]
    paths = [n.replace("(", "").replace(")", "").split(" = ") for n in raw_paths.split("\n")]
    starting_point = paths[0][0]
    paths = {k: v.split(", ") for k, v in paths}

    return key, paths, starting_point


def find_end(key: list[int], paths: list[str], starting_point: str) -> int:
    steps_to_end = 0
    location = "AAA"
    iter_key = (i for i in key * len(paths))
    while location != "ZZZ":
        direction = next(iter_key)
        location = paths[location][direction]
        steps_to_end += 1

    return steps_to_end


def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read()
            key, paths, starting_point = parse_data(data)

        steps_to_end = find_end(key, paths, starting_point)
        solutions.append(steps_to_end)

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[1]}")

    return solutions


if __name__ == "__main__":
    main()