import functools
from collections import Counter

suits = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

# ascending comparison
def cmp_hands(hand1, hand2):
    counter1 = [count for item, count in Counter(hand1).most_common() if item != 'J']
    count1 = (counter1[0] if counter1 else 0) + Counter(hand1)['J']
    counter2 = [count for item, count in Counter(hand2).most_common() if item != 'J']
    count2 = (counter2[0] if counter2 else 0) + Counter(hand2)['J']
    if count1 != count2:
        return count1 - count2
    if count1 == count2:
        if count1 <= 4:
            # full house and two pair
            if counter1[1] != counter2[1]:
                return counter1[1] - counter2[1]
    # equal combinations (pair, 3, 4, 5 of a kind, or nothing)
    for i in range(0, len(hand1)):
        if suits.index(hand1[i]) != suits.index(hand2[i]):
            return suits.index(hand1[i]) - suits.index(hand2[i])
        
    # identical hands
    return 0

with open('input_day7') as f:
    data = f.read().splitlines()

hands, bids = [], []

# parse
for line in data:
    split = line.split()
    hands.append(split[0])
    bids.append(int(split[1]))

# sorting (ascending)
hands_sorted = sorted(hands, key=functools.cmp_to_key(cmp_hands))

# score function
score = 0

for i in range(0, len(hands)):
    idx = hands.index(hands_sorted[i])
    score += bids[idx] * (i + 1)

print(hands_sorted)
print(score)
