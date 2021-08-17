import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input("Area a pintar en metros: "))
    rend = float(input("Rendimiento (m2/l): "))
    litros = math.ceil(area/rend)
    print("Litros a comprar:", math.ceil(litros))
if __name__ == '__main__':
    main()
