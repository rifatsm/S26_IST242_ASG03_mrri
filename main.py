'''
A tester class to run the necessary classes
Author: Ri
'''

from manufacturer import Manufacturer
from auto_model import AutoModel

def main():
    original_list = [2020, 2021]
    am = AutoModel("F150", True, original_list)

    print(am.get_years)

    original_list.clear()

    print(am.get_years)
    

if __name__ == "__main__":
    main()