from Person import Person,Client,Worker
from Dispatcher_company import Dispatcher_company
from Package import Package
from db import old_db

class App:

    def star(self):
        self.construir_clase()

        while True:
            print("Bienvenido a desparchos rapidos")
            print()
            menu=input("""Seleccionar una opcion:
1.- Ver Trabajador
2.- Ver Companias de despacho
3.- Comfirmar entrega
4.- Ver Cliente envio pendiente
5.- Salir
--->""")
            if menu=="1":
                for trabajador in self.workers_obj:
                    trabajador.show_attr()
                    print()
            elif menu=="2":
                print()
                for company in self.company_obj:
                    company.show_attr()
                    print()

            elif menu=="3":
                print()
                print("Paquetes Pendiente: ") 
                for paquete in self.packages_obj:
                    if paquete.delivered==False:
                        paquete.show_attr()
                print()
                print("Paquetes Entregado: ")        
                for paquete in self.packages_obj:
                    if paquete.delivered==True:
                        paquete.show_attr()
                        
                opcion=input("Selecciona el paquete para entregar: ")
                encontrado=False
                for paquete in self.packages_obj:
                    if int(opcion)==paquete.id and paquete.delivered==False:
                        paquete.delivered=True
                        encontrado=True
                    if paquete.delivered==True:
                        print("\t-->paquete fue entregado<--")
                        
                print()
                if encontrado==True:
                    print("\t-->Paquete Entregado<--")
                    print()
                    
                else:
                    print("\t-->Paquete no encontrado<--")
                    print()

            elif menu=="4":
                print()
                cliente_pendiente=[]
                for cliente in self.clients_obj:
                    for paquete_pendiente in self.packages_obj:
                        if cliente.address==paquete_pendiente.address and paquete_pendiente.delivered==False and not cliente in cliente_pendiente:
                            cliente_pendiente.append(cliente)
                for cliente in cliente_pendiente:
                    print()
                    cliente.show_attr()
            
            elif menu=="5":
                break

            else:
                print("Seleccion invalido ")
    def construir_clase(self):
        clients_dic=old_db["clients"]
        workers_dic=old_db["workers"]
        company_dic=old_db["dispatcher_companies"]
        packages_dic=old_db["packages"]

        self.clients_obj=[]
        self.workers_obj=[]
        self.company_obj=[]
        self.packages_obj=[]

        for clients in clients_dic:
            self.clients_obj.append(Client(clients["id"],clients["name"],clients["address"]))

        for workers in workers_dic:
            self.workers_obj.append(Worker(workers["id"],workers["name"],workers["role"],workers["dispatches"]))

        for package in packages_dic:
            self.packages_obj.append(Package(package["id"], package["address"], package["delivered"]))
        
        
        for company in company_dic:
                paquetes_seleccionado=[]
                ids_paquetes=company["packages"]
                for id in ids_paquetes:
                    for paquete in self.packages_obj:
                        if id==paquete.id:
                            paquetes_seleccionado.append(paquete)
                self.company_obj.append(Dispatcher_company(company["id"],company["name"],paquetes_seleccionado))
               

        
    