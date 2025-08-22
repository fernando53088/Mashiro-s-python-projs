

print("Hi! How are you?\n")
user_input = input("Are you feeling good, bad or alright?\n")
    
if "good" in user_input.lower():
    print("Nice, rejoice in your good mood!")
elif "bad" in user_input.lower():
    print("That's sad to hear, well keep your spirits up you only live once!")

elif "alright" in user_input.lower():
    print("Alright? IT SHOULD BE GOOD! Yes I'm going African parent on you.")
elif "ok" in user_input.lower():
    print("Ok? IT SHOULD BE GOOD! Yes I'm going African parent on you.")
else:
    print("I don't know what you said, since I'm still lvl 1 on being a therapist. But, always remember to never stay down in despair!\n")

user_input = input(
    "What type of philosophy would you like to hear today?\n"
     "a. About God \n"
     "b. About Work ethic \n"
     "c. About courage \n"
     "d. About purpose \n"
     "Enter the letters of your choice:\n"
).lower().strip()

if user_input.lower() in ["a", "a."]:
    print("Believe in God or not, he still will love you")
elif user_input.lower() in ["b", "b."]:
    print("Keep consistency, and keep showing up to do the work\n" 
    "For this will make you discover your potential")
elif user_input.lower() in ["c","c."]:
    print("Like, Luke 11:10, 'Ask and you shall receive' For everytime you take action\n" \
    "you will receive the reaction of your actions.")
elif user_input.lower() in ["d","d."]:
    print("It's up to you. Listen to your gut\n" \
    "for your gut will create your 'current' purpose.")

else:
    print("Very funny... well if you did it that way for this question,\n" 
    "then you can do it your way, in this life.")


