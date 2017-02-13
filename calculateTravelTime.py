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
def runCalculations(distance, price=0):
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
        tripCost = calculateCostOfTrip(distance, price, fuelEff)

        # Calculate the money wasted by traveling at a less fuel efficient speed
        moneyLost = calculateMoneyLost(distance, price, fuelEff)

        # Create and append the tuple (speed, time, tripCost, moneyLost) to the list
        speedTime = (mph, timeTot, tripCost, moneyLost)
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
Computes the fuel efficiency of the car
@param speed:int - the speed at which the car is traveling
@return float representing the miles per gallon the average vehicle gets at a given speed

Equation created from this graph: http://www.mpgforspeed.com/fegov_graph.gif
"""
def calculateFuelEfficiency(speed):
    return -0.0000016225 * pow(speed, 4) + 0.00036121 * pow(speed, 3) - 0.036312 * pow(speed, 2) + 1.6445 * speed + 3.7416


"""
Computes the amount of money it would cost to buy gas for the trip
@param distance:float - the distance (mi) being traveled
@param price:float - the price of gas
@param fuelEff:float - the miles per gallon the average vehicle gets at a given speed
@return the time to complete the given distance
"""
def calculateCostOfTrip(distance, price, fuelEff):
    return distance / fuelEff * price


"""
Computes the amount of gas being wasted in dollars
@param distance:float - the distance (mi) being traveled
@param price:float - the price of gas
@param fuelEff:float - the miles per gallon the average vehicle gets at a given speed
@return float representing the amount of money lost by traveling at a less effective speed
"""
def calculateMoneyLost(distance, price, fuelEff):
    return (distance / fuelEff * price) - (distance / calculateFuelEfficiency(50) * price)