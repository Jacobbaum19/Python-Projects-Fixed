from art import logo
import random
from replit import clear

# Collections of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Starting bank amount
users_bank = 1000

def deal_card():
    """Logic function that deals cards"""
    card = random.choice(cards)
    return card

def betting(users_bank):
    """Betting function. Takes the input the users bets. If they have enough, the game will continue; otherwise, the function will keep running."""
    while True:
        # Get the bet amount from the user
        bet_amount = int(input("How much would you like to bet?: (Please only whole numbers) "))
        # Check if the bet amount is valid
        if bet_amount <= 0:
            print("Please enter a valid bet amount.")
        # Check if the user has enough money in their bank
        elif bet_amount > users_bank:
            print("You don't have enough money in your bank to place this bet.")
            print(f"Your current bank amount is: ${users_bank}")
        else:
            print(f"You have placed a bet of ${bet_amount}. Good luck!")
            return bet_amount  # Return the bet amount after validation

def calculate_score(cards):
    """Takes a list of all the cards in the deck and sums them. Checks for Blackjack and if an Ace is in the hand. If it is over 21, the card is removed and replaced with one."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)  # Ensure a score is always returned

def play_game():
    """Main logic of the game that prints the logo, resets cards and starts the game."""
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []

    # Asks user to place a bet.
    bet_amount = betting(users_bank)

    for _ in range(2):
        """Deals out players and computers cards initially."""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
      """While the game is not over, scores are calucated and shown. One of computer's cards is shown."""
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
  
      print(f"Your cards are: {user_cards}, current score is: {user_score}")
      print(f"Computer's first card is {computer_cards[0]}")
  
      if user_score == 0 or computer_score == 0 or user_score > 21:
          is_game_over = True
      else:
          should_deal = input("Type 'y' to draw another card or 'n' to stay: ")
          if should_deal == "y":
              user_cards.append(deal_card())
          else:
              is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards are: {user_cards}, final score is: {user_score}")
    print(f"Computer's final hand is {computer_cards}, with a final score of {computer_score}")
    print(compare(user_score, computer_score, bet_amount))

def compare(user_score, computer_score, bet_amount):
  """Function that compares the computer score and the user score. Also takes in the parameter bet_amount to print the user's bet amount."""
  global users_bank  # Declare users_bank as a global variable
  
  if computer_score == user_score:
      users_bank -= bet_amount
      return (f"It's a draw! You lose ${bet_amount}")
  
  elif computer_score == 0:
      users_bank -= bet_amount
      return (f"You Lose ${bet_amount}")
  
  elif user_score == 0:
      users_bank += bet_amount
      return (f"You Win ${bet_amount}! You got Blackjack!")
  
  elif user_score > 21:
      users_bank -= bet_amount
      return (f"You Lose ${bet_amount}! You went over")
  
  elif computer_score > 21:
      users_bank += bet_amount
      return (f"You Win ${bet_amount}! Computer went over")
  
  elif user_score > computer_score:    
      users_bank += bet_amount
      return (f"You Win ${bet_amount}!")
  
  elif computer_score > user_score:
      users_bank -= bet_amount
      return (f"You Lose ${bet_amount}! ")
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  """Resets the game."""
  clear()
  play_game()
