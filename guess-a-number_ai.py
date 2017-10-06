"""
Guess A Number Game
Scott B.
"""
import random
import math

def get_low_and_high():
    print()
    low = input("Make a low value. ")
    print()
    high = input("Make a high value. ")

    return int(low), int(high)



# helper functions
def show_start_screen():
    print("____ _  _ ____ ____ ____    ____    _  _ _  _ _  _ ___  ____ ____    ____ _")
    print("| __ |  | |___ [__  [__     |__|    |\ | |  | |\/| |__] |___ |__/    |__| |")
    print("|__] |__| |___ ___] ___]    |  |    | \| |__| |  | |__] |___ |  \    |  | |")
    print()


def show_credits():
    print()
    print("This outstanding game was created by Lord and Saviour Eric")
    print(" (                 (      (                       ")
    print(" )\ )              )\ )   )\ )      )    )     (  ")
    print("(()/(    (    (   (()/(  (()/(   ( /(   (     ))\ ")
    print(" /(_))_  )\   )\   ((_))  /(_))_ )(_))  )\  '/((_) ")
    print("(_)) __|((_) ((_)  _| |  (_)) __((_)_ _((_))(_))   ")
    print("  | (_ / _ \/ _ \/ _` |    | (_ / _` | '  \() -_)  ")
    print("   \___\___/\___/\__,_|     \___\__,_|_|_|_|\___|  ")
   

def get_name():
    name = input("What is your name?")
    return name




    
def get_guess(current_low, current_high):
    guess = (current_low + current_high) // 2
    return guess


    
def pick_number(low, high, limit, name):
    print()
    input("Think of a number for the comp to guess between " + str(low) + " and " + str(high) + " please " + str(name) + "." + " I have " + str(limit) + " tries to guess. Press ENTER to continue.")
    

def check_guess(guess, aiguess, limit, name ):
    print()
    print("Was your number " + str(guess) + "?")
    print()
    playerinput = input("Guess " + str(aiguess) + " out of " + str(limit) + ". " + str(name) + " please type if it was low/high/correct.")
    playerinput = playerinput.lower()
    if playerinput == "l" or playerinput == "low":
        check = -1
        return check
    elif playerinput == "h" or playerinput == "high":
        check = 1
        return check
    elif playerinput == "correct" or playerinput == "right":
        check = 0
        return check
    else:
        print()
        print("Type high/low or correct")
        check = 2
        return check
        

    

def show_result(guess, aiguess, limit):
    if aiguess != limit + 1:
        print()
        print("I knew it your number was " + str(guess))
        print()
        print("I took a total of " + str(aiguess - 1) + " gueses.")
    else:
        print()
        print("Im an actual idiot")


    
def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n'.")

def play():

    name = get_name()
    
    current_low, current_high = get_low_and_high()
    check = -1
    aiguess = 1
    limit = math.ceil(math.log(current_high - current_low + 1 , 2 ))
    
    pick_number(current_low, current_high, limit, name)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, aiguess, limit, name)
        aiguess = aiguess + 1
        
        if aiguess != limit + 1:
            if check == -1:
                current_low = guess + 1
            elif check == 1:
                current_high = guess - 1
    
        else:
            print()
            print("I am a BrIcK")
            check = 0
            

    show_result(guess, aiguess, limit, )


# Game starts running here
show_start_screen()


playing = True

while playing:
    play()
    playing = play_again()

show_credits()


