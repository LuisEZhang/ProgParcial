import sqlite3

def conectar_bd():
    conexion = sqlite3.connect('Ventas_mayor.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT,
            informacion TEXT
        )
    ''')
    conexion.commit()
    return conexion, cursor

while True:
    print("\nVXM")
    print("a) Agregar nuevo producto")
    print("c) Editar información del producto")
    print("d) Eliminar producto")
    print("e) Lista de productos")
    print("f) Buscar información del product")
    print("g) Salir")

    opcion = input("Que desea hacer?").lower()

    if opcion == 'a':
        producto = input("Producto: ")
        informacion = input("Información: ")

        conexion, cursor = conectar_bd()
        cursor.execute("INSERT INTO productos (producto, informacion) VALUES (?, ?)", (producto, informacion))
        conexion.commit()
        print(f"El producto {producto} ha sido agregada correctamente.")

    elif opcion == 'c':
        producto_a_editar = input("Ingrese el producto que desea editar: ")
        nuevo_producto = input("Nuevo producto: ")
        nueva_informacion = input(f"Nueva informacion de {nuevo_producto}: ")

        conexion, cursor = conectar_bd()
        cursor.execute("UPDATE productos SET producto=?,informacion=? WHERE producto=?",
                       (nuevo_producto, nueva_informacion, producto_a_editar))
        conexion.commit()
        print("Producto editado correctamente.")

    elif opcion == 'd':
        producto_a_eliminar = input("Ingrese el producto que desea eliminar: ")

        conexion, cursor = conectar_bd()
        cursor.execute("DELETE FROM producto WHERE producto=?", (producto_a_eliminar,))
        conexion.commit()
        print(f"El producto {producto_a_eliminar} ha sido eliminado correctamente.")

    elif opcion == 'e':
        conexion, cursor = conectar_bd()
        cursor.execute("SELECT producto, informacion FROM productos")
        producto = cursor.fetchall()

        if not producto:
            print("El diccionario está vacío.")
        else:
            for producto, informacion in producto:
                print(f"{producto}: {informacion}")

    elif opcion == 'f':
        producto_a_buscar = input("Que producto desea buscar: ")

        conexion, cursor = conectar_bd()
        cursor.execute("SELECT informacion FROM producto WHERE producto=?", (producto_a_buscar,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"Informacion de '{producto_a_buscar}' es: {resultado[0]}")
        else:
            print(f"El producto {producto_a_buscar} no se encuentra en el inventorio.")

    elif opcion == 'g':
        print("Hasta luego")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")