# Hi reminder you're dedicating yourself with coding or you're gonna be broke. Just the facts.
# prime_numbers = [2,3,5,7,11,13,17,19,23]
# Exercise 1
'''for _ in prime_numbers: 
  print(_)'''
# Exercise 2
'''for a in prime_numbers: 
  print(a**2)'''
# Exercise 3
'''numbers = range(1,11) 
for b in numbers:

 if b %2 == 0:
    print(b," is even") # remember "print(b +" is even")" aint valid or just use f string
 else: 
  print(f'{b},is odd') '''
# Exercise 4
'''divisible_numbers = range(1,21) 
 
for c in divisible_numbers:
 if c % 2 == 0 and c % 3 == 0: # In if-elif statement prioritize the more specific statement like that has and on it.
   print(c, " is divisible by 2 and 3") 
 elif c % 2 == 0:
  print(c, " is divisible by 2")
 elif c % 3 == 0:
  print(c, " is divisible by 3")'''

# Exercise 5
'''countdown = int(input("Enter a number:"))

for d in range(countdown, -1, -1): # start stop step at it's finest.
 print(d)
 if d <= 0:
    print("We have a lift off")'''

# Exercise 6
never_quitinput = input("Type quit to exit\n")

while True:
    never_quitinput = input("Type quit to exit\n") # I don't know why but it works, sometimes it's bs.
    if "quit" in never_quitinput.lower().strip():
        break

    
   
