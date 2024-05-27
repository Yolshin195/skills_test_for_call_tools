import unittest
from pathlib import Path

from task_two.main import EmployeeWorkingHours, EmployeeWorkingHoursReport


class TestsEmployeeWorkingHours(unittest.TestCase):

    def test_build(self):
        employee = EmployeeWorkingHours.build("Роман 11")
        self.assertEqual("Роман", employee.employee_name)
        self.assertEqual(11, employee.total_hours)

    def test_equal(self):
        employee_one = EmployeeWorkingHours.build("Роман 11")
        employee_two = EmployeeWorkingHours.build("Роман 14")

        self.assertEqual(employee_one, employee_two)

    def test_hash(self):
        employee_one = EmployeeWorkingHours.build("Роман 11")
        employee_two = EmployeeWorkingHours.build("Роман 14")

        self.assertEqual(hash(employee_one), hash(employee_two))

    def test_open_employee_working_hours(self):
        path = Path("records_of_hours_worked_by_employees.txt")
        list_result = [employee_working_hours for employee_working_hours in EmployeeWorkingHours.open(path)]
        self.assertEqual(7, len(list_result))


class TestsEmployeeWorkingHoursReport(unittest.TestCase):
    def test_open(self):
        expected = (
            "Андрей: 9, 6; sum: 18\n"
            "Василий: 11; sum: 11\n"
            "Роман: 7, 11; sum: 14\n"
            "X Æ A-12: 45; sum: 45\n"
            "Иван Петров: 3; sum: 3"
        )
        path = Path("records_of_hours_worked_by_employees.txt")
        report = EmployeeWorkingHoursReport(path)
        report.build()
        self.assertEqual(expected, str(report))
