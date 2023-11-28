def torrehanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mueve el disco 1 desde {origen} hacia {destino}")
        return
    torrehanoi(n-1, origen, auxiliar, destino)
    print(f"Mueve el disco {n} desde {origen} hacia {destino}")
    torrehanoi(n-1, auxiliar, destino, origen)

# Ejemplo de uso con 8 discos
discos = 5
torrehanoi(discos, 'Torre A', 'Torre C', 'Torre B')
