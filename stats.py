# get book text function
# accepts filepath as input and returns contents of file as a string

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

# get word count function
# accepts text from book as a string and returns number of words in string

def get_word_count(text):
    
    words_in_book = text.split()
    return len(words_in_book)

# get character count function
# accepts text from book as a string and returns number of times each character (incl symbols and spaces) appears

def get_character_count(text):
    
    character_count = {}
    low_book_text = text.lower()

    for character in low_book_text:

        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

# sort character count function
# accepts character dictionary and returns a sorted list (greatest to least) of dictionaries

def sort_key(e):
    return e["num"]

def sort_character_count(text):
    
    sorted_list = []
    character_dictionary = get_character_count(text)

    for character in character_dictionary:
        sorted_list.append({"char": character, "num": character_dictionary[character]})
        sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list


