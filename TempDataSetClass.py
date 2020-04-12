class TempDataSet():
    num_objects = 0

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
        return False

    def get_summary_statistics(self, active_sensors):
        if self._data_set is None:
            return None
        return (0,0,0)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if self._data_set is None:
            return None
        return 0

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        if self._data_set is None:
            return None
        return 0

    @classmethod
    def get_num_objects(self):
        return TempDataSet.num_objects

    def __init__(self):

        self._data_set = None
        self._name_data_set = "Unnamed"
        TempDataSet.num_objects += 1


current_set = TempDataSet()

print("First test of get_num_objects: ", end='')

if TempDataSet.get_num_objects() == 1:
    print("Success")
else:
    print("Fail")

second_set = TempDataSet()

print("Second test of get_num_objects: ", end='')

if TempDataSet.get_num_objects() == 2:
    print("Success")
else:
    print("Fail")

print("Testing get_name and set_name: ")

print("- Default Name:", end='')

if current_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("- Try setting a name too short: ", end='')

try:
    current_set.name = "to"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name too long: ", end='')

try:
    current_set.name = "supercalifragilisticexpialidocious"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name just right (Goldilocks): ", end='')


try:
    current_set.name = "New Name"
    if current_set.name == "New Name":
        print("Success")
    else:
        print("Fail")
except ValueError:
    print("Fail")

print("- Make sure we didn't touch the other object: ", end='')
if second_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("Testing get_avg_temperature_day_time: ", end='')
if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_num_temps: ", end='')
if current_set.get_num_temps(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_loaded_temps: ", end='')
if current_set.get_loaded_temps() is None:
    print("Success")
else:
    print("Fail")

print("Testing get_summary_statistics: ", end='')
if current_set.get_summary_statistics(None) is None:
    print("Success")
else:
    print("Fail")

print("Testing process_file: ", end='')
if current_set.process_file(None) is False:
    print("Success")
else:
    print("Fail")

"""----------------Sample Run-----------------
First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name: 
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success
"""
