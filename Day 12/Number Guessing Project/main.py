import random
import art
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(user_guess,actual_answer,turns):
    """Check answer against guess returns number ot turns remaining"""
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it. The answer was {actual_answer}")
def set_difficulty():
    level =input("Choose a difficulty. Type 'easy' or 'hard'.\n").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
print(art.logo)
print("Welcome to the Number Guessing Game")
def game():
    print("i am thinking of number between 1 to 100")
    answer= random.randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess.\n"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("you 've run out of turn, you loose")
            return
        else:
            print("Guess again")
game()





#Function to set difficulty


# Let the user Gues the Number
#Function to check user guess against actual number
# Track the number of turn and reduce it to 1