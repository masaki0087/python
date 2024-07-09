def for1():
    fruits = ["apple", "banana", "orange", "grape", "melon"]

    for i, name in enumerate(fruits):
        print(i * 2, name)

def for2():
    numbers = [i % 4 for i in range(0,11)]
    print(numbers)

def for3():
    numbers = [i for i in range(0,21) if i < 10 or 18 < i]
    print(numbers)

for3()