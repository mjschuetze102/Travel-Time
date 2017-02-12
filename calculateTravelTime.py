"""
Model for the Travel Time project
Calculates time to travel a certain distance as well as price for gas of the trip
@author Michael Schuetze
"""

"""
Runs the calculations required to display the chart on the user interface
@param distance:String - the distance (mi) being traveled
@param price:String - the price of gas
@return a list of tuples carrying various speeds and times to complete the given distance
"""
def runCalculations(distance, price=1):
    # Convert distance and price to float
    distance = float(distance)
    price = float(price)

    # List that will hold the tuple (speed, time, cost, moneyLost)
    travelData = []

    # Loop through the speeds from 20 mph to 90 mph
    mph = 20
    while (mph <= 90):
        # Calculate the time it will take to reach destination
        timeTot = calculateTime(mph, distance)

        # Create and append the tuple (speed, time) to the list
        speedTime = (mph, timeTot)
        travelData.append(speedTime)

        # Increment the speed
        mph += 5

    return travelData


"""
Computes the amount of time it would take to travel the distance at various speeds
@param distance:float - the distance (mi) being traveled
@return the time to complete the given distance
"""
def calculateTime(speed, distance):
    # Solve for the amount of hours and minutes it will take to travel the distance
    timeHour = int(distance // speed)
    timeMin = int(((distance / speed) - timeHour) * 60)

    # If the minute value is less than 10, put a 0 in front to make it line up
    # Ex 1 hr 3 min will read 1:03 instead of 1:3
    if timeMin < 10:
        timeMin = str(0) + str(timeMin)

    # Combine the hours and minutes together into HR:MIN format
    timeTot = str(timeHour) + ":" + str(timeMin)

    return timeTot


"""
Computes the fuel efficiency of the car at various speeds and displays
    the amount of gas being wasted in dollars
@param speed:int - the speed at which the car is traveling
@param distance:float - the distance (mi) being traveled
@param price:float - the price of gas
@return float representing the amount of money lost by traveling at a less effective speed
"""
def calculateMoneyLost(speed, distance, price):
    pass