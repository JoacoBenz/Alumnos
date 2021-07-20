class Alumno:

    def __init__(self):
        self.anombres = []
        self.aapellidos = []
        self.anacimiento = []
        self.aDNI = []      
    
    def Nombre(self):
        nombre=(input("Ingresar nombre: "))
        self.nombre = nombre
        self.anombres.append(self.nombre)

    def Apellido(self):
        apellido=(input("Ingresar apellido: "))
        self.apellido = apellido
        self.aapellidos.append(self.apellido)

    def FechaNacimiento(self):
        print("Ingresar fecha de nacimiento")

        self.dd = int(input("Ingresar dia: "))
        while (self.dd > 31) or (self.dd <= 0):
            print("Dia no valido. Ingresar de nuevo.")
            print("Ingresar dia: ")
            self.dd = int(input())       

        self.mm = int(input("Ingresar mes: "))
        while (self.mm > 12) or (self.mm <= 0):
            print("Mes no valido. Ingresar de nuevo.")
            print("Ingresar mes: ")
            self.mm = int(input())

        self.aaaa = int(input("Ingresar año: "))
        while (self.aaaa > 2021) or (self.aaaa <= 1920):
            print("Año no valido. Ingresar de nuevo.")
            print("Ingresar año: ")
            self.aaaa = int(input())

        self.tupla = [self.dd, self.mm, self.aaaa]
        self.anacimiento.append(self.tupla)
        
        return self.tupla

    def DDNI(self):
        
        DNI=(input("Ingresar DNI: "))
        self.DNI = DNI
        print("¿Su DNI es: ", self.DNI,"? [s/n]: ")
        correcto = input("")
        while correcto == "n":
            DNI=(input("Ingresar DNI: "))
            self.DNI = DNI
            print("¿Su DNI es: ", self.DNI,"? [s/n]: ")
            correcto = input("")
        
        self.aDNI.append(self.DNI)
        return DNI

    def visualizar(self):
        print("Nombre y apellido: ", self.nombre, self.apellido)
        print("Fecha de nacimiento: ")
        print(self.tupla[0], self.tupla[1], self.tupla[2], sep="/")
        print("DNI: ", self.DNI)
        
    def listado(self):
        print("Listado de alumnos: ")
        for x in range(len(self.anombres)):
            print("_______________________")
            print("Nombre y apellido: ", self.anombres[x], self.aapellidos[x])
            print("Fecha de nacimiento: ", self.anacimiento[x])
            print("DNI: ", self.aDNI[x])
    
    def main(self):
        print("-----------------------")
        print("    MENU PARA CURSOS   ")
        print("-----------------------")
        opcion = 0
        cte = "s"
        while opcion != 3:
            print("1) Cargar alumno: ")
            print("2) Visualizar listado alumnos: ")
            opcion = int(input("Ingresar opcion: "))
            if opcion == 1:
                while cte == "s":
                    self.Nombre()
                    self.Apellido()
                    self.FechaNacimiento()
                    self.DDNI()
                    self.visualizar()
                    print("¿Desea agregar otro alumnno? [s/n]: ")
                    cte = input()
            elif opcion == 2:
                self.listado()

              
#programa principal

Alumno1 = Alumno()
Alumno1.main()
