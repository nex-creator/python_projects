# TODO-1: Ask the user for input
import art
print(art.logo)
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}.")

bid_dict = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name. \n").lower()
    price = int(input("What is your bid? $"))
    bid_dict[name] = price
    bid_or_not = input('Is there any other bid: Type "yes" or "no" \n').lower()
    if bid_or_not == "no":
        continue_bidding = False
        find_highest_bidder(bid_dict)
    elif bid_or_not == "yes":
        print("\n"*20)



