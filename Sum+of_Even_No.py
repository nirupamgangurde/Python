def sum_of_even_numbers(numbers : list) -> int:
    total_sum = 0
    for num in numbers:
        if num % 2 == 0:
            total_sum += num
    return total_sum

numbers = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_even_numbers(numbers))