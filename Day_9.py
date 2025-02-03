# TODO-1: Ask the user for input
import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = int(bidding_dictionary[bidder])  # Convert input to integer
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

# TODO-2: Save data into dictionary {name: price}
bids = {}

# TODO-3: Whether if new bids need to be added
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your price? "))  # Ensure price is an integer
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)  # Clears the screen

