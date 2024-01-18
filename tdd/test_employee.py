from unittest import TestCase

from employeeOOp.employee import Employee
from employeeOOp.exception import InvalidWorkHour


class TestEmployee(TestCase):

    def test_calculateEmpSalary(self):
        employee = Employee()
        self.assertEqual(50, Employee.calculateEmpSalary(5))

    def test_invalidWorkHour(self):
        employee = Employee()
        with self.assertRaises(InvalidWorkHour):
            Employee.calculateEmpSalary(400)

    def test_emp_assign_department(self):
        employee = Employee()
        employee.setEmpDepartment("Coach {Sk}")
        self.assertEqual("Coach {Sk}", employee.getEmpDepartment())

    def test_empId(self):
        employee = Employee()
        employee.setId(1)
        self.assertEqual(1, employee.getId())

    def test_name(self):
        employee = Employee()
        employee.setName("emma")
        self.assertEqual("emma", employee.getName())

    def test_toString(self):
        employee = Employee()
        employee.setId(1)
        employee.setName("SK")
        employee.setEmpDepartment("Coach")
        print(employee.get_Employee_details())

