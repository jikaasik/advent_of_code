import itertools
import numpy as np

def get_empty_rows_and_cols(data_rows: list[str], data_cols: list[str]) -> tuple[list]:
    empty_rows = []
    empty_cols = []

    for i in range(len(data_rows)):
        if all([n == "." for n in data_rows[i]]):
            empty_rows.append(i)
    for i in range(len(data_cols)):
        if all([n == "." for n in data_cols[i]]):
            empty_cols.append(i)
    
    return empty_rows[::-1], empty_cols[::-1]


def expand_space(data: list[str], empty_rows: list[int], empty_cols: list[int]) -> list[str]:
    for n in data:
        for m in empty_cols:
            n.insert(m, ".")
    data = list(map(list, zip(*data)))

    for n in data:
        for m in empty_rows:
            n.insert(m, ".")
    data = list(map(list, zip(*data)))
    
    return data


def number_galaxies(data: list[str]) -> list[str]:
    flat_data = [item for row in data for item in row]
    counter = (n for n in range(len([m for m in flat_data if m == "#"])))
    numbers = [n for n in range(len([m for m in flat_data if m == "#"]))]
    for row in data:
        for j in range(len(row)):
            if row[j] == "#":
                row[j] = next(counter)

    return data, numbers


def get_distances(data: list[str], combos: list[tuple]) -> list[int]:
    data = np.array(data)
    distances = []
    for combo in combos:
        first = np.where(data == str(combo[0]))
        second = np.where(data == str(combo[1]))
        distance = abs(first[0][0] - second[0][0]) + abs(first[1][0] - second[1][0])
        distances.append(distance)

    return distances


def main():
    solutions = []
    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n")
            data_rows = [[n for n in m] for m in data]
            data_cols = list(map(list, zip(*data_rows)))
        

        empty_rows, empty_cols = get_empty_rows_and_cols(data_rows, data_cols)
        expanded_rows = expand_space(data_rows, empty_rows, empty_cols)
        numbered_data, numbers = number_galaxies(expanded_rows)
        combos = list(itertools.combinations(numbers, 2))
        distances = get_distances(numbered_data, combos)

        solutions.append(sum(distances))

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()