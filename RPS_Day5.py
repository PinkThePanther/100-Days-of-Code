import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("Choose 0 for Rock, 1 for Paper, and 2 for Scissors\n "))
computer_choice = random.randint(0,2)

print(f"computer chose:{computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("invalid response")

elif user_choice == 0  and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win")
elif user_choice == computer_choice:
    print("its a draw")
