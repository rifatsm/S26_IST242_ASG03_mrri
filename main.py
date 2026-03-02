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
            AutoModel("Civic", False, []),
            28,
        )
   print(s)
    

if __name__ == "__main__":
    main()