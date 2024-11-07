class Person:
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name

    def show_attr(self):
        print(f"Id:{self.id}")
        print(f"Name:{self.name}")

class Guest(Person):
    def __init__(self, id, name,seat,allergies,confirmed) -> None:
        super().__init__(id, name)
        self.seat=seat
        self.allergies=allergies
        self.confirmed=confirmed

    def show_attr(self):
        super().show_attr()
        print(f"Seat: {self.seat}")
        print(f"allergies: {self.allergies}")
        print(f"confirmed: {self.confirmed}")
    
class Staffmember(Person):
    def __init__(self, id, name,salary) -> None:
        super().__init__(id, name)
        self.salary=salary

    def show_attr(self):
        super().show_attr()
        print(f"Salary: {self.salary}")