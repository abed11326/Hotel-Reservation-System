# import required modules
import Exceptions
import Hashing
import SystemFunctions as sf
from Employee import Employee
from Room import Room

# define a master key 
masterKey = Hashing.Hash("NagyMasterkey@123")

        
# initialize the data and pickle them
rooms = [Room("royal"), Room("presidential"), Room("presidential"), Room("suite"), Room("suite"), Room("suite"), Room("BB"), Room("BB"), Room("BB"), Room("BB")]
employees = [Employee("Nagy", 2022, "nagy123")]
customers = []
reservations = []

data = {"rooms" : rooms, "employees" : employees, "customers" : customers, "reservations" : reservations}

#sf.save(data)

# start system
system_working = 1
while(system_working):
    signIn_working = 0
    data = sf.load()
    
    while(1):
        try:
            emp_signing_id = Employee.signIn(data["employees"])
        except Exceptions.EmployeeNotFoundError:
            print("ID Not Found!")
        except Exceptions.AccessDeniedError:
            print("Wrong Password!")
        except ValueError:
            print("You should enter relevant data types!")
        else:
            signIn_working = 1
            print("Signed in successfully")
            break
    
    while(signIn_working):
        sf.show_options_menu()
        opt = int(input("Enter your option: "))
        
        if opt == 1:
            sf.print_all_rooms(data["rooms"])
        
        elif opt == 2:
            try:
                sf.check_master_key(masterKey)
            except Exceptions.AccessDeniedError:
                print("Wrong Master Key!")
            else:
                try:
                    data["employees"] = sf.add_employee(data["employees"])
                except Exceptions.NameDuplicateError:
                    print("Employee's name already taken!")
                except ValueError:
                    print("You should enter relevant data types!")
        
        elif opt == 3:
            try:
                sf.check_master_key(masterKey)
            except Exceptions.AccessDeniedError:
                print("Wrong Master Key")
            else:
                sf.view_all_employees(data["employees"])
        
        elif opt == 4:
            try:
                sf.check_master_key(masterKey)
            except Exceptions.AccessDeniedError:
                print("Wrong Master Key")
            else:
                try:
                    data["employees"] = sf.delete_employee(data["employees"], emp_signing_id)
                except Exceptions.EmployeeNotFoundError:
                    print("Employee Not Found")
                except Exceptions.SelfDeletingError:
                    print("You cannot delete yourself!")
                except ValueError:
                    print("You should enter an integer as an ID! ")
                    
                    
        elif opt == 5:
            try:
                data = sf.make_resrvation(data, emp_signing_id)
            except Exceptions.CustomerNotFoundError:
                print("Customer Not Found")
            except Exceptions.RoomNotFoundError:
                print("Room Not Found")
            except Exceptions.RoomNotAvailableError:
                print("Room already reserved")
            
            except ValueError:
                print("You should enter relevant data types!")
        
        elif opt == 6:
            sf.view_all_reservations(data["reservations"])
            
        elif opt == 7:
            try:
                sf.check_master_key(masterKey)
            except Exceptions.AccessDeniedError:
                print("Wrong Master Key")
            else:
                try:
                    data = sf.delete_reservation(data)
                except Exceptions.ReservationNotFoundError:
                    print("Reservation not found")
                except ValueError:
                    print("You should enter an integer as an ID! ")
        
        elif opt == 8:
            try:
                data["customers"] = sf.add_customer(data["customers"])
            except Exceptions.NameDuplicateError:
                print("Customer's name already taken!")
            except ValueError:
                print("You should enter relevant data types!")
                
        elif opt == 9:
            sf.view_all_customers(data["customers"])
            
        elif opt == 10:
            try:
                data["customers"] = sf.delete_customer()
            except Exceptions.CustomerNotFoundError:
                print("Customer not found!")
            except ValueError:
                print("You should enter an integer as an ID! ")
                
        elif opt == 11:
            sf.save(data)
            signIn_working = 0
            
        elif opt == 12:
            sf.save(data)
            signIn_working = 0
            system_working = 0
            
            
                

            
            
            
            
            
            
    
    



