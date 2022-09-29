from Person import Person
from Reservation import Reservation

class Customer(Person):
    count = 0
    ress = []
    def __init__(self, name, SSN):
        self.__name = name
        self.__SSN = SSN
        Customer.count += 1
        self.__id = Customer.count
        self.__ress = []
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_ssn(self):
        return self.__SSN
    
    def get_ress(self):
        ress_id_list = []
        for ress in self.__ress:
            ress_id_list.append(str(ress.get_id()))
        
        return ress_id_list
    
    def __str__(self):
        return f"id: {self.get_id()}, name: {self.get_name()}, SSN: {self.get_ssn()}, reservations: {self.get_ress()}"
    
    def addReservation(self, ress):
        self.__ress.append(ress)       
    