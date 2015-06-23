class Address:
    def __init__(self ,door, street, city):
        self.door = door
        self.street = street
        self.city = city
    def display(self):
        print("Door: " , self.door)
        print("Street: " , self.street)
        print("City: " , self.city)
          
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name: " , self.name)

class Employee(Person):
    def __init__(self, name, emp_id, address):
        super().__init__(name)
        self.emp_id = emp_id
        self.address = address
    def display(self):
        super().display()
        print("Id: " , self.emp_id)
        self.address.display();
address = Address("123","Church Street", "Bangalore")
person = Employee("Suraj",1234,address)
person.display()