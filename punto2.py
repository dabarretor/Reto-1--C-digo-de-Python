""" This program checks if a word is a palindrome or not. 
A palindrome is a word that reads the same backward as forward,
ignoring spaces and accents."""

palindrome = str(input("write a word: "))
# It allows you to remove spaces if the word contains them.
palindrome = palindrome.lower().replace(" ", "")
i = 0
# Returns the text string to a number to recognize the last position.
j = len(palindrome) - 1 

while i < j:
    # If the position of the letters is different, it is not a palindrome.
    if palindrome[i] != palindrome[j]: 
        print(f"The word is not a palindrome: {palindrome}")
        break
    i += 1 # Increases the position if the letters are the same.
    j -= 1 # Decreases the position if the letters are the same.
else:
    print(f"The word is a palindrome: {palindrome}")
