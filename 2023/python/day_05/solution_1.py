def get_maps(data: list[str]) -> list[dict]:
    maps = {}
    for line in data:
        k, v = line.split(":")
        k = k.replace("-", "_").replace(" map", "")
        v = v.strip().split("\n")
        v = [n.split(" ") for n in v]
        if k == "seeds":
            seeds = [int(n) for n in v[0]]
        else:
            maps[k] = v

    return seeds, maps

def traverse_maps(seed: int, maps: dict) -> int:
    location = seed
    print(f"\nSeed: {seed}")
    for m in maps.keys():
        location_changed = False
        for s in maps[m]: # s == submap
            s = [int(n) for n in s] # converting to list[int], but this would me more efficient in get_maps()
            min_source = s[1]
            max_source = s[1] + s[2]
            min_destination = s[0]

            if min_source <= location <= max_source:
                location_idx = location - min_source
                location = min_destination + location_idx
                location_changed = True
                print(f"Moving to {location} in {m.split('_')[-1]}.")
                break
        if not location_changed:
            print(f"No shortcut found. Moving to {location} in {m.split('_')[-1]}.")
        
    return location

def get_destinations(seeds: list[int], maps: dict) -> list[int]:
    destinations = []
    for seed in seeds:
        destination = traverse_maps(seed, maps)
        destinations.append(destination)

    return destinations

def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n\n")
        
        seeds, maps = get_maps(data)
        destinations = get_destinations(seeds, maps)
        solutions.append(min(destinations))
    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[1]}")

    return solutions


if __name__ == "__main__":
    main()