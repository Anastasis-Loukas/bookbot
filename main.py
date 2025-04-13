from stats import count_words
from stats import count_characters
from stats import sorted_dicts

import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
   if(len(sys.argv) < 2):
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

   file = sys.argv[1]
   book_contents = get_book_text(file)
  # print(f"{count_words(book_contents)} words found in the document")
   dictionary = count_characters(book_contents)
   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   print(f"Found {count_words(book_contents)} total words")
   print("--------- Character Count -------")
   list_dict = sorted_dicts(dictionary)
   for char_dict in list_dict:
        char = char_dict["char"]
        count = char_dict["count"]
    
    # Only print alphabetical characters as specified in the assignment
        if char.isalpha():
           print(f"{char}: {count}")
   print("============= END ===============")


if __name__ == "__main__":
    main()