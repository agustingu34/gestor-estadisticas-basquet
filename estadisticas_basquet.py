def cargar_puntos():
    puntos=[]
    try:
        with open("punto.txt", "r") as f:
            for linea in f:              
                puntos.append(int(linea.strip()))
    except:
        pass
    return puntos
def guardar_puntos(puntos):
    with open("punto.txt","w") as f:
        for punto in puntos:
            f.write(str(punto)+ "\n")

def agregar_puntos(puntos):
    a=int(input("Puntos del partido: "))
    puntos.append(a)
    print("Agregado √")

def ver_partidos(puntos):
    if not puntos:
        print("No hay partidos cargados")
        return
    for i,p in enumerate(puntos,start=1):
        print(f"Partido {i}: {p} puntos")

    print(f"\ntotal partidos: {len(puntos)}")
    print(f"total de puntos:  {sum(puntos)}")      


def estadisticas(puntos):
    if not puntos:
        print("No hay partidos cargados")
        return
    maximo=max(puntos)
    minimo=min(puntos)
    promedio=sum(puntos)/len(puntos)
    print("\n📊 ESTADISTICAS")
    print(f"Total partidos: {len(puntos)}")
    print(f"Total puntos: {sum(puntos)}")
    print(f"el promedio es: {promedio:.2f}")
    print(f"🔥 Mejor partido: {maximo} puntos")
    print(f"🥶 peor partido: {minimo} puntos")

def mejor_partido(puntos):
    if not puntos:
        print("No hay partidos cargados")
        return
    mejor=max(puntos)
    print(f"Mejor partido: {mejor} puntos")

def main():
    puntos=cargar_puntos()
    while True:
        print("\n🏀 ESTADISTICAS")
        print("1 - Cargar puntos")
        print("2 -Ver partidos")
        print("3 - Estadisticas completas")
        print("4 - Mejor partido")
        print("5 - Guardar al Salir")
        opcion=input("Elegi: ")
        if opcion=="1":
            agregar_puntos(puntos)
        elif opcion=="2":
            ver_partidos(puntos)
        elif opcion=="3":
            estadisticas(puntos)
        elif opcion=="4":
            mejor_partido(puntos)
        elif opcion=="5":
            guardar_puntos(puntos)
            break
main()