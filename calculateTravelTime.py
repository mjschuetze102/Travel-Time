"""
Collects data for the length of the trip and computes travel times at different speeds
@author Michael Schuetze
"""

"""
Computes the amount of time it would take to travel the distance at various speeds
@param distance- the distance (mi) being traveled
@return a list of tuples carrying various speeds and times to complete the given distance
"""
def calculateTime(distance):
    # List that will hold the tuple (speed, time)
    travelTimes= []

    # Loop through the speeds from 20 mph to 90 mph
    mph= 20
    while(mph <= 90):
        # Solve for the amount of hours and minutes it will take to travel the distance
        timeHour= int(distance // mph)
        timeMin= int(((distance / mph) - timeHour) * 60)

        # If the minute value is less than 10, put a 0 in front to make it line up
        # Ex 1 hr 3 min will read 1:03 instead of 1:3
        if timeMin < 10:
            timeMin= str(0)+ str(timeMin)

        # Combine the hours and minutes together into HR:MIN format
        timeTot= str(timeHour)+ ":"+ str(timeMin)

        # Create and append the tuple (speed, time) to the list
        speedTime= (mph, timeTot)
        travelTimes.append(speedTime)

        # Increment the speed by 5 mph
        mph+= 5

    return travelTimes