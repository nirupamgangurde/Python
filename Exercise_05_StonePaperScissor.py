import random
def get_computer_choice():
    choices = ["stone", "paper", "scissor"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (stone, paper, scissor :")
        if user_input in ["stone", "paper", "scissor"]:
            return user_input
        else:
            print("Invalid Syntax!!!")

def winner(user_choice , computer_choice):
    if (computer_choice == user_choice ):
        return "TIE!!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return "You Win!!!"
    else:
        return "You Lose!!!"

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You Choose {user_choice}")
    print(f"{computer_choice}")
    result = winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play()

