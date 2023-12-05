digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

with open("input_day1") as input:
    som = 0
    for line in input:
        found = []
        for i, char in enumerate(line):
            if char.isdigit():
                found.append(char)
            else:
                for digit in digits:
                    if line[i:].startswith(digit):
                        found.append(str(digits.index(digit) + 1))
                        break
        result = int(found[0] + found[-1])
        som += result
    print(som)
