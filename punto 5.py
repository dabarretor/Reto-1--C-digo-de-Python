"""  This program receives a list of strings and returns only 
those elements that have the same characters.  """

def find_words_with_same_characters(list_strings):

    groups = {}
    # It allows you to group words according to the characters they contain.
    for word in list_strings:
        character_pattern = "".join(sorted(word))
        
        if character_pattern in groups:
            groups[character_pattern].append(word)
        else:
            groups[character_pattern] = [word]
            
    # We extract only the words that belong to a group with more than 1 element.
    result = [] 
    for words_similar in groups.values():
        # Len counts how many words are in this group.
        if len(words_similar) > 1:  
            # Extend adds all words from this group to result, one by one.
            result.extend(words_similar)  
            
    return result

if __name__ == "__main__":
    print("--- Seeker of words with the same characters ---")
    # The user is asked to enter the words.
    text_string = input("Write several words separated by spaces: ")  
    # It allows the text string to become a list of words, separated by spaces.
    words = text_string.split()    
    # The list is checked to ensure it is not empty before processing.
    if words:   
        Result = find_words_with_same_characters(words)
        print(f"\nList of words entered: {words}")
        print(f" Result of words with same characters:  {Result}")
    else:
        print("You didn't enter any words.")