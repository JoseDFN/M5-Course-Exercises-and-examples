
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
    
    def __str__(self):
        return f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"



class regMascotas:
    """Clase para realizar el registro de mascotas"""
    def __init__(self) -> None:
        self.mascotas = []
    """
    Agregar mascotas al registro
    Parametro: 
    mascota (Mascota) La mascota a agregar al registro    
    """
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def listar_mascotas (self):
        if self.mascotas:
            print(" Lista de mascotas \n", "="*30)
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas registradas")

    def editar_mascota(self, indice, nueva_mascota):

        """
        edita una mascota del registro

        parametros:
        indice(int) -> indice de la mascota a editar
        nueva_mascota (Mascota) -> La nueva informacion de la mascota
        """

        if indice< 0 or indice>= len(self.mascotas):
            print("No hay registro con este indice")
        else:
            self.mascotas[indice] = nueva_mascota
            print("Informacion de la mascota editada correctamente")

    def eliminar_mascota (self, indice):
        if indice< 0 or indice>= len(self.mascotas):
            print("No hay registro con este indice")
        else:
            del self.mascotas[indice]
            print("Mascota eliminada correctamente")