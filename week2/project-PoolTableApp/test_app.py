import unittest
import datetime
import functions as f


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = f.Table('table 1')

    def test_status(self):
            self.assertEqual("UNOCCUPIED", self.table.status)

unittest.main()