import random

#config

low = 1
high = 100000
limit = 10

#helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number")
            
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            return False

        print("I don't understand. Answer 'y' or 'n'.")
        

again = True

while again:
    #start game
    rand = random.randint(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

    guess = -1, 
    tries = 0
            
    #play the game nerd
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

    again = play_again()
