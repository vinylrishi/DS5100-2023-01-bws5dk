import pandas as pd
import numpy as np
class BookLover:
    # Initializer
    def __init__(self, name, email, fav_genre, num_books = None, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0 if num_books is None else num_books
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []}) if book_list is None else book_list

        
    def add_book(self, book_name, rating):
        if (book_name in set(self.book_list['book_name'])) == True:
            print('This book already exists in the book list. Try a new book.')
            return False
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1


    def has_read(self, book_name):
        return book_name in set(self.book_list['book_name'])
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]