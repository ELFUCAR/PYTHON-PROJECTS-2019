import random

arr = []

numbers = [1, 2, 3, 4, 5, 6]

random.shuffle(numbers)

for i in range(0, 2):
    dice = random.choice(numbers)

    arr.append(dice)

print(arr)