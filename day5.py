import math

def parse_map(data, i, map):
    while i < len(data) and data[i] != "":
        map.append([int(num) for num in data[i].split()])
        i += 1

def parse_input(data):
    # seeds = [int(seed) for seed in data[0].split("seeds: ")[1].split()]
    seeds = iter(int(seed) for seed in data[0].split("seeds: ")[1].split())
    pairs = zip(seeds, seeds)
    seeds = []
    for start, length in pairs:
        # print(list(range(start, start + length)))
        seeds.extend(seed for seed in list(range(start, start + length)))
        print(seeds[0:100])
        # print("AHHHH")

    
    
    for i, line in enumerate(data):
        if line.startswith("seed-to-soil map:"):
            parse_map(data, i + 1, seed_to_soil_map)
        elif line.startswith("soil-to-fertilizer map:"):
            parse_map(data, i + 1, soil_to_fertilizer_map)
        elif line.startswith("fertilizer-to-water map:"):
            parse_map(data, i + 1, fertilizer_to_water_map)
        elif line.startswith("water-to-light map:"):
            parse_map(data, i + 1, water_to_light_map)
        elif line.startswith("light-to-temperature map:"):
            parse_map(data, i + 1, light_to_temperature_map)
        elif line.startswith("temperature-to-humidity map:"):
            parse_map(data, i + 1, temperature_to_humidity_map)
        elif line.startswith("humidity-to-location map:"):
            parse_map(data, i + 1, humidity_to_location_map)
    return seeds

if __name__ == "__main__":
    with open("input_day5") as file:
        data = file.read().splitlines()

    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    seeds = parse_input(data)
    maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]
    result = math.inf
    for seed in seeds:
        current = seed
        for map in maps:
            for row in map:
                if current >= row[1] and current < row[1] + row[2]:
                    current = current + (row[0] - row[1])
                    break
        if current < result:
            result = current
    
    print(result)
