# Get Word Count
# Input book text as one string and return number of words in string

def get_word_count(text):
    
    words_in_book = text.split()
    return len(words_in_book)


# Get Character Count
# Input book text as one string and return number count of each character (incl symbols and spaces) as dict

def get_character_count(text):
    
    character_count = {}
    lowercase_text = text.lower()

    for character in lowercase_text:

        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


# Sort Character Count feat .sort() key
# Input character count dict and return character count in a list of descending ordering

def sort_key(e):
    return e["num"]

def sort_character_count(character_dict):
    
    sorted_list = []

    for character in character_dict:
        sorted_list.append({"char": character, "num": character_dict[character]})
        sorted_list.sort(reverse=True, key=sort_key)

    return sorted_list


