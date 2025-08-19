def palindrome(): # opening function
     word= input("Give me a word, and I'll tell you if it's a palindrome or not\n") # 1. input
     reversed= word[::-1].lower() # the input variable but made it reversed
     if word.lower().replace(" ", "") == reversed.lower().replace(" ", ""): # if word equals input variable but made reversed then it's a palindrome
      print("It's a palindrome")
     else:
        print("It's not a palindrome")
     print(f"the palindrome of {word} is {reversed}.")
palindrome() # closing function