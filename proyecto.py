class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def validar(self):
        if self.edad <= 0 or self.edad >= 100:
            return "Error --> El dato ingresad no es valido en el sistema"
        elif self.edad >= 18:
            return f"{self.nombre} usted es mayor de edad"
        return f"{self.nombre} usted es menor de edad"
        

n1 = Persona(nombre=input("Ingrese su nombre: "), edad= int(input("Ingrese su edad: ")))
print(n1.validar())