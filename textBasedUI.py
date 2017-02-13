"""
Plain Text Based User Interface for input and output values
@author Michael Schuetze
"""

from calculateTravelTime import *


"""
Creates the string that is displayed when asking for a desired distance and price of gas
@return float representing the distance to be traveled, float representing the price of gas
"""
def getUserInput():
    print("=====================================================")
    distance = input("Enter desired distance (mi): ")
    price = input("Enter price for gas ($): ")

    return distance, price


"""
Creates the string that is displayed after calculating speed/time combinations
@param travelData:tuple(int, str, float, float)- list of tuples containing speeds and times/costs associated with those speeds
"""
def displayTable(travelTimes):
    print("=====================================================")
    for speedTime in travelTimes:
        # Inserts the speed and time into different strings
        speed = "{!s} mph".format(str(speedTime[0]))
        time = "{!s} Hours:Minutes".format(str(speedTime[1]))
        cost = "${!s}".format(str(speedTime[2]))
        moneyLost = "${!s}".format(str(speedTime[3]))
        # Inserts the speed and time strings into a larger string with centered wording
        print("|{:^10}|{:^22}|{:^8}|{:^8}|".format(speed, time, cost, moneyLost))
    print("=====================================================")


"""
Main function for the program
Calls functions to collect user input, make calculations, and display them for the user
"""
def main():
    distance, price = getUserInput()
    travelTimes = runCalculations(distance, price)
    displayTable(travelTimes)

if __name__ == '__main__':
    main()