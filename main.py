from stats import get_word_count, get_character_count, sort_character_count
import sys


# Get Book Text
# Input book file path and return contents as a string

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


# Main
# TDL: add sys argument so BookBot is usable

def main():
     
    args = sys.argv
    
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
  
    file_path = args[1]

    book_text = get_book_text(file_path)
    num_words = get_word_count(book_text)
    num_characters = get_character_count(book_text)
    sorted_character_count = sort_character_count(num_characters)
    
    print_report(file_path, num_words, sorted_character_count)

    
# Print Report
# Output word count and character (alphabet only) count in readable report

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



# Execute program

if __name__ == "__main__":
    main()