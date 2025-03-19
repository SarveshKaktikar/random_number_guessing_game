import random

top_range = input("Enter the number for top range: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range<=0:
        print("Please enter greater than zero next time")
        quit()
else:
    print("Please enter number next time")
    quit()

random_number = random.randint(0,top_range)

guesses = 0

while True:
    guesses+=1
    guess = input("Make a guess!!: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter number next time")
        continue
    if guess==random_number:
        print("You guess it right!!!")
        break
    elif guess>random_number:
        print("You are above the number")
    else:
        print("You are below the number")
    
print("You got it in ",guesses,"guesses")


