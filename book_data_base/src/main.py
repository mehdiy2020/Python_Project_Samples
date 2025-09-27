# main class
# name, author, when started, when finished, reader rate, publisher, translator
# add info
# view info (who data base)
# update info
# delete info
# from typing import Union

import pprint
from prettytable import PrettyTable, MARKDOWN


class BookDatabase():
  def __init__(self):
    self.booklist = []
      
  def add_a_book_inf(self, title: str = "",
    author_s: str | list =  "",
    genre: str  = "",
    start_date: str = "",
    finish_date: str = "",
    publisher: str = "",
    edition: str = "",
    published_year: int = "",
    translator: str | list = ""):
    """User should provide string for arguments to set a dictionary as an item within a the list of database

    :param title: Title of book, defaults to ""
    :type title: str, optional
    :param author_s: Book author or authors may be provided by user! , defaults to ""
    :type author_s: str | list, optional
    :param genre: Book genre may be provided here, defaults to ""
    :type genre: str, optional
    :param start_date: A date that user starts reading this book, defaults to ""
    :type start_date: str, optional
    :param finish_date: The date that book was finished, defaults to ""
    :type finish_date: str, optional
    :param publisher: Name of a company that published this book, defaults to ""
    :type publisher: str, optional
    :param edition: The edition number of the book, defaults to ""
    :type edition: str, optional
    :param published_year: The year that book has been published!, defaults to ""
    :type published_year: int, optional
    :param translator: Name of the translator or translators of this book to English Language, defaults to ""
    :type translator: str | list , optional
    """
    
    try:
      if isinstance(author_s, str): 
        authors = []
        authors.append(author_s)
      elif isinstance(author_s, list):
        authors = author_s
    except TypeError:
      print("The author either is one person or several people in a list. Type Must be string or list!")
    
    try:
      if isinstance(translator, str): 
        translators = []
        translators.append(translator)
      elif isinstance(translator, list):
        translators = translator
    except TypeError:
      print("\n\nThe translator(s) r is one person or several people in a list. Type Must be string or list!")
    
    book_info = self.booklist.append({
      "Book Title":title,
      "Author(s)":authors,
      "Genre":genre,
      "Translator(s)": translators,
      "Publisher":publisher,
      "Start Reading": start_date,
      "Finish Reading": finish_date,
      "Edition Number": edition,
      "Published Year":published_year
    })
   
   
  
  def view_book_info_db(self, title: str):
    """IF user enter a title for a book in form of string, she/he can see the relevant data to this book

    :param title: Book title
    :type title: str
    """
    for book in self.booklist:
      if list(book.values())[0]==title:
        pprint.pprint(f"{book}")
        
  def view_whole_database(self):
    """To see the whole data base

    :return: A list of many items in form of dictionary
    :rtype: list
    """
    table = PrettyTable()
    table.field_names = ["Book Title", "Author(s)", "Genre", "Translator(s)", "Publisher", "Start Date", "Finish Date", "Edition Number", "Published Year"]
    for book in self.booklist:
      row_list = list(book.values())
      table.add_row(row_list)
    # Customization:
    table.align = "l"               # Set default alignment to left for all columns
    # table.align["Author(s)"] = "r" # Override alignment for a specific column to right
    table.sortby = "Book Title" # Sort the table based on this column
    table.reversesort = True        # Sort in descending order
    table.header_style = "upper"    # Capitalize the header names
    table.set_style(MARKDOWN) 
    
    print(table)
  
  def update_book_info(
    self, title: str, writers: str | list = None,
    genre: str = None,translator: str | list = None,
    publisher: str = None, start_date: str = None,
    finish_date: str = None, edition: str = None,
    published_year: int = None
    ):
    """Any information pieces may be modified for any reasons. User can change and update any book info within any of the list items (dictionaries).

    :param title: Updated title of book, defaults to None
    :type title: str
    :param writers: Updated book author or authors may be provided by user!, defaults to None
    :type writers: str | list, optional
    :param genre: Updated book genre may be provided here, defaults to None
    :type genre: str, optional
    :param translator: Updated name of the translator or translators of this book to English Language, defaults to None
    :type translator: str | list, optional
    :param publisher: Revised name of a company that published this book, defaults to None
    :type publisher: str, optional
    :param start_date: New starting date for reading the book, defaults to None
    :type start_date: str, optional
    :param finish_date: New date when user finishs reading of the book, defaults to None
    :type finish_date: str, optional
    :param edition: Updated book edition, defaults to None
    :type edition: str, optional
    :param published_year: Revise the year for publishing the book, defaults to None
    :type published_year: int, optional
    """
    
    
    for book in self.booklist:

      if list(book.values())[0]==title:
        try:
          if isinstance(writers, str):
            authors = []
            authors.append(writers)
          elif isinstance(writers, list):
            authors = writers
          else:
            print("\n\n Author(s) remained unchanged!")
        except TypeError:
          print("\n\n The author/writer either is one person or several people in a list. Type Must be string or list!")
    
        try:
          if isinstance(translator, str): 
            translators = []
            translators.append(translator)
          elif isinstance(translator, list):
            translators = translator
          else:
            print("\n\n Translator(s) remain(s) unchanged!")
        except TypeError:
          print("\n\n The translator(s) r is one person or several people in a list. Type Must be string or list!")
        
        if genre:
          book["Genre"] = genre
        else:
          print("\n\n Genre for this Book Stays as is!")
       
        if publisher:
          book["Publisher"] = publisher
        else:
          print("\n\n Publisher has not been updated!")
          
        if start_date:
          book["Start Reading"] = start_date
        else:
          print("\n\n Starting day of reading this book remains as is!")
        
        if finish_date:
          book["Finish Reading"] = finish_date
        else:
          print("\n\n The finishing date of reading this book has not beem changed!")
          
        if edition:
          book["Edition Number"] = edition
        else:
          print("\n\n Edition remains unchanged!")
          
        if published_year:
          book["Published Year"] = published_year
        else:
          print("\n\n Published date of the book stays as is!")
      
    
    
  def remove_book_info(self, title: str):
    """To delete one item (dictionary) within the list (database) of book by providing the book title

    :param title: Book title
    :type title: str
    """
    current_book_name = [book["Book Title"] for book in self.booklist]
    if title in current_book_name:
        self.booklist = [book for book in self.booklist if book["Book Title"] != title]
        book_name = [book["Book Title"] for book in self.booklist]
        if title not in book_name:
          print(f"\n\n The {title} has been removed from the database.\n\n ")
    else:
      print(f"\n\n This {title} does not exist in data base!\n\n")
    
        
        
        
if __name__=='__main__':
  
  book = BookDatabase()
  book.add_a_book_inf(
  "An Introduction to Statistical Learning",
  ["Gareth James", "Daniel Witten", "Trevor Hastie", "Robert Tibshirani"],
  genre="Science - Data Science",
  start_date="2024-01-01",
  finish_date="on going",
  publisher="Springer",
  edition="2nd Edition",
  published_year= 2020

  )

  book.add_a_book_inf(
  title = "FastAPI Modern Python Web Development",
  author_s="Bill Lubanovic",
  genre="Science - Data Science",
  start_date="2025-10-01",
  finish_date="on going",
  publisher="O'Reilly Media Inc.",
  edition="1st Edition",
  published_year=2022

  )

  book.add_a_book_inf(
    title="Why Nations Fail",
    author_s=["Daron Acemoglu", "James A. Robinson"],
    genre="World Policy",
    start_date="2023-12-01",
    finish_date="2025-01-31",
    publisher="Penguin Random House LLC",
    edition="1st Edition",
    published_year=2012
  )

  book.add_a_book_inf(
    title="Hands-on Machine Learning with Scikit-Learn, Keras & TensorFlow",
    author_s="Aurelien Geron",
    genre="Science - Data Science",
    start_date="2025-10-15",
    finish_date="On Going",
    publisher="O'Reilly Media Inc.",
    edition="2nd Edition",
    published_year=2019
  )

  book.view_book_info_db("Why Nations Fail")
  book.view_whole_database()
  book.remove_book_info(title="Data Science")
  book.remove_book_info(title="Hands-on Machine Learning with Scikit-Learn, Keras & TensorFlow")
  book.view_whole_database()
  book.update_book_info("Why Nations Fail", published_year=2015)
  book.view_whole_database()




# test = [{'Book_Title': 'Why Nations Fail', 'Author(s)': ['Daron Acemoglu', 'James A.Robinson'], 'Genre': 'World Policy'},{'Book_Title': 'Why1 Nations Fail', 'Author(s)': ['Daron1 Acemoglu', 'James A.Robinson'], 'Genre': 'W1orld Policy'},{'Book_Title': 'Why2 Nations Fail', 'Author(s)': ['Daron2 Acemoglu', 'James A.Robinson'], 'Genre': 'W2orld Policy'} ]
# title = "Why1 Nations Fail"

# test = [book for book in test if book["Book_Title"]!=title]  
# test
# my_list = [book["Book_Title"] for book in test]

# if title not in my_list:
#   print(f"{title} is gone")