import concurrent.futures
import numpy as np
import tqdm


def get_maps(data: list[str]) -> list[dict]:
    maps = {}
    seed_ranges = []
    for line in data:
        k, v = line.split(":")
        k = k.replace("-", "_").replace(" map", "")
        v = v.strip().split("\n")
        v = [n.split(" ") for n in v]
        if k == "seeds":
            seed_vals = [int(n) for n in v[0]]
            seed_range = [list(n) for n in np.array_split(seed_vals, len(seed_vals)/2)]
            seed_ranges.extend(seed_range)
            # for r in seed_range:
            #     import pdb; pdb.set_trace()
            #     for seed in range(r[0], r[0]+r[1]):
            #         seed_ranges.append(seed)
        else:
            maps[k] = v

    return seed_ranges, maps

def traverse_maps(seed: int, maps: dict) -> int:
    location = seed
    # print(f"\nSeed: {seed}")
    for m in maps.keys():
        location_changed = False
        maps[m] = [n for n in maps[m] if int(n[0]) < location]
        for s in maps[m]: # s == submap
            if int(s[1]) <= location:
                s = [int(n) for n in s] # converting to list[int], but this would me more efficient in get_maps()
                min_source = s[1]
                max_source = s[1] + s[2]
                min_destination = s[0]

                if min_source <= location <= max_source:
                    location_idx = location - min_source
                    location = min_destination + location_idx
                    location_changed = True
                    # print(f"Moving to {location} in {m.split('_')[-1]}.")
                    break
        # if not location_changed:
        #     print(f"No shortcut found. Moving to {location} in {m.split('_')[-1]}.")
        
    return location

def get_destinations(seed_ranges: list[list], maps: dict) -> list[int]:
    destinations = []
    for seed_range in seed_ranges:
        seeds = (n for n in range(seed_range[0], seed_range[0]+seed_range[1]))
        range_desc = f"RANGE: {seed_range}"
        for i in tqdm.trange(seed_range[1], desc=range_desc):
            seed = next(seeds)
            destination = traverse_maps(seed, maps)
            destinations.append(destination)

    return destinations

def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n\n")
        
        seed_ranges, maps = get_maps(data)
        # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        #     futures = []
        #     destinations = []
        #     for seed_range in seed_ranges:
        #         seed_range = [seed_range]
        #         futures.append(ex.submit(get_destinations, seed_range, maps))
        #     results = [future.result() for future in concurrent.futures.as_completed(futures)]
        #     for n in results:
        #         destinations.extend(n)
        destinations = get_destinations(seed_ranges, maps)
        solutions.append(min(destinations))

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()