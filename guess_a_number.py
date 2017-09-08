import random

#config

low = 1
high = 100000000000000000000000

rand = random.randrange(1,100)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1

while guess != rand:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

print("Game over")
