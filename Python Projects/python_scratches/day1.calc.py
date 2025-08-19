while True:
 try:
     print("Homie, this is a basic calculator.")
     first_number = float(input("Give me the first number\n"))
     operator = input("Give me an operator? plus? minus? times?\n")
     second_number = float(input("Give me the second number\n"))

     if operator == "+":
      result= first_number + second_number
      print(result)
     elif operator =="-":
      result = first_number - second_number
      print(result)
     elif operator =="/":
      result = first_number / second_number
      print(result)
     elif operator =="*":
      result = first_number * second_number
      print(result)	
     elif first_number == 'exit':
       break
     elif operator == 'exit':                                                                            
      break
     elif second_number == 'exit':                                                                            
      break

     else:
      print("Put numbers asshole")
 except ValueError:
  print("Put numbers asshole")
  continue

