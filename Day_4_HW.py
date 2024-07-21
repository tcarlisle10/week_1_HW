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
                                                        #  Hope you know your pokemon Travis :)
while pokemon:
    pokemon = input("Which pokemon is this?")
    print(pokemon)
    count += 1
    if count == 5:
        print("No more Pokemon")
        print("That's", count, "Pokemon!")
        break
    