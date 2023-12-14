

def get_prediction(history: list[int]) -> list[int]:
    if all([n==0 for n in history]):
        return 0
    differences = []
    for i in range(len(history)):
        if i > 0:
            differences.append(history[i] - history[i-1])

    return history[-1] + get_prediction(differences)


def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n")
            histories = [[int(m) for m in n.split(" ")] for n in data]

        predictions = []
        for history in histories:
            prediction = get_prediction(history)
            predictions.append(prediction)
            print(prediction)
        solutions.append(sum(predictions))

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()