import datetime

class Departamento:
    def __init__(self, tipo, disponible=True, comprador=None):
        self.tipo = tipo
        self.disponible = disponible
        self.comprador = comprador


class CasaFeliz:
    def __init__(self):
        self.departamentos = []
        self.precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
        self.crear_departamentos()
    
    def crear_departamentos(self):
        for piso in range(1, 11):
            for tipo in ['A', 'B', 'C', 'D']:
                self.departamentos.append(Departamento(tipo=tipo))
    
    def mostrar_departamentos_disponibles(self):
        print("Departamentos disponibles:")
        for piso in range(1, 11):
            print(f"Piso {piso}: ", end="")
            for departamento in self.departamentos[(piso-1)*4 : piso*4]:
                if departamento.disponible:
                    print(departamento.tipo, end=" ")
                else:
                    print("X", end=" ")
            print()
    
    def comprar_departamento(self):
        piso = int(input("Ingrese el número de piso (1-10): "))
        tipo = input("Ingrese el tipo de departamento (A, B, C o D): ").upper()
        
        index = (piso-1)*4 + ord(tipo) - ord('A')
        departamento = self.departamentos[index]
        
        if departamento.disponible:
            run = input("Ingrese el RUN del comprador (sin guiones ni puntos): ")
            departamento.disponible = False
            departamento.comprador = run
            print("Departamento comprado exitosamente.")
        else:
            print("El departamento no está disponible.")
    
    def ver_listado_compradores(self):
        compradores = [dep.comprador for dep in self.departamentos if dep.comprador]
        compradores.sort()
        
        print("Listado de compradores:")
        for comprador in compradores:
            print(comprador)
    
    def mostrar_ventas_totales(self):
        ventas_totales = {tipo: [0, 0] for tipo in ['A', 'B', 'C', 'D']}
        
        for departamento in self.departamentos:
            if departamento.comprador:
                tipo = departamento.tipo
                ventas_totales[tipo][0] += 1
                ventas_totales[tipo][1] += self.precios[tipo]
        
        print("Ventas totales:")
        total_general = 0
        for tipo, (cantidad, monto) in ventas_totales.items():
            total_general += monto
            print(f"Tipo {tipo} {self.precios[tipo]} UF {cantidad} {monto} UF")
        
        print(f"TOTAL {total_general} UF")


casa_feliz = CasaFeliz()

while True:
    print("\n----- Menú -----")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        casa_feliz.comprar_departamento()
    elif opcion == "2":
        casa_feliz.mostrar_departamentos_disponibles()
    elif opcion == "3":
        casa_feliz.ver_listado_compradores()
    elif opcion == "4":
        casa_feliz.mostrar_ventas_totales()
    elif opcion == "5":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
        print(f"\n¡Gracias por utilizar el sistema, {nombre} {apellido}!")
        print(f"Fecha: {fecha_actual}")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
