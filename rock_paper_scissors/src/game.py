  
"""
:author: Mehdi Yazdanian
:date: 2025-09-06
"""


from random import choice

class RockPaperScissors:
  """A class for Rock, Paper and Scissors Game. THis class 
  contains four method and one attribute just to introduce the player
  """
  def __init__(self, player_name: str):
    self.game_list = ['rock', 'paper', 'scissors']
    self.player_name = player_name
    
  def computer_select(self):
    """This function is producing computer
    choice from game list.    
    """
    computer_hand = choice(self.game_list)
    return computer_hand
  
  def player_select(self):
    """Player can choose his/her hand for this game.
    """
    your_hand = input("Enter your choice of Rock, Paper, or Scissors: ").lower()
    if your_hand in self.game_list:
      return your_hand
    else:
      print(f"you are required to enter the correct input not {your_hand}")
      return self.player_select()
      
  def evaluate_game(self, computer_choice: str, player_choice: str):
    """Assessment to realize the winner of the game.
    :param computer_choice: A strong to demonstrate computer choice
    :type computer_choice: str
    :param player_choice: A strong to demonstrate player choice
    :type player_choice: str
    :return who is the winner: game is tied, computer or player
    """
    if player_choice == computer_choice:
      print("Game is tied")
    elif player_choice == 'rock' and computer_choice == 'paper':
      print('Computer Won!')
    elif player_choice == 'paper' and computer_choice == 'rock':
      print('You Won!')
      
    elif player_choice == 'scissors' and computer_choice == 'paper':
      print('You Won!')
      
    elif player_choice == 'paper' and computer_choice == 'scissors':
      print('Computer Won!')
      
    elif player_choice == 'scissors' and computer_choice == 'rock':
      print('Computer Won!')
    
    elif player_choice == 'rock' and computer_choice == 'scissors':
      print('You Won!')
      
  def play_again(self):
    """How the feature implemented that allows a player to continue playing or abort the game. 
    """
    your_wish = input("Do you want to play again? Enter 'Yes' to continue, 'q' to quit the game: ").lower()
    if your_wish != 'q':
      self.play_game()
    else:
      print('Game Over!')
       
 
    
      
  def play_game(self):
    computer_choice = self.computer_select()
    player_choice = self.player_select()
    print(f"Computer select {computer_choice}")
    self.evaluate_game(computer_choice, player_choice)
    self.play_again()
    
        
if __name__=='__main__':  
  game_1 = RockPaperScissors("Mehdi")
  game_1.computer_select()
  game_1.player_select()  
  game_1.play_game()