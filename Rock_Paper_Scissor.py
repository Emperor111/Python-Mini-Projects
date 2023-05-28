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

#Write your code below this line 👇
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player==0:
  print(rock)
elif player==1:
  print(paper)
else:
  print(scissors)
  
computer=random.randint(0,2)
print("Computer chose:")

if computer==0:
  print(rock)
elif computer==1:
  print(paper)
else:
  print(scissors)

if player==0:
  if computer==0:
    print("It's a Draw!")
  elif computer==1:
    print("You Lose!")
  elif computer==2:
    print("You Win!")
elif player==1:
  if computer==1:
    print("It's a Draw!")
  elif computer==2:
    print("You Lose!")
  elif computer==0:
    print("You Win!")
elif player==2:
  if computer==2:
    print("It's a Draw!")
  elif computer==0:
    print("You Lose!")
  elif computer==1:
    print("You Win!")

"""
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end    
"""