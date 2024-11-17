# data_item.py
class DataItem:
    def __init__(self, name, unit, value, region, time, period):
        self._name = name
        self._unit = unit
        self._value = value
        self._region = region
        self._time = time
        self._period = period

    # Getter methods
    def get_name(self):
        return self._name

    def get_unit(self):
        return self._unit

    def get_value(self):
        return self._value

    def get_region(self):
        return self._region

    def get_time(self):
        return self._time

    def get_period(self):
        return self._period

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_unit(self, unit):
        self._unit = unit

    def set_value(self, value):
        self._value = value

    def set_region(self, region):
        self._region = region

    def set_time(self, time):
        self._time = time

    def set_period(self, period):
        self._period = period

    def __repr__(self):
        return f"DataItem(name={self._name}, unit={self._unit}, value={self._value}, region={self._region}, time={self._time}, period={self._period})"
