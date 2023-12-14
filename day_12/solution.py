
def main():
    solutions = []
    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n")
        import pdb; pdb.set_trace()

        solutions.append(solution)

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()