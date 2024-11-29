from mi_paquete import modulo1
import datetime as dt
from datetime import date, datetime

if (__name__ == "__main__"):
    hoy = dt.datetime.now()
    hoy2 = date.today()
    ahora = datetime.now()

    print (f"Hoy es {hoy2} \nHoy es {hoy}")
    print (f"ahora es {ahora}")

    modulo1.saludar()

    print(__name__)
    print("Mensaje solo mostrado si el prorama se ejecuta desde el archivo principal")