def checkmatches(line, idx):
    total = 0
    line = line.split(":")[1].split("|")
    winningnums = line[0].split()
    cardnums = line[1].split()
    matches = sum(1 for num in winningnums if num in cardnums)
    for i in range(matches):
        total += checkmatches(data[idx + i + 1], idx + i + 1)
    return total + matches

with open("input_day4") as file:
    data = file.read().splitlines()

total = 0
for i, line in enumerate(data):
    total += checkmatches(line, i) + 1

print(total)
