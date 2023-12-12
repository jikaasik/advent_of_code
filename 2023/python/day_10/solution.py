import numpy as np

def traverse_map(grid: str) -> int:
    import pdb; pdb.set_trace()

def main():
    solutions = []
    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n")
            grid = np.array([[n for n in m] for m in data])

    solution = traverse_map(grid)

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()