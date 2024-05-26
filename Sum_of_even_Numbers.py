def sum_of_even_Numbers (numbers: list) -> int:
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
    return sum_even


input_numbers = input("Enter list of integers seprated by spaces : ")
number_list = list(map(int, input_numbers.split()))
result = sum_of_even_Numbers(number_list)
print(f"The sum of Even number is : ",result)