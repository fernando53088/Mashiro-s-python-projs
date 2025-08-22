import random
scrambbler = input("Give me a word\n") # input 
letters = list(scrambbler) # This makes the letters of the word made in to a list
random.shuffle(letters) # Don't have to put this in a variable. if it's .choice then yeah put it in a variable.
# This shuffles the letters of the word, but it's still on a list
final_shuffle = "".join(letters) # Which is where .join comes in and is the rope that strings it all together
print(final_shuffle)