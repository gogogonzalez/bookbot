from stats import get_word_count, get_character_count

# main function

def main():
    
    # 1st test
    # used get_book_text in conjunction with relative path to file to print the contents of book to console
    # book = get_book_text("books/frankenstein.txt")
    # print(book)

    num_word = get_word_count("books/frankenstein.txt")
    print(f"{num_word} words found in the document.")

    num_character = get_character_count("books/frankenstein.txt") 
    print(num_character)

# call main to execute program

if __name__ == "__main__":
    main()