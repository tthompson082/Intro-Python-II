# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = 0
        self.s_to = 0
        self.e_to = 0
        self.w_to = 0
        self.items = items
