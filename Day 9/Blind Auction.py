import art
print(art.logo)

# TODO-1: Ask the user for input
check = "yes"
bids = {}
while check == "yes":
    name = input("What is your name? : ")
    amount = int(input("What is your bid? : $ "))

# TODO-2: Save data into dictionary {name: price}
    bids[name] = amount

# TODO-3: Whether if new bids need to be added
    check = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    print("\n" * 20)

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    highest_bid_key = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            highest_bid_key = bidder
    print(f"The winner is {highest_bid_key} with a bid of $ {highest_bid}")

find_highest_bidder(bids)

#Max function usage
#dictionary = {"item1":1, "item2":2, "item3":3}
#max(dictionary, key = dictionary.get)
#prints out ->'item3'
