number = 23
running = True

while running:
    guess = int(input('Enter an Integer: '))

    if guess == number:
    #new block starts here
        print('Congratulations, you guessed it.')
        running = False
    
    elif guess < number:
        print ('No, it is a little higher than that.')
    else:
        print ('No, it is a little lower than that.')
    # new block ends here

else: 
    print('The while loop is done.')
print('Done')

