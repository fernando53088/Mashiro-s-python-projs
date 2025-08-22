
secret_word = "Mississippi"
# print(len(secret_word)) The output of this is 11. 
guess_word_listed = ["_"] * len(secret_word) # if it says sht is
guess_word = "   ".join(guess_word_listed) # Holy sht doing exercises did, pay off.
the_input = input(f"{guess_word} Guess the word:")

while True: # Now this is where I'm fked
  the_input = input(f"{guess_word} Guess the word:")
  if "Mississippi" in the_input.lower().strip():
    break 
   