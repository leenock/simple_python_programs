
while True:
    try:
        number_of_cookies = int(input('\nKindly would you enter the number of cookies you would you like to bake:'))
    except ValueError:
        print("Sorry, You have not entered anything.")
        continue
    
    if number_of_cookies < 0:
        print("Sorry, your response must not be negative number.")
        continue
    else:
        break

if number_of_cookies >= 0:
    
    cups_of_sugar = 1.5
    cups_of_butter = 1
    cups_of_flour = 2.75
    produced_cookies = 48


    cups_sugar_needed = (cups_of_sugar * number_of_cookies)/produced_cookies
    cups_of_butter_needed = (cups_of_butter * number_of_cookies) /produced_cookies
    cups_of_flour_needed = (cups_of_flour * number_of_cookies) /produced_cookies



    print('\nNumber of cookies the user wants to bake =', number_of_cookies, end='\n\n')
    print('The number of cups of sugar needed for',number_of_cookies,'cookies is:',round(cups_sugar_needed,2),
      '\n The number of cups of butter needed ',number_of_cookies,'cookies is:',round(cups_of_butter_needed,2),
      '\n The number of cups of flour needed ',number_of_cookies,'cookies is:',round(cups_of_flour_needed,2))


