import os


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


bids = {}  #creating an empty dictionary to store te name as key and the amount as the value inside it
bidding_finished = False # this is to loop the process untill no other perwson is there to bid

def find_highest_bidder(bidding_record):  # this is to iterate through the values of the bidding and finding the highest value 
  highest_bid = 0 # to compare the highest value
  winner = "" #empty string to store the name of the winner later kin the program
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price # here the dictionary names bids store the name as key and price as the value 
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True # loop breaks
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('cls') # the previous output on screen gets clear (it doesn't mean that the data has been cleared from the dictionary)
