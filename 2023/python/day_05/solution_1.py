def get_maps(data: list[str]) -> list[dict]:
    maps = {}
    for line in data:
        k, v = line.split(":")
        k = k.replace("-", "_").replace(" map", "")
        v = v.strip().split(" ")
        import pdb; pdb.set_trace()

    # maps = {
    #     "seeds": 
    #     "seed_to_soil": 
    #     "soil_to_fertilizer": 
    #     "fertilizer_to_water": 
    #     "water_to_light": 
    #     "light_to_temperature": 
    #     "temperature_to_humidity": 
    #     "humidity_to_location": 
    # }


def main():
    solutions = []

    for input_type in ['train', 'test']:
        with open(f"{input_type}_input_1.txt", "r") as f:
            data = f.read().split("\n\n")
        
        maps = get_maps(data)


        lowest = None

        import pdb; pdb.set_trace()
        
    
    
    return solutions


if __name__ == "__main__":
    main()