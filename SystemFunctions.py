import Exceptions
import Hashing
import pickle
from Employee import Employee
from Reservation import Reservation
from Customer import Customer
 
def save(object):
    try:
        file = open("data", "wb+")
        pickle.dump(object, file)
        print("Done Saving")
        file.close()
    except:
        print("Save Failed")
        
def load():
    try:
        file = open("data", "rb")
        object = pickle.load(file)
        file.close()
        print("Done Loading")
        file.close()
        return object
    except:
        print("Load Failed")
        return None


def show_options_menu():
    print("\nChoose one of the following options:")
    print("1. View All rooms")
    print("2. Add new employee")
    print("3. View all employees")
    print("4. Delete employee by id")
    print("5. Make new reservation")
    print("6. View all reservations")
    print("7. Delete a reservation")
    print("8. Add new customer")
    print("9. View all customer")
    print("10. Delete customer by id")
    print("11. Sign Out")
    print("12. Exit and Save")

def print_all_rooms(rooms):
    for room in rooms:
        print(room)
    
def check_master_key(masterKey):
    signMasterKey = input("Please, enter the master key first: ")
    
    if(not Hashing.verify(signMasterKey, masterKey)):
        raise Exceptions.AccessDeniedError
    
    return True

def add_employee(employees):
    emp_name = input("Enter employee's name: ")
    emp_ssn =  int(input("Enter employee's SSN: "))
    emp_pass = input("Enter employee's password: ")
    
    fl = 0
    for employee in employees:
        if(emp_name == employee.get_name()):
            fl = 1
            break
    
    if fl == 0:
        emp_object = Employee(emp_name, emp_ssn, emp_pass)
        employees.append(emp_object)
        print("Done Adding Employee")
        return employees
    else:
        raise Exceptions.NameDuplicateError
    
    
    
def view_all_employees(employees):
    for employee in employees:
        print(employee)

def delete_employee(employees, emp_signing_id):
    empToDel = int(input("Enter employee's ID: "))
    
    if empToDel == emp_signing_id:
        raise Exceptions.SelfDeletingError
        return employees
    
    fl = 0
    for i in range(len(employees)):
        if(employees[i].get_id() == empToDel):
            fl = 1
            del employees[i]
            break
    
    if fl == 0:
        raise Exceptions.EmployeeNotFoundError 
    else:
        print("Employee deleted Successfully")
        return employees
    
def make_resrvation(data, emp_signing_id):
    customer_id = int(input("Enter customer ID: "))
    room_number = int(input("Enter room number: "))
    duration = int(input("Enter Duration: "))
    
    fl = 0
    for i in range(len(data["customers"])):
        if customer_id == data["customers"][i].get_id():
            fl = 1
            customer_obj = data["customers"][i]
            break
    if fl == 0:
        raise Exceptions.CustomerNotFoundError 
    
    fl = 0
    for i in range(len(data["rooms"])):
        if room_number == data["rooms"][i].get_num():
            fl = 1
            room_obj = data["rooms"][i]
            if room_obj.isReserved():
                raise Exceptions.RoomNotAvailableError
            break
    if fl == 0:
        raise Exceptions.RoomNotFoundError 
        
    for i in range(len(data["employees"])):
        if emp_signing_id == data["employees"][i].get_id():
            employee_obj = data["employees"][i]
            break
    
    reservation_obj = Reservation(duration, employee_obj, room_obj, customer_obj) 
    room_obj.reserve(reservation_obj)
    customer_obj.addReservation(reservation_obj)
    data["reservations"].append(reservation_obj)
    print("Reservation made Successfully")
    return data

def view_all_reservations(reservations):
    for reservation in reservations:
        print(reservation) 
        
def delete_reservation(data):
    resToDel = int(input("Enter reservation's ID: "))
    
    fl = 0
    for i in range(len(data["reservations"])):
        if(data["reservations"][i].get_id() == resToDel):
            fl = 1
            room_id = data["reservations"][i].get_room().get_num()
            
            for j in range(len(data["rooms"])):
                if data["rooms"][j].get_num() == room_id:
                    data["rooms"][j].free()
                    break
            
            del data["reservations"][i]
            break
    
    if fl == 0:
        raise Exceptions.ReservationNotFoundError  
    print("Done deleting reservation")
    return data

def add_customer(customers):
    cust_name = input("Enter customer's name: ")
    cust_ssn =  int(input("Enter customer's SSN: "))
    
    fl = 0
    for customer in customers:
        if(cust_name == customer.get_name()):
            fl = 1
            break
    
    if fl == 0:
        cust_object = Customer(cust_name, cust_ssn)
        customers.append(cust_object)
        print(cust_object)
        print("Done Adding Customer")
        return customers
    else:
        raise Exceptions.NameDuplicateError
    
def view_all_customers(customers):
    for customer in customers:
        print(customer) 

def delete_customer(customers):
    custToDel = int(input("Enter customer's ID: "))
    
    fl = 0
    for i in range(len(customers)):
        if(customers[i].get_id() == custToDel):
            fl = 1
            del customers[i]
            break
    
    if fl == 0:
        raise Exceptions.CustomerNotFoundError 
    else:
        return customers


    



        