from random import randint


def your_number_guess():
  cont = True
  while cont:
    try:
      your_guess = int(input('Pleae enter your guess here: '))
      if your_guess >= 1 and your_guess <=100:
        cont = False
        return your_guess
      else:
        your_guess = int(input('Pleae enter your guess here: '))
    except ValueError:
      print("Invalid input. PLease enter a whole number")
    
   



def enter_the_game(score: int=10, continue_game: str='yes'):
  """
  # A random number will be selected between 1 to 100 inclusively
  # Participant guess a random number between 1 to 100 inclusively
  # The score, by default 10, however can be modified by participant
  # to make the game more competitive the score shouod not be more than 20 and less than 5
  # by defualt game is not on by 'q'!
  # A dictionary of outcome will be the return of the function

"""
  number_random = randint(1, 100)
  your_guess = your_number_guess()
  if score > 20:
    score = 20
    your_remaining_score = score
  elif score < 5:
    score = 5
    your_remaining_score = score
  else:
    your_remaining_score = score
  game_is_on = continue_game
  return {
    'game_on':game_is_on,
    'participant_guess':your_guess,
    'participant_score':your_remaining_score,
    'random_number':number_random
    }






def play_guessing_game():
  
  print("You will be ask to guess a number between 1 to 100 inclusive!")
  print('First time you play, you score is from 10')
  
  game = enter_the_game()
  
  while game['game_on'] != "q":
    if game['participant_guess'] > game['random_number'] and game['participant_score'] > 0 :
      print("Hint: The actual number is less than what you guessed!")
      game['participant_score'] -=1
      print(f"Your current score is {game['participant_score']} ")
      your_new_guess = your_number_guess()
      game['participant_guess'] = your_new_guess  
    elif game['participant_guess'] < game['random_number'] and game['participant_score'] > 0:
      print("Hint: The actual number is more than what you guessed!")
      game['participant_score'] -=1
      print(f"Your current score is {game['participant_score']} ")
      your_new_guess = your_number_guess()
      game['participant_guess'] = your_new_guess  
    elif game['participant_score'] == 0:
      print(f" Your score is now {game['participant_score']}, and you must decide whether you wish to play again or not!.")
      continue_game = input("Do you want to quit the game or play agian? Enter any comments but 'q' for another game, or use 'q' to quit the game: ").lower()
      if continue_game != 'q':
        score = int(input('Please enter your maximum score here: '))
        game = enter_the_game(score=score, continue_game=continue_game)
      else:
        break
    else:
      print(f" Your quess, {game['participant_guess']}, is correct. You Won, Horrray!")
      continue_game = input("Do you want to quit the game or play agian? Enter any comments but 'q' for another game, or use 'q' to quit the game: ").lower()
      if continue_game != 'q':
        score = int(input('Please enter your maximum score here: '))
        game = enter_the_game(score=score, continue_game=continue_game)
      else:
        break
    
      

if __name__=='__main__':
  play_guessing_game()
      