import random

#config

low = 1
high = 100000
limit = 10

rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

#tell the player the outcome
    
if guess == rand:
    print("Good job buddy.")
else:
    print("You are a brick. The number was " + str(rand) + ".")
