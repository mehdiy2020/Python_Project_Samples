
from random import choice








def play_again():
  """This function assists user to re-play the game.

  :return: As long as user does not enter 'q', game will be on!
  :rtype: str
  """

  your_wish = input("Do you want to play again? Enter 'Yes' to continue, 'q' to quit the game: ").lower()
  return your_wish


def evaluate_game(your_hand, computer_hand):
  """This function evaluate whether user or computer wins the game.

  :param your_hand: What user/player chooses to play.
  :type your_hand: str
  :param computer_hand: What computer chooses to play.
  :type computer_hand: str
  """
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
  """Game will be played if user chooses this function. No argument is require
     as the start of the game.
  """
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