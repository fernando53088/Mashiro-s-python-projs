# Another reminder of, this is ur pick, for another skills to make a livelihood of. If this don't work idk wth will.
# Exercise  1
'''students = {'Mashiro': 'The oldest student', 'Alex': 'The Jerk', 'Chevy': 'The Crackhead', 'Henessy': 'The short burst'}
print(students[1])'''

# Exercise 2
'''player = {"health": 100, "mana": 50}
player1 = {"health": 80, "mana": 40}
player.update(player1)
print(player) # I see so this is the update system'''

# Exercise 3
'''fruits = {"apples": 3, "bananas": 5, "oranges": 2}
for fruit_loops in fruits:
 print(f"You have {fruits[fruit_loops]} {fruit_loops}") """That's cool. 
 looping through a dictionary gives the values (via fruits[fruit_loops])""" '''
 
 # Exercise 4
'''inventory = {}
inventory["sword"] = 1 # Key-value pair on dictionary, to add huh.
inventory["potion"] = 3
del inventory["sword"] # This is how we delete
print(inventory)'''

# Exercise 5
user_input = input("Give me a word: \n")

# Empty dictionary for the letter counter
letter_count = {}

for letter in user_input:
   if letter in letter_count:
      letter_count[letter] += 1
   else:
      letter_count[letter] = 1
print(letter_count)