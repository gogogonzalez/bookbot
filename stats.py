# get book text function
# accepts filepath as input and returns contents of file as a string

def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

# get word count function
# accepts text from book as a string and returns number of words in string

def get_word_count(file_path):
    
    book_text = get_book_text(file_path)
    words = book_text.split()
    num_words = len(words)

    return num_words

# get character count function
# accepts text from book as a string and returns number of times each character (incl symbols and spaces) appears

def get_character_count(file_path):
    
    character_count = {}

    book_text = get_book_text(file_path)
    low_book_text = book_text.lower()

    for character in low_book_text:

        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

# sort character count function
# accepts character dictionary and returns a sorted list (greatest to least) of character count

def sort_character_count():
    # blah
    return