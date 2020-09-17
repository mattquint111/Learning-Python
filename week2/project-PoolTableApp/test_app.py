# import unittest
# import datetime
# import functions as f


# class TestTable(unittest.TestCase):
#     def setUp(self):
#         self.table = f.Table('table 1')
#     # Check that inital table status = "UNOCCUPIED"
#     def test_status(self):
#         self.assertEqual("UNOCCUPIED", self.table.status)
#     # check that inital cost for table = 30 and adds another 30 for every extra hour
#     def test_calc_cost(self):
#         initial_cost = f.calc_cost(0)
#         second_hour = f.calc_cost(1)
#         self.assertEqual(initial_cost, 30)
#         self.assertEqual(second_hour, 60)

#     #

# unittest.main()
while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number")
    else:
        print(f"The number you choose is: {number}")
        break