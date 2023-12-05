import math

with open("input_day3") as file:
    result = 0
    data = file.read()
    digit_indices = []
    asterix = {}
    width = len(data.splitlines()[0]) + 1
    length = len(data.splitlines())
    for i, char in enumerate(data):
        if char.isdigit():
            digit_indices.append(i)

    i = 0
    while i < len(digit_indices):
        # print(digit_indices[i])
        index = digit_indices[i]
        # print("index: ", index)

        cursor = index
        valid = False
        while cursor % width < width - 1 and data[cursor].isdigit():
            if not valid:
                row, col = divmod(cursor, width)
                

                surrounding_indices = [
                    cursor - width if row > 0 else None,  # Up
                    cursor + width if row < length - 1 else None,  # Down
                    cursor - 1 if col > 0 else None,  # Left
                    cursor + 1 if col < width - 2 else None,  # Right
                    cursor - width - 1 if col > 0 and row > 0 else None,  # Top-left diagonal
                    cursor - width + 1 if col < width - 2 and row > 0 else None,  # Top-right diagonal
                    cursor + width - 1 if col > 0 and row < length - 1 else None,  # Bottom-left diagonal
                    cursor + width + 1 if col < width - 2 and row < length - 1 else None  # Bottom-right diagonal
                ]

                surrounding_chars = [(data[j], j) for j in surrounding_indices if j != None]
                # print(surrounding_chars)
                for char, idx in surrounding_chars:
                    if char == '*':
                        x = idx
                        valid = True
                        break

            cursor += 1
        if valid:
            number = int(data[index:cursor])
            # print(index, cursor, number)
            if x in asterix:
                asterix[x].append(number)
            else:
                asterix[x] = [number]
        
        i += cursor - index

    # print(asterix)

    for key in asterix:
        if len(asterix[key]) == 2:
            result += math.prod(asterix[key])

    print(result)
