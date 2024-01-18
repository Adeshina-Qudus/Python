from employeeOOp.exception import InvalidWorkHour


class Employee:
    HourlyRate = 10

    def __init__(self):
        self.__employeeId = None
        self.__employeeName = None
        self.__employeeDepartment = None

    def setEmpDepartment(self, department):
        self.__employeeDepartment = department

    @staticmethod
    def calculateEmpSalary(numbersOfHour):
        if numbersOfHour <= 0 or numbersOfHour > 200:
            raise InvalidWorkHour("invalid work hour")
        return Employee.HourlyRate * numbersOfHour

    def getEmpDepartment(self):
        return self.__employeeDepartment

    def setId(self, userId):
        self.__employeeId = userId

    def getId(self):
        return self.__employeeId

    def setName(self, empName):
        self.__employeeName = empName

    def getName(self):
        return self.__employeeName

    def __str__(self):
        return f""" 
        employeeId: {self.getId()}
        employeeName : {self.getName()}
        employeeDepartment : {self.getEmpDepartment()}
        """
    def get_Employee_details(self):
        return self.__str__()
