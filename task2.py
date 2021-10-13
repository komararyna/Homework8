import random
a = set()
b = set()
for item in range(1, 100):
    num = random.randint(1, 100)
    if num % 3 == 0:
        a.add(num)
for item in range(1, 100):
    num = random.randint(1, 100)
    if num % 5 == 0:
        b.add(num)
print(a, b, a & b, sep = '\n')
