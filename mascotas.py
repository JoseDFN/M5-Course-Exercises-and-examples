
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"

Animal1 = Animal("Perro", "13 Meses")


Animal2 = Animal("Gato", "6 Meses")


class Mascota(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.__nombre = nombre
#encapsulacion
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return f"Mascota[Nombre: {self.__nombre}, Especie: {self.especie}, Edad: {self.edad}]"

mascota = Mascota("Perro", "6 Meses", "IDK")

print (mascota)

mascota.edad = "2 años"
#modificador __ solo permite que la clase o propiedad sea accedidad desde la funcion
mascota.set_nombre("idk")
print (mascota.get_nombre())

print(mascota)