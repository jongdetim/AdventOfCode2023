import math

# times = [47,98,66,98]
# distances = [400,1213,1011,1540]
times = [47986698]
distances = [400121310111540]

count = [0]

for i in range(len(count)):
    start = times[i] // 2
    while(start > 0):
        if start * (times[i] - start) > distances[i]:
            count[i] += 2
        else:
            break
        start -= 1
    count[i] -= (1 - times[i] % 2)

# print(count)
print(math.prod(count))
