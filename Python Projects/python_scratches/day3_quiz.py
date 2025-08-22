import random 
questions = [ ["What's the capital of the Philippines?", "Manila"],["The best time to plant a tree was decades ago. When's the second best time?", "Today"],
["Are you worthful?", "Yes"]] # This is list
qanda = random.choice(questions) # This randomizes the list and picks one of the blocks
print(qanda[0])
answer = input('-->')
if answer.lower().strip() == qanda[1].lower().strip(): # Don't capitalize I in if or you're screwed
 print("You're right")
else:
 print("You are wrong")