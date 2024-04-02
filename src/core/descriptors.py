class IntegerValue:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self._value = None

    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        value = int(value)
        #if not isinstance(value, int):
        #    raise TypeError("Value must be Integer!")
        if self.min_value is not None and value < self.min_value:
            raise TypeError(f"Value must be more than {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise TypeError(f"Value must be lower than {self.max_value}")
        self._value = value
