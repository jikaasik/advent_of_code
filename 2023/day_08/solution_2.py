import math

def parse_data(data: str) -> tuple[list, list]:
    key, raw_paths = data.split("\n\n")
    directions = {"L": 0, "R": 1}
    key = [directions[n] for n in key]
    paths = [n for n in raw_paths.split("\n")]
    paths = [n.replace("(", "").replace(")", "").split(" = ") for n in raw_paths.split("\n")]
    starting_points = [n[0] for n in paths if n[0][-1] == "A"]
    paths = {k: v.split(", ") for k, v in paths}

    return key, paths, starting_points


def find_end(starting_point: str, paths: dict, key: list[int]):
    location = starting_point
    steps = 0
    iter_key = (i for i in key * 10000000)
    while not location.endswith('Z'):
        direction = next(iter_key)
        location = paths[location][direction]
        steps += 1
    return steps 

def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_2.txt", "r") as f:
            data = f.read()
            key, paths, starting_points = parse_data(data)

        steps = 1
        count = 1
        for starting_point in starting_points:
            if starting_point.endswith('A'):
                steps = math.lcm(steps, find_end(starting_point, paths, key))
            print(f"Least common multiple for count: {count}: {steps}", end="\r", flush="True")
            count += 1
        solutions.append(steps)

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()