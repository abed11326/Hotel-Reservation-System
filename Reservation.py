from datetime import date

class Reservation:
    count = 0
    id = 0
    date_created = ""
    duration = 0
    room = None 
    customer = None
    employee = None 
    
    def __init__(self, duration, employee, room, customer):
        self.__date_created = str(date.today())
        Reservation.count += 1
        self.__id = Reservation.count
        self.__duration = duration
        self.__employee = employee
        self.__room = room
        self.__customer = customer
        
    def get_id(self):
        return self.__id
    
    def get_customer(self):
        return self.__customer
    
    def get_room(self):
        return self.__room
    
    def get_date(self):
        return self.__date_created
    
    def get_duration(self):
        return self.__duration
    
    def __str__(self):
        return f"id: {self.get_id()}, customer id: {self.get_customer().get_id()}, room id: {self.get_room().get_num()}, date created: {self.get_date()}, duration: {self.get_duration()}"
        
    
        

