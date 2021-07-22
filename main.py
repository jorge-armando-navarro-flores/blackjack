

from replit import clear

def sum(cards):
  sum = 0
  for value in cards:
    sum += value
  return sum

def card():
  return random.choice(cards)

def is_blackjack(score):
  if score == 21:
    return True
  else:
    return False

def ace(score):
  if score + 11 < 22:
    return 11
  else:
    return 1

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  print(logo)
  player_cards =[card(), card()]
  if player_cards[0] == 11 and player_cards[1] == 11:
    player_cards[1] = 1
  player_score = sum(player_cards)
  computer_cards = [card(), card()]
  computer_score = sum(computer_cards)

  computer_first_card = computer_cards[0]
  should_continue = True

  if is_blackjack(computer_score):
    should_continue = False
  elif is_blackjack(player_score):
    should_continue = False
    
  while should_continue:
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer first card: {computer_first_card}")
    get_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
    if get_card == "y":
      new_card = card()
      if new_card == 11:
        new_card = ace(player_score)
      player_cards.append(new_card)
      player_score += new_card
    else:
      should_continue = False

    if player_score >= 21:
      should_continue = False


  while computer_score <= 16:
    new_computer_card  = card()
    if new_computer_card == 11:
        new_computer_card = ace(computer_score)
    computer_cards.append(new_computer_card)

    computer_score += new_computer_card

  print(f" Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  if computer_score == 21:
    print("You lose 😤")
  elif player_score == 21:
    print("You win 😃")
  elif player_score > 21:
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