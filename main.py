import sys
import os

def main():
  if len(sys.argv) < 2:
    raise Exception("Please pass in a relative path to the book you want to analyze") 

  book_path = sys.argv[1]
  if not os.path.isfile(book_path):
    raise Exception(f"'{book_path}' does not exist in your filesystem")

  with open(book_path) as f:
    file_contents = f.read()

    words_in_file = count_words(file_contents)

    letters_in_file = count_letters(file_contents)

    create_book_report(words_in_file, letters_in_file) 


def count_words(text):
  text_array = text.split()
  return len(text_array)

def count_letters(text):
  text = text.lower()
  letters_count = {}
  for char in text:
    if char.isalpha():
      if char in letters_count:
        letters_count[char] += 1
      else:
        letters_count[char] = 1
    
  return letters_count

def create_book_report(num_words, letters_dict):
  print("--- begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")

  letters_list = list(letters_dict)
  letters_list.sort()

  for letter in letters_list:
    print(f"The {letter} character was found {letters_dict[letter]} times")

  print("--- End report ---")

try:
  main()
except Exception as e:
  print(e)