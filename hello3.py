#This program says hello and asks for my name
passWrd = input('Welcome, What is the password?')
if passWrd == 'montypython':
    print ('Access Granted!')
    myName = input('What is your Name?')
    print ('It is good to meet you, ' + myName)
    print ('The length of your name is:')
    print (len(myName))
    myAge = input('What is your age? ')
    print ('You will be ' + str(int(myAge) + 1) + ' in a year')
else:
    print('Wrong Password!')
