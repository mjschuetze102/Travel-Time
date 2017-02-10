"""
Graphical User Interface for input and output values
@author Michael Schuetze
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from calculateTravelTime import *

"""
Main function for the program
Calls functions to collect user input, make calculations, and display them for the user
"""
class createWindow(Gtk.Window):

    """
    Initializes the GUI and adds all of the elements to it
    """
    def __init__(self):
        # Create a new window for the GUI
        Gtk.Window.__init__(self, title="Travel Times")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        # Grid Layout
        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        self.add(grid)


        ### Top of the Grid ###

        # Box to hold user input label and field
        userInput = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        grid.attach(userInput, 0, 0, 2, 1)

        # Label for user input
        distanceLabel = Gtk.Label()
        distanceLabel.set_label("Please Enter a Distance (mi):")
        userInput.pack_start(distanceLabel, True, True, 0)

        # Entry for user input
        distanceInput = Gtk.Entry()
        userInput.pack_start(distanceInput, True, True, 0)


        # Button for calculating data
        calculateButton = Gtk.Button(label="Calculate")
        calculateButton.connect("clicked", self.calculateButtonClicked)
        grid.attach(calculateButton, 0, 1, 2, 1)


        ### Bottom of the Grid ###

        # Data to be placed in the travelTimeChart
        speedTime_list_store = Gtk.ListStore(int, str)
        # Chart to display speeds and travel times
        travelTimeChart = Gtk.TreeView(speedTime_list_store)

        # Add columns to the chart
        for i, colTitle in enumerate(["Speed", "Travel Time"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(colTitle, renderer, text=i)

            travelTimeChart.append_column(column)

        grid.attach(travelTimeChart, 0, 2, 2, 1)


    """
    Collects the user input and sends it to be converted into speeds and times
    """
    def calculateButtonClicked(self, widget):
        travelTimes = calculateTime(self.distanceInput.get_text())
        self.changeTravelTimes(travelTimes)


    """
    Changes the chart on the GUI to the appropriate data
    @param travelTimes:tuple(int, str)- list of tuples containing speeds and times associated with those speeds
    """
    def changeTravelTimes(self, travelTimes):
        # Remove all the data from the previous list
        self.speedTime_list_store.clear()

        # Add in the new data so that it may be displayed
        for speedTime in travelTimes:
            self.speedTime_list_store.append(list(speedTime))


"""
Main function for the program
Calls the function that creates the UI
"""
def main():
    window= createWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()