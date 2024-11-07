from Package import Package
class Dispatcher_company:
    def __init__(self,id,name,packages) -> None:
        self.id=id
        self.name=name
        self.package=packages
    
    def show_attr(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.name}")
        print(f"Paquetes: ")
        for package in self.package:
            package:Package
            package.show_attr()