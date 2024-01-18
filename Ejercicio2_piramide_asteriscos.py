### PIRAMIDE DES ASTERISCOS ###

def generar_piramide(n):
    for i in range(1, n * 2, 2):
        espacios = (n * 2 - i) // 2
        print(" " * espacios + "*" * i)

def main():
    while True:
        try:
            n = int(input("Ingrese un número entero mayor o igual a 1 para el número de niveles de la pirámide: "))
            if n >= 1:
                break
            else:
                print("El número debe ser mayor o igual a 1. Inténtelo nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    print(f"\nPirámide de asteriscos con {n} niveles:\n")
    generar_piramide(n)

if __name__ == "__main__":
    main()
