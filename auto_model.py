'''
 Represents an automodel
'''

class AutoModel: 
    def __init__(
            self, 
            name: str, 
            in_production: bool, 
            years: list[int]):
        if not years:
            raise ValueError("The years list must be not empty.")
        self._name = name
        self._in_production = in_production
        self._years = list(years) # defensive copy

    @property
    def name(self) -> str:
        return self._name

    @property
    def in_production(self) -> bool:
        return self._in_production

    @property
    def years(self) -> list[int]:
        return list(self._years) # return a copy
    
    @property
    def first_year(self) -> int:
        """
        Returns the first (earliest) production year
        """
        return self._years[0]
    
    def __str__(self) -> str:
        return f"{self._name} in production = {self._in_production},  release year: {self._years[0]}"
    
