import random 
number=random.randint(1,9)
chances=0
while chances<5:
    guess=int(input('enter a guess'))
    if guess==number:
        print('its correct')
    else:
        print('its wrong')
    chances=chances+1

if not chances<5:
    print('you lose') 

        

        
