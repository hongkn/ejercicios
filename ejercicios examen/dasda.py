arreglos = {

    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True,
    'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
} #'sigla': ['nombre', 'tipo', 'color_principal', 'tamaño', 'incluye_tarjeta, 'temporada]

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
} #'sigla': ['precio' 'unidades']

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese opción: "))
            if 1 <= op <= 6:
                return op
            else:
                print("Solo deben ser números del 1 al 6")
        except ValueError:
            print("Error: Solo se aceptan números enteros")

def no_existe_codigo(codigo, arreglos):
    return codigo not in arreglos

def validar_codigo(codigo):
    return len(codigo.strip()) > 0    

def validar_nombre(nombre):
    return len(nombre.strip()) > 0    

def validar_tipo(tipo):
    return len(tipo.strip()) > 0

def validar_color(color):
    return len(color.strip()) > 0    

def validar_tamaño(tamaño):
    return tamaño == "S" or tamaño == "M" or tamaño == "L"

def validar_incluye_tarjeta(si_no):
    return si_no in ["s", "n"]
    
def validar_temporada(temporada):
    return len(temporada.strip()) > 0  

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0    

def validar_unidades(unidades):
    return isinstance(unidades, int) and unidades >= 0    

def unidades_tipo(tipo):
    tipo_buscado = tipo.lower()
    total_acumulado = 0

    for codigo, info_arreglo in arreglos.items():
        if info_arreglo[1].lower() == tipo_buscado:
            unidades_disponibles = bodega[codigo][1]
            total_acumulado += unidades_disponibles
         
    print(f"El total de unidades disponibles para el tipo {tipo} es: {total_acumulado}")

def busqueda_precio(p_min, p_max):

    resultados = []

    for codigo, info_bodega in bodega.items():
        precio = info_bodega[0]
        unidades = info_bodega[1]

        if p_min <= precio and precio <= p_max and unidades > 0:
            nombre_arreglo = arreglos[codigo][0]

            formato = f"{nombre_arreglo}--{codigo}"
            resultados.append(formato)

    if len(resultados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        resultados.sort()

        print("=== Arreglos encontrados ===")
        for item in resultados:
            print(item)

def buscar_codigo(codigo):
    for codigo_buscado in arreglos:
        if codigo_buscado == codigo:
            return True
        return False

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        if buscar_codigo == True:
            bodega[codigo][0] = nuevo_precio
            return True
    return False
    
def eliminar_arreglo(codigo):

    if buscar_codigo(codigo):
        del arreglos[codigo]
        del bodega[codigo]
        return True
    return False

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada, precio, unidades):
    existe = buscar_codigo(codigo)

    if not existe:
        arreglos[codigo] = [nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada]
        bodega[codigo] = [precio, unidades]
        return True
    else:
        return False

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

    op = leer_opcion()

    if op == 1:
        while True:
            tipo_arreglo = input("Ingrese tipo de arreglo a consultar: ")

            encontrado = False

            for codigo, datos in arreglos.items():
                tipo_buscado = datos[1]
                
                if tipo_arreglo == tipo_buscado:
                    encontrado = True
                    break
            if encontrado:
                unidades_tipo(tipo_arreglo)
                break
            else:
                print("El tipo de arreglo no se encuentra en el sistema")
                    
    if op == 2:
        while True:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))

                if precio_min < 0:
                    print("Debe ser un número entero mayor a 0.")
                    continue
                break
            except ValueError:
                print("Debe ingresar valores enteros.")

        while True:
            try:
                precio_max = int(input("Ingrese el precio máximo: "))
                if precio_max <= precio_min:
                    print("Debe ser un precio mayor a tu precio mínimo")
                break
            except ValueError:
                print("Debe ingresar valores enteros.")

        busqueda_precio(precio_min, precio_max)

    if op == 3:
        while True:
            codigo = input("Ingrese código del arreglo: ").upper()
            existe = buscar_codigo(codigo)

            if not existe:
                print("El codigo no existe en el sistema.")

                while True:
                    respuesta = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    if respuesta == "s":
                        break
                    if respuesta == "n":
                        break
                    else:
                        print("Solo se admiten respuesta: (s/n)")
                if respuesta == "n":
                    break
            else: 
                while True:
                    try:
                        precio_nuevo = int(input("Ingresa nuevo precio: "))
                        if precio_nuevo < 0:
                            print("Debe ser un valor mayor o igual a 0.")

                        actualizar_precio(codigo, precio_nuevo)
                        print("Precio actualizado con éxito.")
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros.")
                break

    if op == 4:
        while True: 
            codigo = input("Ingrese el codigo del arreglo: ")
            if validar_codigo(codigo) and no_existe_codigo(codigo, arreglos):
                break
            print("Codigo inválido o ya registrado.")

        while True:
            nombre = input("Ingrese nombre: ")
            if validar_nombre(nombre):
                break
            print("Nombre inválido.")
        
        while True:
            tipo = input("Ingrese tipo: ")
            if validar_tipo(tipo):
                break
            print("Tipo inválido.")        

        while True:
            color = input("Ingrese color principal: ")
            if validar_color(color):
                break
            print("Color inválido.")

        while True:
            tamanio = input("Ingrese tamaño (S/M/L): ").upper()
            if validar_tamaño(tamanio):
                break
            print("Tamaño invalido. Ingrese S, M o L.")           
            
        while True:
            tarjeta = input("¿Incluye tarjeta? (s/n): ").lower()
            if validar_incluye_tarjeta(tarjeta):
                break
            print("Respuesta inválida. Ingrese 's' o 'n'.")

        while True:
            temporada = input("Ingrese temporada: ")
            if validar_temporada(temporada):
                break
            print("Temporada inválida.")

        while True:
            try:
                precio = int(input("Ingrese precio: "))
                if validar_precio(precio):
                    break
                print("Precio inválido. Debe ser un número entero.")
            except ValueError:
                print("Error: Solo se admiten números enteros.")

        while True:
            try:
                unidades = int(input("Ingrese unidades: "))
                if validar_unidades(unidades):
                    break
                print("Unidades inválidas. Debe ser un número entero mayor a 0.")
            except ValueError:
                print("Error: Solo se admiten números enteros.")     

        agregar_arreglo(codigo, nombre, tipo, color, tamanio, tarjeta, temporada, precio, unidades)
        print("Arreglo ingresado con éxito.")

    if op == 5:
        while True:
            codigo_eliminar = input("Ingresa el codigo que desea eliminar: ")
            if not no_existe_codigo(codigo_eliminar, arreglos):
                eliminar_arreglo(codigo_eliminar)
                print("Arreglo eliminado.")
                break
            print("Codigo inválido o inexistente.")

    if op == 6:
        print("Programa finalizado.")
        break
