import numpy as np


def get_maps(data: list[str]) -> list[dict]:
    maps = []
    seed_ranges = []
    for line in data:
        k, v = line.split(":")
        k = k.replace("-", "_").replace(" map", "")
        v = v.strip().split("\n")
        v = [n.split(" ") for n in v]
        # Sorting by the length of the range removes some of the computational load,
        # cause we can stop early if we find a match
        v = sorted([[int(n) for n in lst] for lst in v], key=lambda x: x[-1])
        if k == "seeds":
            seed_vals = [int(n) for n in v[0]]
            seed_range = [list([n[0], n[0]+n[1]]) for n in np.array_split(seed_vals, len(seed_vals)/2)]
            seed_ranges.extend(seed_range)

        else:
            maps.append(v)
    return seed_ranges, maps


# def get_min_destination(seed_ranges: list[list], maps: dict) -> int:
#     seed = 0
#     seed_match = False
#     map_keys = [n for n in maps.keys()]
#     map_keys.reverse()

#     while not seed_match:
#         location = seed
#         path = []
#         for i in range(len(map_keys)):
#             # print(f"Using {map_keys[i]}")
#             for sublist in maps[map_keys[i]]:
#                 if location in range(sublist[0], sublist[0]+sublist[2]):
#                     location = sublist[1] + (location - sublist[0])
#                     break

#             path.append(location)
#         for seed_range in seed_ranges:
#             if seed_range[0] <= location <= seed_range[0] + seed_range[1]:
#                 print(seed)
#                 seed_match = True
#         if seed_match == True:
#             break
#         seed += 1
#         print(f"Seed: {seed}", end="\r", flush="True")
#         # print(seed)
#     return seed

def get_min_destination(seed_ranges: list[list], maps: list[list]) -> int:
    locations = []
    results = []
    for m in maps:
        while seed_ranges:
            start_range, end_range = seed_ranges.pop()
            for target, start_map, r in m:
                end_map = start_map + r
                offset = target - start_map
                if end_map <= start_range or end_range <= start_map:  # no overlap
                    continue
                if start_range < start_map:
                    seed_ranges.append([start_range, start_map])
                    start_range = start_map
                if end_map < end_range:
                    seed_ranges.append([end_map, end_range])
                    end_range = end_map
                results.append([start_range + offset, end_range + offset])
                break
            else:
                results.append([start_range, end_range])
        seed_ranges = results
        results = []
    locations += seed_ranges
    min_loc = min([loc[0] for loc in locations])
    print(min(loc[0] for loc in locations))

    return min_loc


def main():
    solutions = []

    for input_type in ['train', 'test']:
        print(input_type.upper())
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n\n")
        
        seed_ranges, maps = get_maps(data)
        destination = get_min_destination(seed_ranges, maps)

        solutions.append(destination)

    print(f"\nSolutions:\nTrain: {solutions[0]}\nTest: {solutions[-1]}")

    return solutions


if __name__ == "__main__":
    main()