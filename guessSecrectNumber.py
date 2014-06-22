print "Please think of a number between 0 and 100!"

low = 0
high = 100
guess = (low + high)/2

print "Is your secret number " + str(guess) + "?"
ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") 

while ans != 'c': #not right answer
    if ans == 'h': #too high
        high = guess
        guess = (low + high)/2
        print "Is your secret number " + str(guess) + "?"
    elif ans == 'l': #too low
        low = guess
        guess = (low + high)/2
        print "Is your secret number " + str(guess) + "?"
    else: #unkown answer
        print "Sorry, I did not understand your input."
        print "Is your secret number " + str(guess) + "?"
        
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.") 

print "Game over. Your secret number was: " + str(guess)