'''
A tester class to run the necessary classes
Author: Ri
'''

from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage

"""
Ford F150 (Truck)	Ford, USA	F150	2020–2022	not dually, mpg 20
Honda Civic LX (Sedan)	Honda, Japan	Civic	1996–1998	mpg 28
BMW M3 Limited (Sedan)	BMW, Germany	M3 Limited	2015–2018	mpg 30
Toyota Tundra (Truck)	Toyota, Japan	Tundra	1987–1988	dually, mpg 30
"""

def main():
   
   # trucks
   f150 = Truck(Manufacturer("Ford", "USA"),
                AutoModel("F150", True, list(range(2020, 2022))), 
                20.0)
   
   tundra = Truck(Manufacturer("Toyota", "Japan"),
                AutoModel("Tundra", False, list(range(1987, 1988))), 
                30.0, 
                is_dually=True)
   
   # sedan
   civic = Sedan(Manufacturer("Honda", "Japan"),
                AutoModel("Civic", False, list(range(1996, 1998))), 
                28.0)
   
   m3 = Sedan(Manufacturer("BMW", "Germany"),
                AutoModel("M3 Limited", False, list(range(2015, 2018))), 
                28.0)
   
   g = Garage() # empty list is initiated
   g.add_vehicle(f150)
   g.add_vehicle(civic)
   g.add_vehicle(m3)
   g.add_vehicle(tundra)

   print("Before sorting:")
   print(g)
   print()

   g.sort_by_release_year()

   print("After sorting:")
   print(g)
     

if __name__ == "__main__":
    main()

