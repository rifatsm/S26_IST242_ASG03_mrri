'''
A tester class to run the necessary classes
Author: Ri
'''

from manufacturer import Manufacturer

def main():
    m = Manufacturer("Ford", "USA")
    print(m.get_name)
    print(m.get_country)
    print(m)
    pass

if __name__ == "__main__":
    main()