""" This program checks if a word is a palindrome or not.
A palindrome is a word that reads the same backward as forward,
ignoring spaces and accents."""

def is_palindrome(word):
    # It allows you to remove spaces if the word contains them.
    palindrome = word.lower().replace(" ", "")
    left_index = 0
    # Returns the text string to a number to recognize the last position.
    right_index = len(palindrome) - 1

    while left_index < right_index:
        # If the position of the letters is different, it is not a palindrome.
        if palindrome[left_index] != palindrome[right_index]:
            return False
        left_index += 1 # Increases the position if the letters are the same.
        right_index -= 1 # Decreases the position if the letters are the same.

    return True


word = str(input("write a word: "))

if is_palindrome(word):
    print(f"The word is a palindrome: {word}")
else:
    print(f"The word is not a palindrome: {word}")
