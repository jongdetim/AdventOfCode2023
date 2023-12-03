def check_games(games):
    min_cubes = {}
    power = 1
    for game in games:
        for cubes in game.split(","):
            # print(cubes)
            amount, color = cubes[1:].split(" ")
            if color not in min_cubes or (int(amount) > min_cubes[color]):
                min_cubes[color] = int(amount)

    for color in min_cubes:
        power *= min_cubes[color]
    return power

with open("input_day2") as inputfile:
    data = inputfile.read().splitlines()
    powersum = 0

    for line in data:
        # game_id = int(line.split(":")[0].split(" ")[1])
        powersum += check_games(line.split(":")[1].split(";"))

    print(powersum)
        