import random
print("Enter the range of numbers to guess from: ")
min= int(input("Enter the starting point: "))
max= int(input("Enter the ending point: "))
ran = random.randint(min, max)
while True:
    number = int(input("Enter your guess: "))

    if number==ran:
        print("You have guessed right!")
        break
    elif number>ran:
        print("Guess lower")
    elif number<ran:
        print("Guess higher")
    else: 
        print("Please try again")
