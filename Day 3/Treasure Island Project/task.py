from os import waitpid

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at crossroad, '
                'where do you want to go? type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to the lake. '
                    'Type "wait" to wait for boat.'
                    'Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input('You\'re arrived unharmed to island.'
                         ' There is one house with 3 door.'
                         'one red, one yellow and one blue.'
                         'Which colour do you choose? \n').lower()
        if choice3 == "red":
            print("Its a room full of fire. Game over")
        elif choice3 == "yellow":
            print("You found the treasure hunt. You win!")
        elif choice3 == "blue":
            print("You enter a room of beast. Game over.")
        else:
            print("You choose a door that doesn't exist. Game over.")

    else:
        print("You got attacked by angry out. Game over")

else:
    print("Game over. You fell into the hole")