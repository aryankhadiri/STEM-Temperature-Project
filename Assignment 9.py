"""Assignment three: Menu Functionality  - Aryan Khadiri
"""

import sys
import math
from tkinter import*
current_unit = 0    # The global variable for the  function for the temperature. set as 0'C
UNITS = {
        0: ("Celsius", "C"),
        1: ("Fahrenheit", "F"),
        2: ("Kelvin", "K"),
    }
DAYS = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }
HOURS = {
    0: "Mid-1AM  ",
    1: "1AM-2AM  ",
    2: "2AM-3AM  ",
    3: "3AM-4AM  ",
    4: "4AM-5AM  ",
    5: "5AM-6AM  ",
    6: "6AM-7AM  ",
    7: "7AM-8AM  ",
    8: "8AM-9AM  ",
    9: "9AM-10AM ",
    10: "10AM-11AM",
    11: "11AM-NOON",
    12: "NOON-1PM ",
    13: "1PM-2PM  ",
    14: "2PM-3PM  ",
    15: "3PM-4PM  ",
    16: "4PM-5PM  ",
    17: "5PM-6PM  ",
    18: "6PM-7PM  ",
    19: "7PM-8PM  ",
    20: "8PM-9PM  ",
    21: "9PM-10PM ",
    22: "10PM-11PM",
    23: "11PM-MID ",
}


class TempDataSet:
    num_objects = 0    # Will increment if a new object is created. It increments inside init__
    num_samples_loaded = 0    # Will increment if a sample is loaded and will be used in method get_load_temp

    @property
    def name(self):
        """Getter Function"""

        return self._name_data_set

    @name.setter
    def name(self, new_name):
        """Setter Function"""

        if 3 <= len(new_name) <= 20:
            self._name_data_set = new_name
        else:
            raise ValueError

    def process_file(self, filename):
        """Reads a file in the same directory as this python file. creates an empty list of type <TempDataType>.
         Then adds each line of the file as a tuple to the list. """
        try:
            my_file = open(filename, 'r')
        except OSError:
            return False
        else:
            self._data_set = []
            for next_line in my_file:
                my_list = list(next_line.rstrip('\n').split(","))    # Using list because tuple is immutable
                if my_list[3] == "TEMP":
                    my_list[0] = int(my_list[0])    # Converting the day number from string to int
                    my_list[2] = int(my_list[2])    # Converting the sensor number from str to int
                    temp = float(my_list[1])*24
                    my_list[1] = math.floor(temp)
                    my_list[4] = float(my_list[4])    # Converting Temperature from string to float
                    my_list.remove("TEMP")
                    my_tuple = tuple(my_list)    # Then we will convert to tuple
                    self._data_set.append(my_tuple)
                    self.num_samples_loaded += 1

    def get_summary_statistic(self, active_sensors):
        """Returns the minimum, maximum and average temperature of the active sensors during the entire week"""
        found = 0
        summ = 0.0
        temp_list = []

        if self._data_set is None:
            return None
        elif len(active_sensors) == 0:
            return None
        else:
            for i in range(0, len(self._data_set)):
                if self._data_set[i][2] in active_sensors:
                    temp_list.append(self._data_set[i][3])
                    found += 1
                    summ += self._data_set[i][3]
        maximum = max(temp_list)
        minimum = min(temp_list)
        avg = summ / found
        new_tuple = (minimum, maximum, avg)
        return new_tuple

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """finds the average temperature of a certain day and time of certain active sensors"""
        found = 0
        sum = 0.0
        if self._data_set is None:
            return None
        elif len(active_sensors) == 0:
            return None
        else:
            for i in range(0, len(self._data_set)):
                if (self._data_set[i][2] in active_sensors) and (self._data_set[i][0] == day) and (
                        self._data_set[i][1] == time):
                    found += 1
                    sum += self._data_set[i][3]
        return sum/found

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        """Returns the number of samples loaded"""
        if self._data_set is None:
            return None
        else:
            return self.num_samples_loaded

    @classmethod
    def get_num_objects(self):
        """Returns the number of objects created"""
        return self.num_objects

    def __init__(self):

        self._data_set = None
        self._name_data_set = "Unnamed"
        self.num_objects += 1


def print_header():
    """Prints The Header"""

    print("STEM Center Temperature Project")
    print("Aryan Khadiri")


def print_menu():
    """prints the menu"""

    print("Main Menu")
    print("-----------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


def recursive_sort(org_list_to_sort, key=0):
    """It sorts the list by recursion and method of bubble sort"""

    list_to_sort = org_list_to_sort.copy()    # because we need to keep the original list untouched
    changed = 0    # it determines whether the list have been changed or not
    if key == 1:
        for i in range(0, len(list_to_sort)-1):
            if list_to_sort[i][1] > list_to_sort[i+1][1]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i+1]
                list_to_sort[i+1] = temp
                changed += 1

        if changed == 0:
            return list_to_sort
        return recursive_sort(list_to_sort, 1)

    for i in range(0, len(list_to_sort)-1):
        if list_to_sort[i][0] > list_to_sort[i+1][0]:
            temp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[i+1]
            list_to_sort[i+1] = temp
            changed += 1    # the list is changed

    if changed == 0:    # base case, if the changed comes out of the loops unchanged, then we stop!
        return list_to_sort

    return recursive_sort(list_to_sort)


def new_file(dataset):
    """Gets the current_set as an object and call it dataset, use the process file function of the class TempDataSet
    and gives the list which the process_file function had created a name chosen by the user. Also returns amount of
    samples loaded by the function get_loaded_temps"""
    print("Please enter the filename of the new dataset:")
    file_entered = input()
    if dataset.process_file(file_entered) is not False:
        print("Loaded ", dataset.get_loaded_temps(), "samples")
        print("Please provide a 3 to 20 character name for the dataset:")
        while True:
            entered_name = input()
            try:
                dataset.name = entered_name
                break
            except ValueError:    # Value error was raised in the name setter function if the name was not fit
                print("Name not qualified, try again:")
    else:
        print("Invalid Entry")


def choose_units():
    """Changes the unit of temperatures for the entire program. Every time this function is called,
    it changes the current_unit of temperature"""
    global current_unit

    print("Current units in", UNITS.get(current_unit)[0])

    while True:
        print("Choose units:")
        for i in UNITS:
            print(i, " - ", UNITS[i])
        print("Which Unit?")
        try:
            current_unit = int(input())
        except ValueError:
            print("*** Please enter a number ***")
        else:
            if current_unit not in UNITS:
                print("Please enter a number from the menu:")
            else:
                break


def convert_units(celsius_value=0.0, units=0.0):
    """Converts the Temperature from Celsius"""

    if units == 0:    # To Celsius (No Change)
        return round(celsius_value,2)
    elif units == 1:    # To Fahrenheit
        return round((celsius_value * 9 / 5) + 32,2)
    elif units == 2:    # To Kelvin
        return round(celsius_value + 273.15, 2)


def print_filter(sensor_list, active_sensors):
    """ Prints the list of sensors including their status"""

    for j in range(0, len(sensor_list)):
        if sensor_list[j][2] not in active_sensors:
            print(f"{sensor_list[j][0]}: {sensor_list[j][1]}")
        else:
            print(f"{sensor_list[j][0]}: {sensor_list[j][1]} [ACTIVE]")
    print()


def change_filter(sensor_list, active_sensors):
    """change the active sensors and pass on the value to the print function"""
    sensors = {}    # Dictionary
    for i in range(0, len(sensor_list)):
        sensors[sensor_list[i][0]] = sensor_list[i][2]
        working = True
    while working:
        print_filter(sensor_list, active_sensors)
        print("Type the sensor to toggle (e.g. 4201) or x to end:")
        sensor = str(input())
        valid_choices = ["4201", "4204", "4205", "4213", "4218", "Out"]    # to throw away invalid choices
        if sensor in valid_choices:
            if sensors[sensor] in active_sensors:
                active_sensors.remove(sensors[sensor])
            elif sensors[sensor] not in active_sensors:
                active_sensors.append(sensors[sensor])
        elif sensor == "x":    # to exist, I changed the working to false so the while loop won't execute
            working = False
        else:
            print("Invalid choice, please enter again:")
            print()


def print_summary_statistics(dataset, active_sensors):
    """Print minimum, maximum, and average of temperature of the active sensors in the week
    Helper function of the get summary statistics"""
    global current_unit
    print("Summary Statistics for ", dataset.name)
    print("Minimum Temperature: ", convert_units(dataset.get_summary_statistic(active_sensors)[0], current_unit),
          UNITS.get(current_unit)[1])
    print("Maximum Temperature: ", convert_units(dataset.get_summary_statistic(active_sensors)[1], current_unit),
          UNITS.get(current_unit)[1])
    print("Average Temperature: ", convert_units(dataset.get_summary_statistic(active_sensors)[2], current_unit),
          UNITS.get(current_unit)[1])


def print_temp_by_day_time(dataset, active_sensors):
    """Prints a table of temperatures by Day and hour"""
    if dataset.get_loaded_temps() is None:
        print("There is no file loaded. Redirecting to menu...")
    else:
        print("Average Temperatures for ", dataset.name)
        print ("Units are in", UNITS.get(current_unit)[0])
        for i in range(0, len(DAYS)):
            if i == 0:
                print("             ", DAYS.get(i), end="    ")
            else:
                print(DAYS.get(i), end="    ")
        print()
        for j in range(0, len(HOURS)):
            print(HOURS.get(j), end="    ")
            for f in range(0, len(DAYS)):
                try:
                    print(round(convert_units(dataset.get_avg_temperature_day_time(active_sensors, f, j),
                                              current_unit), 1), end="   ")
                except TypeError:
                    print(" ---", end="   ")
            print()


def print_histogram(dataset, active_sensors):

    print("Histogram printing function was called")


def quitting():
    """ Quits the menu"""

    print("Thank you for using the STEM Temperature project.")
    sys.exit()


def main():
    sensor_list = [("4213", "STEM Center", 0), ("4201", "Foundations Lab", 1),
                   ("4204", "CS Lab", 2), ("4218", "Workshop Room", 3),
                   ("4205", "Tiled Room", 4), ("Out", "Outside", 10)]
    active_sensors = [0, 1, 2, 3, 4, 10]
    current_set = TempDataSet()
    print_header()

    while True:    # Test the input to be an integer/ reprint the menu
        print()
        print_menu()
        print()
        print("Enter your choice:")
        try:    # if entry was integer we will move on to else
            choice = int(input())
        except ValueError:  # if input was isn't integer, prints error message
            print("Wrong Entry! You must enter only an integer. "
                  "Try Again:")
        else:    # if the entry was integer
            while choice > 7 or choice < 1:
                print("Wrong choice! The entry must be an Integer from 1-7"
                      ". Enter Again:\n")
                break
                """ important! this break will exit out of the loop if
                the input is an Integer bigger than 7 or smaller than 1
                so the next choice we enter also goes through the first 
                loop to get checked if it is a number or a character"""

            while 0 < choice < 8:
                if choice == 1:
                    new_file(current_set)
                    break
                elif choice == 2:
                    choose_units()
                    break
                elif choice == 3:
                    change_filter(recursive_sort(sensor_list), active_sensors)
                    break
                elif choice == 4:
                    if current_set.name == "Unnamed" or len(active_sensors)== 0:
                        print("Please load data file and make sure at least one sensor is active")
                    else:
                        print_summary_statistics(current_set, active_sensors)
                    break
                elif choice == 5:
                    print_temp_by_day_time(current_set, active_sensors)
                    break
                elif choice == 6:
                    print_histogram(0, 0)
                    break
                elif choice == 7:
                    quitting()
                    break
                else:
                    break


if __name__ == "__main__":
    main()
"""
STEM Center Temperature Project
Aryan Khadiri

Main Menu
-----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

Enter your choice:
1
Please enter the filename of the new dataset:
Temperatures2017-08-06.csv
Loaded  11724 samples
Please provide a 3 to 20 character name for the dataset:
Aryan's Data

Main Menu
-----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

Enter your choice:
3
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end:
4201
4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end:
4204
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end:
4205
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end:
Out
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside

Type the sensor to toggle (e.g. 4201) or x to end:
x

Main Menu
-----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

Enter your choice:
2
Current units in Celsius
Choose units:
0  -  ('Celsius', 'C')
1  -  ('Fahrenheit', 'F')
2  -  ('Kelvin', 'K')
Which Unit?
1

Main Menu
-----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

Enter your choice:
5
Average Temperatures for  Aryan's Data
Units are in Fahrenheit
              SUN    MON    TUE    WED    THU    FRI    SAT    
Mid-1AM      68.8   68.5   72.7   71.3   70.6   70.7   66.8   
1AM-2AM      69.0   68.3   72.5   71.1   70.3   70.5   66.9   
2AM-3AM      69.1   68.3   72.3   70.9   70.0   70.4   67.0   
3AM-4AM      69.2   68.1   72.2   70.8   69.8   70.3   67.0   
4AM-5AM      69.2   68.1   72.1   70.6   69.7   70.1   67.1   
5AM-6AM      69.2   68.0   72.1   70.5   69.5   70.0   67.1   
6AM-7AM      68.8   67.9   72.1   70.1   69.4   69.6   67.1   
7AM-8AM      68.1   68.1   71.8   70.0   69.5   69.2   67.1   
8AM-9AM      67.4   68.1   71.1   69.5   69.7   68.3   67.1   
9AM-10AM     67.3   69.1   71.5   69.4   70.6   67.1   67.2   
10AM-11AM    67.1   70.4   72.3   69.9   71.5   66.7   67.2   
11AM-NOON    66.9   70.9   73.2   70.4   72.2   66.6   66.6   
NOON-1PM     66.8   71.2   73.1   71.3   72.1   66.3   65.9   
1PM-2PM      66.7   71.9   73.6   72.3   71.9   66.1   65.5   
2PM-3PM      66.9   72.8   74.3   73.1   72.3   66.1   65.2   
3PM-4PM      66.7   73.3   74.7   74.0   72.7   66.1   65.0   
4PM-5PM      66.7   73.8   75.1   74.4   73.4   66.0   64.9   
5PM-6PM      66.7   74.2   75.8   74.9   74.0   66.0   64.8   
6PM-7PM      66.7   73.5   75.1   74.6   73.5   65.8   64.8   
7PM-8PM      67.2   73.3   74.0   73.4   72.5   65.7   64.8   
8PM-9PM      67.8   73.4   73.0   72.6   71.7   65.4   64.8   
9PM-10PM     68.1   73.3   72.2   71.7   71.1   65.5   64.9   
10PM-11PM    68.3   73.2   71.8   71.3   70.9   66.3   65.5   
11PM-MID     68.6   73.0   71.5   70.9   70.8   66.6   65.7   

Main Menu
-----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

Enter your choice:
7
Thank you for using the STEM Temperature project.

Process finished with exit code 0


"""
