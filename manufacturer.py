'''
This represents a vehicle manufacturer. 
'''

class Manufacturer:
    # constructor
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country
        

    # getters 
    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_country(self) -> str:
        return self._country

    def print_me(self):
        print("Hello Manufacturer")