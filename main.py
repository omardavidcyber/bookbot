def main():
  with open("./books/frankenstein") as f:
    file_contents = f.read()
    print_book_report(get_words_from_book(file_contents), get_letter_totals(file_contents))

def get_words_from_book(book):
  return len(book.split())

def get_letter_totals(book):
  letter_totals = {}
  for letter in book:
    letter = letter.lower()
    if letter in letter_totals:
      letter_totals[letter] += 1
    else:
      letter_totals[letter] = 1
  return letter_totals

def print_book_report(num_words, letter_counts):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the book\n")

  letters = []

  for k in letter_counts:
    if k.isalpha():
      letters.append((k, letter_counts[k])) # appends to list as a tuple of letter,letter_count pairs
  
  letters.sort(key=lambda letter: letter[1], reverse=True) # list sorted descending order using the letter_count as key for comparison

  for letter in letters:
    print(f"The '{letter[0]}' character was found {letter[1]} times")   

  print("\n--- End report ---")

main()