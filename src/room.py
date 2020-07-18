# Implement a class to hold room information. This should have name and
# description attributes.
# Creating a class for room that will have individual attributes and methods
class Room:

    def __init__(self, name, direction, description):
        self.name = name
        self.direction = direction
        self.description = description


room_1 = Room('Outside', 'North', 'Outside Cave Entrance')
room_2 = Room('Foyer', 'South', 'Dim light filters in from the south. Dusty passages run north and east.')
room_3 = Room('Outside', 'North', 'Outside Cave Entrace')
room_4 = Room('Outside', 'North', 'Outside Cave Entrace')
room_5 = Room('Outside', 'North', 'Outside Cave Entrace')