"""
User Interface for input and output values
@author Michael Schuetze
"""

from calculateTravelTime import *

"""
Creates the string that is displayed when asking for a desired distance
"""
def getDistance():
    print("===================================")
    distance= int(input("Enter desired distance (mi): "))

    return distance

def displayTable(travelTimes):
    print("===================================")
    for speedTime in travelTimes:
        speed= "{!s} mph".format(str(speedTime[0]))
        time= "{!s} Hours:Minutes".format(str(speedTime[1]))
        print("|{:^10}|{:^22}|".format(speed, time))
    print("===================================")

def main():
    distance= getDistance()
    travelTimes= calculateTime(distance)
    displayTable(travelTimes)

if __name__ == '__main__':
    main()