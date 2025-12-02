import sys
from stats import get_count_words, get_count_chars, sort_list


def get_book_text(file_path):
    content = None

    with open(file_path) as f:
        content = f.read()

    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = get_count_words(content)
    count_char = get_count_chars(content)
    liste = sort_list(count_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in liste:
        if item["name"].isalpha():
            print(f"{item['name']}: {item['num']}")
    print("============= END ===============")


main()
