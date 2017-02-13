"""
Model for the Travel Time project
Calculates time to travel a certain distance as well as price for gas of the trip
@author Michael Schuetze
"""

"""
Runs the calculations required to display the chart on the user interface
@param distance:String - the distance (mi) being traveled
@param price:String - the price of gas
@return a list of tuples carrying various speeds, times, and costs to complete the given distance
"""
def runCalculations(distance, price=1):
    # Convert distance and price to float
    distance = float(distance)
    price = float(price)

    # List that will hold the tuple (speed, time, tripCost, moneyLost))
    travelData = []

    # Loop through the speeds from 20 mph to 90 mph
    mph = 20
    while (mph <= 90):
        # Calculate the time it will take to reach destination
        timeTot = calculateTime(mph, distance)

        # Calculate the fuel efficiency of an average car at the given speed
        fuelEff = calculateFuelEfficiency(mph)

        # Calculate the cost of the trip for an average car based on the given gas price
        tripCost = str(calculateCostOfTrip(distance, price, fuelEff))

        # Calculate the money wasted by traveling at a less fuel efficient speed
        moneyLost = str(calculateMoneyLost(distance, price, fuelEff))

        if tripCost[-3] != ".":
            tripCost = tripCost + "0"

        if moneyLost[-3] != ".":
            moneyLost = moneyLost + "0"

        # Create and append the tuple (speed, time, tripCost, moneyLost) to the list
        speedTimeCostLoss = (mph, timeTot, tripCost, moneyLost)
        travelData.append(speedTimeCostLoss)

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
Computes the fuel efficiency of the car
@param speed:int - the speed at which the car is traveling
@return float representing the miles per gallon the average vehicle gets at a given speed

Most efficient speed to travel at is between 50 and 55 mpg
Equation created from this graph: http://www.mpgforspeed.com/fegov_graph.gif
"""
def calculateFuelEfficiency(speed):
    # Shift the graph over so the high point is at 50 mpg
    speed= speed - 3.683
    return -0.000000001066 * pow(speed, 6) + 0.0000003738 * pow(speed, 5) - 0.000050025 * pow(speed, 4) + \
           0.0032957 * pow(speed, 3) - 0.12182 * pow(speed, 2) + 2.719 * speed - 0.22814


"""
Computes the amount of money it would cost to buy gas for the trip
@param distance:float - the distance (mi) being traveled
@param price:float - the price of gas
@param fuelEff:float - the miles per gallon the average vehicle gets at a given speed
@return the time to complete the given distance
"""
def calculateCostOfTrip(distance, price, fuelEff):
    return float( int((distance / fuelEff * price) * 100) / 100)


"""
Computes the amount of gas being wasted in dollars
@param distance:float - the distance (mi) being traveled
@param price:float - the price of gas
@param fuelEff:float - the miles per gallon the average vehicle gets at a given speed
@return float representing the amount of money lost by traveling at a less effective speed
"""
def calculateMoneyLost(distance, price, fuelEff):
    return float( int(((distance / fuelEff * price) - (distance / calculateFuelEfficiency(50) * price)) * 100) / 100)