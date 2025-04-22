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
game_images = [rock,paper,scissors]
user_choice = int(input('What do you choose?'
                    'Type 0 for Rock,'
                    'Type 1 for paper,'
                    'Type 2 for Scissors.\n'))
if user_choice >= 0 and user_choice <= 2:
    print("User Choice:")
    print(game_images[user_choice])
else:
    print("you made a wrong choice")
comp_choice = random.randint(0,2)
if comp_choice >= 0 and comp_choice <= 2:
    print(f"Computer choose {comp_choice}")
    print(game_images[comp_choice])
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)
if user_choice == 0:
    if comp_choice == 0:
        print('Draw')
    else:
        print("You loose")
if user_choice == 1:
    if comp_choice == 0:
        print("You won")
    elif comp_choice == 1:
        print("Draw")
    else:
        print("You loose")
if user_choice == 2:
    if comp_choice == 2:
        print("Draw")
    elif comp_choice == 1:
        print("You won")
    else:
        print("you loose")