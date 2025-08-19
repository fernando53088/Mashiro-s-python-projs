import random
scrambbler = input("Give me word\n") # input
letters = list(scrambbler)
random.shuffle(letters)
final_shuffle = "".join(letters) # this is the rope that strings it all together
print(final_shuffle)