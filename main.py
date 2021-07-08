############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from replit import clear

def sum(cards):
  sum = 0
  for value in cards:
    sum += value
  return sum

def card():
  return random.choice(cards)

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  print(logo)
  player_cards =[card(), card()]
  player_score = sum(player_cards)
  computer_cards = [card(), card()]
  computer_first_card = computer_cards[0]

  should_continue = True
  while should_continue:
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer first card: {computer_first_card}")
    get_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
    if get_card == "y":
      new_card = card()
      player_cards.append(new_card)
      player_score += new_card
    else:
      should_continue = False

    if player_score > 21:
      should_continue = False


  while 21 - sum(computer_cards) >= 5:
    computer_cards.append(card())

  computer_score = sum(computer_cards)

  print(f" Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  if player_score > 21:
    print("You went over. You lose 😤")
  elif computer_score > 21:
    print("Opponent went over. You win 😁")
  elif computer_score > player_score:
    print("You lose 😤")
  elif computer_score == player_score:
    print("Draw")
  else:
    print("You win 😃")

  restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if restart == 'y':
    clear()
    blackjack()
  else:
    print("Goodbye")

blackjack()