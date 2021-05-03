class Terminal:
    def __init__(self, type, value, priority=0):
        self.type = type
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.type}, {self.value})"

    def get_type(self):
        return self.type

    def get_priotiry(self):
        return self.priority

    def get_value(self):
        return self.value