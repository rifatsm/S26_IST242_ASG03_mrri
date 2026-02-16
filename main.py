'''
A tester class to run the necessary classes
Author: Ri
'''

from manufacturer import Manufacturer

def main():
    # print("Hello World")
    # Manufacturer.print_me()
    m = Manufacturer("Ford", "USA")
    # m.print_me()
    # print(m._name) # DO NOT access private variable
    print(m.get_name)
    print(m.get_country)
    pass

if __name__ == "__main__":
    main()