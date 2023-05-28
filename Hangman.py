#Hangman
import random

words_list = ["DRISHYAM", "BADLA", "KOILA", "DAMINI","SHOLAY", "RANJHNAA"]
chosen_word = random.choice(words_list).lower()

blank_length = len(chosen_word)

#Test Code
print(f"The word is {chosen_word}")

display = []
for _ in range(blank_length):
    display += "_"
display_top = " ".join(display)
print(display_top)    

guess = input("Guess a letter: ").lower()

if guess in range(chosen_word):
    print("Right")


"""
chosen_word_string = "".join(chosen_word)

display = []
display_lower = "" 

for letter in chosen_word:
        display += "_"
        display_top = " ".join(display)
print(display_top)

while not chosen_word_string == display_lower:    
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            print("Right")
            letter_place = int(chosen_word.index(guess))
            display[letter_place] = guess
        else:
            print("Wrong")

display_lower = "".join(display)
print(display_lower)
"""