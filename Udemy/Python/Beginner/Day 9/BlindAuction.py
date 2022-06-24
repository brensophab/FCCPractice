from operator import index
from time import sleep
from AuctionArt import logo

# function that mimics ctrl + L to clear terminal
def clear():
    
    print('\n' * 100)
    print('\033[2J\033[1;1H', end='')
    
bid_list = {
    "names": [],
    "bids" : []
    }
print(logo)
print("Welcome to the Silent Auction!")
def add_info():
    name = input("What is your name?\n")
    bid = int(input("What is your bid? \n$"))
    bid_list["names"].append(name)
    bid_list["bids"].append(bid)

    


add_info()

another_bidder = input("Is there another bidder?\n")
while another_bidder == 'yes'.lower():
    clear()
    add_info()

    another_bidder = input("Is there another bidder?\n")
else:
    max_bid = max(bid_list["bids"])
    max_bidder = bid_list["names"][bid_list["bids"].index(max_bid)] #The name of the max bidder is the index of the max bid in the bid_list["bids"] list.
    

    
    
print(f"The maximum bid is ${max_bid} which belongs to {max_bidder}!")
    # print(bid_list)
    # print(f"The top bid is a value of {bid_list['bids'][0]}")