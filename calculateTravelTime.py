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
    travelTimes= []

    mph= 20
    while(mph <= 90):
        timeMin= distance // mph
        timeSec= distance % mph
        timeTot= str(timeMin)+ ":"+ str(timeSec)

        speedTime= (mph, timeTot)
        travelTimes.append(speedTime)

        mph+= 5

    return travelTimes