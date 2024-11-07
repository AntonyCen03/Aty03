from Person import Person,Guest,Staffmember
from Product import Product
from Provider import Provider
from db import old_db

class App:
    def star(self):
        self.construir_clase()

        while True:
            print("Bienvenido")
            menu=input("""1.- Ver invitados:
2.- Ver Provedores con sus productos:
3.- Confirmar asistencia de invidado:
4.- Salir
--->""")
            if menu=="1":
                print()
                for invitados in self.guest_obj:
                    invitados.show_attr()
                    print()
            elif menu=="2":
                print()
                for provedores in self.providers_obj:
                    provedores.show_attr()
                    print()
            
            elif menu=="3":
                print("\tInvitados por confirmar:")
                for invitados in self.guest_obj:
                    if invitados.confirmed==False:
                        invitados.show_attr()
                        print()
                print("\tinvitados confirmados:")
                for invitados in self.guest_obj:
                    if invitados.confirmed==True:
                        invitados.show_attr()
                        print()
                opcion=input("Ingrese el id para confirmar la asistencia: ")
                encontardo=False
                
                for invitados in self.guest_obj:
                    if int(opcion)==invitados.id and invitados.confirmed==False:
                        invitados.confirmed=True
                        encontardo=True
                    if invitados.confirmed==True:
                        print("Invitados Confirmado")
                print()
                if encontardo==False:
                    print("No encontrado")
            
            elif menu=="4":
                break

            else:
                print("Ingreso invalido")


    def construir_clase(self):
        guest_dic=old_db["Guests"]
        staff_dic=old_db["Staff"]
        providers_dic=old_db["Providers"]
        product_dic=old_db["Products"]

        self.guest_obj=[]
        self.staff_obj=[]
        self.providers_obj=[]
        self.product_obj=[]

        for guest in guest_dic:
            self.guest_obj.append(Guest(guest["id"],guest["name"],guest["seat"],guest["allergies"],guest["confirmed"]))
        
        for producto in product_dic:
            self.product_obj.append(Product(producto["id"],producto["name"],producto["quantity"],producto["price"]))

        for provedor in providers_dic:
            productos=[]
            ids_product=provedor["products"]
            for id in ids_product:
                for id_product in self.product_obj:
                    if id==id_product.id:
                        productos.append(id_product)
            self.providers_obj.append(Provider(provedor["id"],provedor["name"],productos))


