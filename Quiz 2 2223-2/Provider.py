from Product import Product
class Provider:
    def __init__(self,id,name,products) -> None:
        self.id=id
        self.name=name
        self.products=products

    def show_attr(self):
        print(f"Id: {self.id}-->Name: {self.name}")
        print(f"Product: ")
        for producto in self.products:
            producto:Product
            producto.show_attr()