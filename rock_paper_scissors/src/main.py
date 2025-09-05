
from random import choice








def play_again():
  your_wish = input("Do you want to play again? Enter 'Yes' to continue, 'q' to quit the game: ").lower()
  return your_wish


def evaluate_game(your_hand, computer_hand):
  if your_hand == computer_hand:
    print("Game is tied")
    
  elif your_hand == 'rock' and computer_hand == 'paper':
    print('Computer Won!')
  
  elif your_hand == 'paper' and computer_hand == 'rock':
    print('You Won!')
    
  elif your_hand == 'scissors' and computer_hand == 'paper':
    print('You Won!')
    
  elif your_hand == 'paper' and computer_hand == 'scissors':
    print('Computer Won!')
    
  elif your_hand == 'scissors' and computer_hand == 'rock':
    print('Computer Won!')
  
  elif your_hand == 'rock' and computer_hand == 'scissors':
    print('You Won!')
      
   
    

  
def play_game():
  game_list = ['rock', 'paper', 'scissors']
  computer_hand = choice(game_list)
  game_on = 'yes'
  while game_on != 'q':
    try:
      your_hand = input("Enter your choice of Rock, Paper, or Scissors: ").lower()
      if isinstance(your_hand, str) and your_hand in game_list:
        evaluate_game(your_hand, computer_hand)
        game_on = play_again()
        computer_hand = choice(game_list)
      else:
        print(f"you are required to enter the correct input not {your_hand}")
    except ValueError:
      print("Please enter a string of Rock, Paper or Scissors")
    
    

  
play_game()