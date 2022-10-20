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

import random
print("Welcome to the Rock, Paper and Scissors game!")

#Making Choice
human_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

#Creating a list for RPS
choice_list = [rock, paper, scissors]

#Printing choices
if human_choice <= 2 and human_choice >= 0:
  print(choice_list[human_choice])
  print("Computer choice:")
  print(choice_list[computer_choice])
else: 
  print("Invalid choice!")

#Deciding who wins
if human_choice==computer_choice:
  print("A draw")
elif human_choice==0 and computer_choice==1:
  print("You lose")
elif human_choice==0 and computer_choice==2:
  print("You win")
elif human_choice==1 and computer_choice==0:
  print("You win")
elif human_choice==1 and computer_choice==2:
  print("You lose")
elif human_choice==2 and computer_choice==0:
  print("You lose")
elif human_choice==2 and computer_choice==1:
  print("You win")