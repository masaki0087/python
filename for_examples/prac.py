def for1():
    fruits = ["apple", "banana", "orange", "grape", "melon"]

    for i, name in enumerate(fruits):
        print(i * 2, name)

def for2():
    numbers = [i % 4 for i in range(1,11)]
    print(numbers)

for2()