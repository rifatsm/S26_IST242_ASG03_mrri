from vehicle import Vehicle

class Garage:
    """
    A garage is a place that stores a collection of vehicles
    """

    # constructor
    def __init__(self):
        """initialize an empty list"""
        self._vehicles: list[Vehicle] = []
    
    # getter
    @property
    def vehicles(self) -> list[Vehicle]:
        """returns a copy of the internal list (to protect encapsulation)"""
        return list[self._vehicles]

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """add a vehicle to the list"""
        self._vehicles.append(vehicle)

    def empty_garage(self):
        """empties the garage of all the vehicles"""
        self._vehicles.clear()
