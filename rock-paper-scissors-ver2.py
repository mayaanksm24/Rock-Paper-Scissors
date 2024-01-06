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
dict_result = {rock : {rock : 'draw', paper : "You Loose!",scissors : "You Win!"},
               paper : {rock : "You win!", paper : "draw",scissors : "You Loose!"},
               scissors : {rock : "You Loose!", paper : "You Win!", scissors : "Draw"}}
images=[rock,paper,scissors]
print("Welcome to ROCK PAPER SCISSORS")
while True:
    choice_of_user = int(input("What is your choice? 0-ROCK 1-PAPER 2-SCISSORS: "))
    if choice_of_user not in [0,1,2]:
        print("Invalid Choice. Please check menu and enter 0/1/2: ")
    print(f"Your choice is {images[choice_of_user]}")
    choice_of_computer = random.randint(0,2)
    print(f"Computer choice is {images[choice_of_computer]}")
    print(dict_result[images[choice_of_user]][images[choice_of_computer]])
    again = input("Do you want to play again (yes-y/no-n): ").lower()
    if again != 'y':
        print("Thanks for playing. Exiting...")
        break
   




