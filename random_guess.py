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

computer_score = 0
user_score = 0

while True:
    guess = input("Make a guess!!: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter number next time")
        continue
    if guess==random_number:
        print("You guess it right!!!")
        user_score+=1
    else:
        print("You are wrong!!!")
        computer_score+=1
    
    exit = input("Enter E to exit or any other key to continue: ").lower()
    if exit=='e':
        break

print("----------FINAL RESULT----------")
print("USER SCORE = ",user_score)
print("COMPUTER SCORE = ",computer_score)
if user_score > computer_score:
    print("YOU WON!!!")
elif user_score < computer_score:
    print("COMPUTER WON!!!")
else:
    print("MATCH DRAW!!!")