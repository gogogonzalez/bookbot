from stats import get_book_text, get_word_count, get_character_count, sort_character_count

# main function

def main():
    
    # TDL: add get text function to main,
    # clean up with clearer explanations

    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_word_count(book_text)
    num_characters = get_character_count(book_text)
    sorted_character_count = sort_character_count(book_text)

    print_report(file_path, num_words, sorted_character_count)
    

    
# print report function
# it'll make things look nice :)

def print_report(file_path, num_words, sorted_character_count):
      print("============ BOOKBOT ============", 
            f"\nAnalyzing book found at {file_path}...")
      
      print("----------- Word Count ----------", 
            f"\nFound {num_words} total words")
        
      print("--------- Character Count -------")

      for item in sorted_character_count:
            if not item["char"].isalpha():
                 continue
            print(f"{item['char']}: {item['num']}")  
      
      print("============= END ===============")





# call main to execute program

if __name__ == "__main__":
    main()