try:
 while True:
  import random
  user_input = int(input("Guess the numbers between 1-10\n"))

  if user_input <= 10:
   print(random.randint(1, 10))

  else:
   print("Read instructions carefully please") 
except ValueError:
    print("Are you illiterate?")
    