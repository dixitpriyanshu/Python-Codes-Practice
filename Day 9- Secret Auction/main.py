from art import logo
from replit import clear
print(logo)

auction_candidates ={}

def find_highest_bidder(bidding_record):
    highets_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highets_bid:
            highets_bid=bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highets_bid}")        

print("Welcome to the secret auction program.")
continue_the_auction = True
while continue_the_auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    auction_candidates[name] = bid

    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == 'yes':
        clear()
    elif choice == 'no':
        continue_the_auction = False
        clear()
        find_highest_bidder(auction_candidates)

    