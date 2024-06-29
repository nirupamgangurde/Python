def count_unique(numbers):
    empty_set = set()
    for num in numbers:
        empty_set.add(num)
    return len(empty_set)

num1 = [1,1,1,1,1,1,1]
print(count_unique(num1))
