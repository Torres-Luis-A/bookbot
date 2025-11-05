from stats import count_words
from stats import count_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words\n--------- Character Count -------")
    char_count = count_characters(book_text)
    for char_info in char_count:
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")
main()
