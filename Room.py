class Room:
    count = 0
    number = 0
    rtype = ""
    curr_res = None
    
    def __init__(self, rtype):
        self.__rtype = rtype
        Room.count += 1
        self.__number = Room.count
        self.__curr_res = None
        
    def get_num(self):
        return self.__number
    
    def get_type(self):
        return self.__rtype
    
    def get_ress(self):
        return self.__curr_res
    
    def isReserved(self):
        return self.get_ress() != None
    
    def free(self):
        self.__curr_res = None
        
    def reserve(self, ress):
        self.__curr_res = ress
    
    def __str__(self):
        return f"number: {self.get_num()}, type: {self.get_type()}, reserved: {self.isReserved()}"
    


