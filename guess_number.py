import simplegui
import random
import math


# initialize global variables used in your code here
num_range = 100
secret_num = 0
num_guess = 0
print "New game - the computer thought of a number."

# helper function to start and restart the game
def new_game():
    global num_range
    global secret_num
    global num_guess

    secret_num = random.randrange(0, num_range)

    if num_range == 100 :
        num_guess = 7
    elif num_range == 1000 :
        num_guess = 10


    print "New game. The range is from 0 to", num_range, "."
    print "You have ", num_guess,  " guesses left."
    print




# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    global num_guess
    global secret_num

    won = False

    print "You chose: ", guess
    num_guess = num_guess - 1
    print "You have ", num_guess, " guesses left."

    if int(guess) == secret_num:
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"


    if won:
        print "Correct"
        print
        new_game()
        return

    elif num_guess == 0:
        print "You have no guesses left."
        new_game()
        return

    else:
        print result

# create frame
# register event handlers for control elements and start frame

frame = simplegui.create_frame("Guess", 200, 200)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)





# call new_game
new_game()
frame.start()

#input_guess("50")
#input_guess("75")
#input_guess("62")
#input_guess("68")
#input_guess("71")
#input_guess("73")
#input_guess("74")
