value =int(input("Enter value: "))
a = 0
b = 1
count = 0
if value <= 0:
    print("Enter valid input")
elif value == 1:
    print(f"Fibonacci sequence upto {value} : ")
    print(a)
else:
    print("fibonacci Sequence ")
    while count < value:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1
