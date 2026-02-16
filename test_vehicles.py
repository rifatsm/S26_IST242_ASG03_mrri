'''
This is the unit testing file.
Author: Ri

Run the script using: 
    pytest -v
'''

import pytest

from manufacturer import Manufacturer

class TestManufacturer: 
    def test_constructor(self):
        m = Manufacturer("Ford", "USA")
        assert m.get_name == "Ford"
        assert m.get_country == "USA"
