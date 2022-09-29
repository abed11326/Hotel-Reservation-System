from Person import Person
import Hashing
import Exceptions

class Employee(Person):
    password = ""
    count = 0

    def __init__(self, name, SSN, password):
        self.__name = name
        self.__SSN = SSN
        self.__password = Hashing.Hash(password)
        Employee.count += 1
        self.__id = Employee.count
        
    def get_pass(self):
        return self.__password
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_ssn(self):
        return self.__SSN
    
    def __str__(self):
        return f"id: {self.get_id()}, name: {self.get_name()}, SSN: {self.get_ssn()}, password: {self.get_pass()}"

    @staticmethod
    def signIn(employees):
        signId = int(input("Enter your ID: "))    
        signPass = input("Enter your Password: ") 
        
        fl = 0
        for employee in employees:
            if employee.get_id() == signId:
                fl = 1
                emp = employee
                break
            
        if fl == 0:
            raise Exceptions.EmployeeNotFoundError 
        else:
            if not Hashing.verify(signPass, emp.get_pass()):
                raise Exceptions.AccessDeniedError
            else:
                return signId
                
    

