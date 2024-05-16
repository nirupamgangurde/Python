a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd Number : "))
print(" A to perform Addition \n S to perform Substraction \n M to perform Multiplication")
c = input("Please enter input : ")
if c=='A':
    result = a + b
    print(f"Addition of {a} and {b} is {result} ")
elif c =="S":
    result = a - b
    print(f"Substraction of {a} and {b} is {result} ")

elif c =="M":
    result = a * b
    print(f"Multiplication of {a} and {b} is {result} ")

else:
    print("Invalid Input!!!")