import time

def jugar_blitz():
    tiempo_carlsen = 180
    tiempo_nakamura = 180
    tiempo_movimiento = 10
    turno = "Carlsen"

    while tiempo_carlsen > 0 and tiempo_nakamura > 0:
        print(f"\nTiempo actual - Carlsen: {tiempo_carlsen} segundos, Nakamura: {tiempo_nakamura} segundos")
        print(f"Es el turno de {turno}")

        tiempo_inicio_turno = time.time()  # Marcar el tiempo al inicio del turno

        movimiento_jugador = input("Ingresa el nombre del jugador para realizar un movimiento (Carlsen/Hikaru/Salir): ")

        tiempo_fin_turno = time.time()  # Marcar el tiempo al final del turno

        if movimiento_jugador == "Salir":
            print("\nPartida terminada.")
            break
        elif movimiento_jugador == turno:
            tiempo_transcurrido = int(tiempo_fin_turno - tiempo_inicio_turno)
            if turno == "Carlsen":
                tiempo_carlsen -= tiempo_transcurrido
            else:
                tiempo_nakamura -= tiempo_transcurrido

            if tiempo_carlsen <= 60 or tiempo_nakamura <= 60:
                tiempo_movimiento = 5

            turno = "Nakamura" if turno == "Carlsen" else "Carlsen"
            tiempo_carlsen += tiempo_movimiento if turno == "Carlsen" else 0
            tiempo_nakamura += tiempo_movimiento if turno == "Nakamura" else 0
        else:
            print("¡Error! Nombre de jugador incorrecto. Inténtalo de nuevo.")

    if tiempo_carlsen <= 0 and tiempo_nakamura <= 0:
        print("\n¡Empate!")
    elif tiempo_carlsen <= 0:
        print("\n¡Hikaru Nakamura ha ganado!")
    elif tiempo_nakamura <= 0:
        print("\n¡Magnus Carlsen ha ganado!")

if __name__ == "__main__":
    jugar_blitz()

