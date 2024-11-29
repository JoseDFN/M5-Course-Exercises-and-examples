
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
        self.nombre = nombre

    def hablar(self):
        pass
    
    def __str__(self):
        return f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"


class Perro(Mascota):
    def hablar(self):
        return "Woof"

class Gato(Mascota):
    def hablar(self):
        return "Meow"

p = Perro("Perro", "12 meses", "Bobby")
g = Gato("Gato", "13 meses", "Pelusa")

print (p.hablar())
print (g.hablar())