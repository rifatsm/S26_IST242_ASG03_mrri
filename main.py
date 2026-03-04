'''
A tester class to run the necessary classes
Author: Ri
'''

from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan

def main():
   s = Sedan(
            Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, [2020, 2021]),
            28,
        )
   print()
   print(s.how_far_with(10)) # call concrete method
   print()    

if __name__ == "__main__":
    main()