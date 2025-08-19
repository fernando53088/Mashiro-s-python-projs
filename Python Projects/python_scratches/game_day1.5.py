import random
low = 1 
high = 10  # scaling 1-10
guess_lives = 3 # lives
number = random.randint(low,high) # This guesses the numbers ranging that.
try:
 while guess_lives:
    guess = int(input(f"Guess a number between {low}-{high}:\n"))
   
    if guess > number:
      print("too high")
      guess_lives -= 1
    elif guess < number:
        print("too low")
        guess_lives -= 1

    elif guess == number:
        print("You guessed it right!")
    if guess_lives == 0:
        print(f"You're all out of lives! The number is {number}")
except ValueError:
    print("Read instructions asshole") 
        