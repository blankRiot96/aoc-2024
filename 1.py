import utils

sample = utils.get_aoc_input(1)

str_pairs = sample.splitlines()
str_pairs.pop(0)  # Remove \n

l1, l2 = [], []

for pair in str_pairs:
    a, b = pair.split()
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()

utils.answer(1, sum(abs(a - b) for a, b in zip(l1, l2)))

total = 0
for a in l1:
    count = l2.count(a)
    total += a * count

utils.answer(2, total)
