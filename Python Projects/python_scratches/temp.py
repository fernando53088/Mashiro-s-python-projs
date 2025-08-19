try:
    temp = float(input("What's the temperature today? (In Celsius)\n"))

    if temp <= 10.0:
       print("It's cold")
    elif 10.0 <= temp < 25.0:
         print("It's nice")
    elif 25.0 <= temp < 69.0:
        print("It's hot af")
    elif 69.0 <= temp < 3000.0:
        print("Cap.")
    elif temp >= 3000.0:
        print("Cap. Where the hell are you at? The Sun?")
 
    else:
        print("What? Please repeat") 
    
except ValueError:
    print("What? Please prompt numbers retard")          
