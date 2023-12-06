import numpy as np
import re
import tqdm

def get_possible_outcomes(time: int) -> list[int]:
    outcomes = []
    for i in tqdm.trange(0, time+1):
        outcome = np.prod([i, time-i])
        if outcome:
            outcomes.append(outcome)

    return outcomes


def get_ways_to_win(race_params: list[tuple]) -> list[int]:
    ways_to_win = []

    time, distance = race_params
    possible_outcomes = get_possible_outcomes(time)
    winning_outcomes = len([n for n in possible_outcomes if n > distance])
    ways_to_win.append(winning_outcomes)
    
    return ways_to_win


def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            time, distance = f.read().split("\n")
            pattern = r"(\d+)"
            time_matches = re.finditer(pattern, time)
            distance_matches = re.finditer(pattern, distance)
            times = [n.group() for n in time_matches]
            distances = [n.group() for n in distance_matches]
            race_params = [int("".join(times)), int("".join(distances))]
        
        ways_to_win = get_ways_to_win(race_params)
        solution = np.product(ways_to_win)
        solutions.append(solution)


    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[1]}")

    return solutions


if __name__ == "__main__":
    main()