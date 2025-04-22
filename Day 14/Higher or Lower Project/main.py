#Display art
from art import logo ,vs
from game_data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country= account["country"]
    return f"{account_name},a{account_desc},from {account_country}"

def check_answer(user_guess,a_followers,b_followers):
    """Take a user guess and followers count of a and b and return if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True
# set random data from dictionary game_data
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")


    # ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': \n").lower()
    print("\n" *20)
    print(logo)


    #check if user is correct.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score +=1
        print(f"You 're right! Current score {score}.")
    else:
        print(f"Sorry,You're wrong! Final score {score}. ")
        game_should_continue = False
## use if account to check if user is correct

# give user a feedback on their guess
#score keeping
# make game repeatable
#making account at account at position B to position A