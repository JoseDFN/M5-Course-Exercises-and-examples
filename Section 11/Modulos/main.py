from colorama import init, Fore

init()  # Inicializar colorama

if (__name__ == "__main__"):
    print(Fore.RED + "Este es un mensaje en color rojo")
    print(Fore.GREEN + "Este es un mensaje en color verde")
    print(Fore.YELLOW + "Este es un mensaje en color amarillo")
    print(Fore.BLUE + "Este es un mensaje en color azul")