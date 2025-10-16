age = 24
guess = 0

while guess != age:
    guess = int(input("Guess my age: "))

    if guess < age:
        print("Too low!")
    else:
        print("Too high!")
        
else: # This else corresponds to the while loop
    print("Well done! You guessed it right.")