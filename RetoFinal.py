# Defino
from typing import Counter
contador = 0
Estado = True
datosContadorExterno = [1] * 11
numeros_repetidos = None
frecuencias = [0] * 10


while True:
    print("\n--- MENU ---")
    print("1.- Solicitar un número del 0 al 9")
    print("2.- Numeros No Elegidos")
    print("3.- Mostrar Apariciones")
    print("4.- Ver Media De Numeros")
    print("5.- Numeros Mas Frecuentes")
    print("6.- Numeros Menos Frecuente")
    print("7.- Numeros Pares E Impares")
    print("8.- Total")
    print("9.- Salir Del Programa")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        while True:
            try:
                num = int(input("Introduce un número del 0 al 9: "))
                if 0 <= num <= 9:
                    frecuencias[num] += 1
                    break
                else:
                    print("Número fuera de rango. Debe estar entre 0 y 9.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    elif opcion == "2":
        print("Números no elegidos: ", end="")
        for i in range(10):
            if frecuencias[i] == 0:
                print(i, end=" ")
        print()

    elif opcion == "3":
        print("Apariciones de cada número:")
        for i in range(10):
            print(f"{i} = {frecuencias[i]} veces")

    elif opcion == "4":
        total = sum(frecuencias)
        media = total / 10.0
        print(f"Media de apariciones: {media:.2f}")

    elif opcion == "5":
        max_apariciones = max(frecuencias)
        print("Numeros Mas Frecuentes ", end="")
        for i in range(10):
            if frecuencias[i] == max_apariciones:
                print(i, end=", ")
        print()

    elif opcion == "6":
        min_apariciones = min([f for f in frecuencias if f > 0]) if any(f > 0 for f in frecuencias) else 0
        print("Numeros Menos Frecuentes: ", end="")
        for i in range(10):
            if frecuencias[i] == min_apariciones and frecuencias[i] > 0:
                print(i, end=",")
        print()

    elif opcion == "7":
        pares = 0
        impares = 0
        for i in range(10):
            if i % 2 == 0:
                pares += frecuencias[i]
            else:
                impares += frecuencias[i]
        print(f"Total De Apariciones De Numeros Pares: {pares}")
        print(f"Total De Apariciones De Numero Impares: {impares}")

    elif opcion == "8":
        total = sum(frecuencias)
        print(f"Total De Apariciones De Todos Los Numeros: {total}")

    elif opcion == "9":
        print("Saliendo Del Programa...")
        break

    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 9.")

    frecuencia = Counter(datosContadorExterno)
    numeros_repetidos = [numero for numero , cantidad in frecuencia.items() if cantidad > 1]
    print("La frecuencia es :", numeros_repetidos)