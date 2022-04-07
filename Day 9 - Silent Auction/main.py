from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
flag = 0

def auction(record_bid):
  highest_bid = 0
  bidlist = ""
  for bidding in record_bid:
    current_bid = record_bid[bidding]
    if current_bid > highest_bid:
      highest_bid = current_bid
      bidlist = bidding
  print(f"The winner is {bidlist} with ${highest_bid}")

while flag == 0:
  name = input("What is your name? ")
  price = int(input("What is your price? $"))
  bids[name] = price
  other_players = input("Are there any other bidders? Y or N\n")
  if other_players == "N":
    flag += 1
    auction(bids)
  else:
    clear()