# Displays the time for every 15 minute interval from 12:00 am to 11:45 pm

hours = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
minutes = ['00', '15', '30', '45']   # interval = 15 Mins

for meridiem in ['am', 'pm']:
    for i in range(len(hours)): # am cycle
        for j in range(len(minutes)):
            print(hours[i] + ':' + minutes[j] + ' ' + meridiem)


