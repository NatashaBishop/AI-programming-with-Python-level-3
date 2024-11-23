#desision making on points based on user entry
points=int(input('WHat is your points\' balance? '))
                 
if points<=50 and points>=1:
    print('You hVE WON a wooden rabbit')
elif points<=150 and points>51:
    print('You hVE WON nothing')
elif points<=200 and points>150:
    print('You hVE WON a concert ticket')
