from stats import get_num_words
from stats import get_symbol_num
from stats import sorting_char
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    counting = get_num_words(sys.argv[1])
    result = get_symbol_num(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {counting} total words")
    print("--------- Character Count -------")
    sorted_list = sorting_char(result)
    for sorting in sorted_list:
        if sorting["char"].isalpha():
            print(f"{sorting['char']}: {sorting['num']}")
    print("============= END ===============")
main()