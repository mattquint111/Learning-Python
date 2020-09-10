# Palindrome

word = input("Enter a word: ")

def palindrome():
    #make sure input is all lowercase
    word_lower = word.lower()
    #reverse the lowercase word
    word_reversed = word_lower[::-1]

    if word_lower == word_reversed:
        return(f"{word} is a palindrome.")
    else:
        return(f"{word} is NOT a palindrome.")

print(palindrome())