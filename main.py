from stats import get_num_words
from stats import count_characters
from stats import report
import sys


def get_book_text(fpath) :

        with open(fpath) as f:
            
            file_contents = f.read()
            return file_contents



        

def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("too many args")
        sys.exit(1)
    else:
        book_P = sys.argv[1]

    awholebook = get_book_text(book_P)
    num_words = get_num_words( awholebook)
    num_characters = count_characters(awholebook)
#    print(f"{num_words} words found in the document")
#    print(num_characters)
    report(num_characters, book_P, awholebook)

main()
