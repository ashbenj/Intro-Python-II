# Implement a class to hold room information. This should have name and
# description attributes.
# Creating a class for room that will have individual attributes and methods
class Room:

    def __init__(self, name, direction, description):
        self.name = name
        self.direction = direction
        self.description = description
