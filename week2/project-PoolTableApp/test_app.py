import unittest
import datetime
from functions import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table('table 1')

    def test_status(self):
            self.assertEqual("UNOCCUPIED", self.table.status)

unittest.main()