class Package:
    def __init__(self,id,address,delivered) -> None:
        self.id=id
        self.address=address
        self.delivered=delivered
    
    def show_attr(self):
        print(f'\tId: {self.id} - Direccion: {self.address} - ({"Entregado" if self.delivered else "Pendiente"})')
        
        