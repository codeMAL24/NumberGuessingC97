import random 
number1 = random.randint(1,10)
print("guess a number between 1 and 10")
chances = 0
while chances < 5:
    guess = int(input("pick a number here:     "))
    if guess == number1:
        print("congrats :) YOU WON!!")
        break
    elif guess < number1:
        print("number is to small. Try again")
    else:
        print("number is to high. Try again")
    chances += 1         
if not chances < 5:
    print("You Lose. The correct number is ",(number1))
