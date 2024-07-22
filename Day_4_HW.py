# Question 1

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in range(len(days_of_week)):
    if day % 2 == 0:
        print(day, days_of_week[day])

#---------------------------------------------------------#
print('='*50)

# Question 2

while True:
    best_spiderman = input("Who is the best Spiderman?")

    if best_spiderman == "tobey maguire":
        print('You got that right!')
        break
    else:
        print("HA! nope try again")

#----------------------------------------------#
print("Let's count our pokemon")

pokemon = True
count = 0
quit = False

while pokemon:
    pokemon = input("Which pokemon is this?")
    print(pokemon)
    count += 1
    if count == 5:
        print("No more Pokemon")
        print("That's", count, "Pokemon!")
    elif pokemon == 'quit':
        count = count - 1
        print("You only have", count, "Pokemon, you can't enter the tournament")
        break
        

        
#--------------------------------------------------------------#

# Extra credit

import random
cars = ["Ford", "BMW", "Chevy", "Volkswagen", "GMC", "Toyota", "Honda", "KIA"] 

random_car = random.choice(cars)

while True:
    guesser_input = input("What car brand am I thinking?")
    
    if random_car == guesser_input:
        print('Yes! You got it')
        break
    else:
        print("Nope! That's not it. Try again")