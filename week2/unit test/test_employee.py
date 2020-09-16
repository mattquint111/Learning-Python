import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.new_employee = Employee('John','Doe',10_000)

    def test_give_default_raise(self):
        self.new_employee.give_raise()
        self.assertEqual(15_000, self.new_employee.annual_salary)

    def test_give_custom_raise(self):
        self.new_employee.give_raise(10_000)
        self.assertEqual(20_000, self.new_employee.annual_salary)

if __name__ == '__main__':
    unittest.main()

    