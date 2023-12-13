import numpy as np
import numpy.typing as npt


DIRECTIONS_ALLOWED = {
    "|": ["up", "down"],
    "-": ["left", "right"],
    "L": ["up", "right"],
    "J": ["up", "left"],
    "7": ["left", "down"],
    "F": ["down", "right"],
    "S": ["up", "down", "left", "right"]
}


def get_neighbor(grid: npt.NDArray, location: list[int], direction: str) -> list[int]:
    new_location = location.copy()
    match direction:
        case "up":
            new_location[0] -= 1
            return grid[new_location[0]][new_location[1]], "down", new_location
        case "down":
            new_location[0] += 1
            return grid[new_location[0]][new_location[1]], "up", new_location
        case "left":
            new_location[1] -= 1
            return grid[new_location[0]][new_location[1]], "right", new_location
        case "right":
            new_location[1] += 1
            return grid[new_location[0]][new_location[1]], "left", new_location
        case _:
            return None


def evaluate_direction(current: str, neighbor: str, direction: str) -> bool:
    match neighbor:
        case "|" if (direction in ["up", "down"] and
                     direction in DIRECTIONS_ALLOWED.get(current, [])):
            return True
        case "-" if (direction in ["left", "right"] and
                     direction in DIRECTIONS_ALLOWED.get(current, [])):
            return True
        case "L" if (direction in ["down", "left"] and
                     direction in DIRECTIONS_ALLOWED.get(current, [])):
            return True
        case "J" if (direction in ["down", "right"] and
                     direction in DIRECTIONS_ALLOWED.get(current, [])):
            return True
        case "7" if (direction in ["up", "right"] and
                     direction in DIRECTIONS_ALLOWED.get(current, [])):
            return True
        case "F" if (direction in ["up", "left"] and
                     direction in DIRECTIONS_ALLOWED.get(current, [])):
            return True
        case _:
            return False


def traverse_map(grid: str) -> int:
    uturn = None
    neighbor = None
    location = [n[0] for n in np.where(grid == "S")]
    current = "S"
    finished = False
    steps = 0

    while not finished:
        # for direction in ["up", "down", "left", "right"]:
        for direction in ["right", "left", "down", "up"]:
            if direction != uturn:
                neighbor, new_uturn, new_location = get_neighbor(grid, location, direction)
                if neighbor == "S":
                    steps += 1
                    print(f"Moving: {direction} to {neighbor} at step {steps}")
                    finished = True
                    break
                evaluation = evaluate_direction(current, neighbor, direction)
                if evaluation:
                    location = new_location
                    current = str(grid[location[0], location[1]])
                    uturn = new_uturn
                    steps += 1
                    print(f"Moving: {direction} to {neighbor}", end="\r", flush="True")
                    break
    print(f"Shortest route: {steps//2}")
    return int(steps//2) # A decimal would mean we could have arrived faster by starting with a different direction
            

def main():
    solutions = []
    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n")
            grid = np.array([[n for n in m] for m in data])

        solution = traverse_map(grid)
        solutions.append(solution)

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()