sum = 0
while(True):
    userInput = input("Enter the item price or press q to exit : \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far : {sum}")
    else:
        print(f"Your bill total is {sum}. Thanks for shopping with us")
        break
