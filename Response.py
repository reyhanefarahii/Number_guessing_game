import random
name = (input('what is your name? '))
computer = '0'
user = '1'
print('hello, ' + str(name))
print('Do you like to choose the number yourself or the computer?')
gameMode=input('You = 1, computer = 0: ')
if gameMode == computer:
    rand = random.randrange(1, 50)
    response=int(input('guess, what is number between 1 or 50?'))

    while rand != response:
        if response >= rand:
          print('the answer is lower ' + str(response))
        else:
          print('the answer is bigger ' + str(response))
        response = int(input('no, try it:'))
    else:
        print('good job ' + str(name) + ', correct!')
elif gameMode == user:
    lower_bound= 1
    bigger_bound=50
    correct = 'Y'
    bigger = 'B'
    lower = 'L'
    rand = random.randint(lower_bound, bigger_bound)
    print('Choose a number between 1 and 50 in your mind')
    print('if correct: Y, bigger: B and lower: L enter please.')
    mind = input('is the number ' + str(rand) + ' ?')
    while mind != correct:
        if mind != bigger and mind != correct and mind != lower:
            print('are you kidding me !? enter if correct: Y, bigger: B and lower: L please!')
        elif mind == bigger:
            lower_bound = rand+1
            try:
                rand = random.randint(lower_bound , bigger_bound)
            except:
                print('again! please Chose a number between 1 and 50 in your mind!')
                lower_bound=1
                bigger_bound=50
        elif mind == lower:
            bigger_bound=rand-1
            try:
                rand = random.randint(lower_bound, bigger_bound)
            except:
                print('again! please Chose a number between 1 and 50 in your mind!')
                lower_bound=1
                bigger_bound=50
        mind = input('is the number ' + str(rand) + ' ?')
    else:
        print('Wow, im succeeded')
else:
    print('We do not have this game! 1 or 0?')