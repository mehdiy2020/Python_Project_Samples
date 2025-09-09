import string
from random import choices
from abc import ABC, abstractmethod
from typing import List
import nltk
from nltk.corpus import words

nltk.download('words')
english_word = words.words()



class PasswordGenerator(ABC):
  """An abstract base class that serves as blueprint for all
  the other password generator classes. It defines a common interface that all
  concerete subclasses must follow.

  :param ABC: Defines the abstract base class comes from the'abc' moudle.
  :type ABC: class
  """
  def __init__(self, name: str="name"):
    """Atribute to provide a name for owner of password.
    
    """
    self.name = name
    self.alphabet_list = [letter for letter in string.ascii_letters ]
    self.number_list = [str(num) for num in list(range(0, 10))]
    self.symbol_list = [sbl for sbl in string.punctuation]
  
  @abstractmethod
  def generate(self) -> str:
    """Under @abstractmethod decorator to enforce a consistent
    structure or define a common interface for subclasses. Here, 
    we create a dictionary of all the pissible character that are 
    required to use and to create a password
    """
    passwrod_dic = {'letter': self.alphabet_list,
    'number': self.number_list,
    'symbol': self.symbol_list,}
    return passwrod_dic
  


class RandomPasswordGenerator(PasswordGenerator):
  """This class generate a rather suphsticated random 
  password that may contain all the characters, numbers, and
  permitted symbols in python

  """
  def __init__(self, name):
    super().__init__(name)
    
  def generate(self):
    return super().generate()
  
  def random_password(
    self,
    n: int = 10,
    num_included: bool=False,
    symbo_included: bool=False,
    all_charac: bool=False
    ):
    """This method creates a random password that can be all strings,
    strings and numbers, strings and allowed symbols, or all together.    
    """
    if num_included:
      random_password = "".join(choices(self.generate()['letter'] + self.generate()['number'], k=n))
      return random_password
    elif symbo_included:
      random_password = "".join(choices(self.generate()['letter'] + self.generate()['symbol'], k=n))
      return random_password
    elif all_charac:
      random_password = "".join(choices(self.generate()['letter'] + self.generate()['symbol'] + self.generate()['number'], k=n))
      return random_password
    else:
      random_password = "".join(choices(self.generate()['letter'], k=n))
      return random_password


     
class MemorablePasswordGenerator(PasswordGenerator):
  """
  This class generates a memorable password.
  """
  def __init__(
    self,
    name,
    number_of_words: int=8,
    capitalized: bool=False
    ):
    super().__init__(name)
    self.number_of_words: int=number_of_words
    self.capitalized: bool=capitalized
    self.english_list: List[str]=choices(english_word, k=number_of_words)
    self.separators = {
      'hyphen': '-',
      'space': ' ',
      'dot': '.',
      'underscore': '_',
      'comma': ',',
      'slash': '/' 
      }
    
  def generate(self):
      return super().generate()

  def generate_password(self, separator: str='hyphen'):
    if self.capitalized:
      word_capitalized = [word.upper() for word in self.english_list]
      return self.separators[separator].join(word_capitalized)
    else:
      return self.separators[separator].join(self.english_list)
    
   

class PinCodeGenerator(PasswordGenerator):
  def __init__(self, name):
    super().__init__(name)
    
  def generate(self):
    return super().generate()
    
  def generate_password(self, length: int=4):
    return "".join(choices(self.number_list, k=length))



def test_random_password_generator():
  random_1 = RandomPasswordGenerator("Mehdi")
  password = random_1.random_password(n=20, all_charac=True)
  print(password)
  assert len(password)==20
  assert any(character in string.ascii_letters for character in password)
  assert any(num in str(list(range(10))) for num in password)
  assert any(sym in string.punctuation for sym in password)
  
def test_memorable_password_generator():
  random_2 = MemorablePasswordGenerator("Nasim", number_of_words=5, capitalized=True)
  password = random_2.generate_password(separator='underscore')
  print(password)
  assert len(password.split("_")) == 5
  assert all(word[0].isupper for word in password)
  
def test_pincode_generator():
  random_3 = PinCodeGenerator("Mike")
  password = random_3.generate_password(length=10)
  print(password)
  assert len(password)==10
  assert all(num in str(list(range(10))) for num in password)
  
def main():
  print("Testing the RansdomPasswordGenerator: ")
  test_random_password_generator()
  print("Testing MemorablePasswordGenerator: ")
  test_memorable_password_generator()
  print("Testing PincodeGenerator: ")
  test_pincode_generator()


if __name__ == '__main__':
  main()
