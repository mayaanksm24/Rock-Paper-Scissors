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
print("Welcome to ROCK PAPER SCISSORS")
while True:
  choice_of_user = int(input("What is your choice? 0 - ROCK 1-PAPER 2-SCISSORS: "))
  if choice_of_user == 0:
    print(rock)
  elif choice_of_user == 1:
    print(paper)
  else:
    print(scissors)
  print("Computer chose: ")
  choice_of_computer = random.randint(0,3)
  if choice_of_computer == 0:
    print(rock)
  elif choice_of_computer == 1:
    print(paper)
  else:
    print(scissors)
  if choice_of_user == choice_of_computer:
    print("Choose again")
  elif choice_of_user == 0 and choice_of_computer == 1:
    print("You lose")
  elif choice_of_user == 0 and choice_of_computer == 2:
    print("You Win")
  elif choice_of_user == 1 and choice_of_computer == 0:
    print("You Win")
  elif choice_of_user == 1 and choice_of_computer == 2:
    print("You Lose")
  elif choice_of_user == 2 and choice_of_computer == 0:
    print("You Lose")
  elif choice_of_user == 2 and choice_of_computer == 1:
    print("You Win")
  elif choice_of_user > choice_of_computer:
    print("You have typed an invalid number, you lose")
  again = input("Do you want to play again (yes-y/no-n): ").lower()
  if again != 'y':
    print("Thanks for playing. Exiting...")
    break