import random
import os
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 21
  if 11 in hand and sum(hand) > 21:
    index = hand.index(11)
    hand[index] = 1
    # hand.remove(11)
    # hand.append(1)
  return sum(hand)

def deal_card():
  card = random.choice(cards)
  return card
  
def compare(user_score, computer_score):
  if user_score == computer_score:
    print("Draw!")
  elif computer_score == 21:
    print("Lose, Opponent has a BlackJack!")
  elif user_score == 21:
    print("Win with a BlackJack!")
  elif user_score > 21:
    print("You went over! Lose!")
  elif computer_score > 21:
    print("Opponent went over! Win!")
  elif user_score > computer_score:
    print("Win!")
  else:
    print("Lose!")
    
def play_game():
  print(logo)

  draw_card = True
  
  user_hand = random.choices(cards, k = 2)
  computer_hand = random.choices(cards, k = 2)
  while draw_card:
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
  
    print(f"    Your cards: {user_hand}, Current score: {user_score}")
    print(f"    Computer's first card: {computer_hand[0]}")
    if user_score == 21 or computer_score == 21 or user_score > 21:
      draw_card = False
    else:
      get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if get_another_card == 'n':
        draw_card = False
      elif get_another_card == 'y':
        user_hand.append(deal_card())
      
    
  while computer_score != 0 and computer_score < 17:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)
  
  print(f"    Computer's final hand: {computer_hand}, computer score: {computer_score}.")
  compare(user_score, computer_score)
  
while input("Do you wanna play a game of BlackJack? Type 'y' or 'n': ") == 'y':
  os.system('cls')
  play_game()