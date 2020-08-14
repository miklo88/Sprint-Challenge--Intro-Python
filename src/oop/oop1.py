# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class aka parent class
class Vehicle:
    pass
# child class
class GroundVehicle(Vehicle):
    pass
# grandkids
class Car(GroundVehicle):
    pass
# grandkids
class Motorcycle(GroundVehicle):
    pass
# child
class FlightVehicle(Vehicle):
    pass
# grandkids
class Starship(FlightVehicle):
    pass
# grandkids
class Airplane(FlightVehicle):
    pass

