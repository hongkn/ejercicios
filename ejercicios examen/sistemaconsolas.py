consolas = {}  # "siglas": ["nombre", "fabricante", "año"]
ventas = {}    # "siglas": [precio, stock]

# --- Funciones de Menú ---

def mostrar_menu():
    print("\n" + "="*40)
    print(" "*5 + "ADMINISTRACIÓN DE CONSOLAS")
    print("="*40)
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("="*40)

def elegir_opcion():
    while True:
        try:
            return int(input("Ingresa la opción: "))
        except ValueError:
            print("Error: Solo se permiten números enteros.")

# --- Funciones de Validación ---

def no_existe_sigla(sigla, consolas):
    return sigla not in consolas

def validar_sigla(sigla):
    return sigla.isupper() and 2 <= len(sigla) <= 5

def validar_nombre(nombre):
    return 3 <= len(nombre.strip()) <= 40

def validar_fabricante(fabricante):
    return 2 <= len(fabricante.strip()) <= 30

def validar_anio(anio):
    return isinstance(anio, int) and 1972 <= anio <= 2025

def validar_precio(precio):
    return isinstance(precio, float) and precio > 0

def validar_stock(stock):
    return isinstance(stock, int) and stock >= 0

# --- Función Principal (Agregar) ---

def agregar_consola(consolas, ventas):
    while True:
        sigla = input("Ingresa la sigla: ")
        if not validar_sigla(sigla):
            print("Error: La sigla debe tener entre 2 y 5 caracteres, solo letras mayúsculas y no puede estar vacía.")
        elif not no_existe_sigla(sigla, consolas):
            print("Error: Esa sigla ya existe en el sistema.")
        else:
            break

    nombre = input("Ingresa el nombre: ")
    while not validar_nombre(nombre):
        print("Error: El nombre debe tener entre 3 y 40 caracteres y no puede estar vacío.")
        nombre = input("Ingresa el nombre: ")

    fabricante = input("Ingresa el fabricante: ")
    while not validar_fabricante(fabricante):
        print("Error: El fabricante debe tener entre 2 y 30 caracteres y no puede estar vacío.")
        fabricante = input("Ingresa el fabricante: ") 

    while True:
        try:
            anio = int(input("Ingresa el año: "))
            if validar_anio(anio):
                break
            else:
                print("Error: El año debe estar entre 1972 y 2025")
        except ValueError:
            print("Error: El año solo debe tener números enteros.")

    while True:
        try:
            precio = float(input("Ingresa el precio: "))
            if validar_precio(precio):
                break
            else:
                print("Error: El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: El precio solo deben ser números decimales.")

    while True:
        try:
            stock = int(input("Ingresa el stock: "))
            if validar_stock(stock):
                break
            else:
                print("Error: El stock debe ser mayor o igual a 0.")
        except ValueError:
            print("Error: El stock solo deben ser números enteros.")
            
    consolas[sigla] = [nombre, fabricante, anio]
    ventas[sigla] = [precio, stock]
    print(f"\n¡Consola {sigla} agregada con éxito!")

# --- Opción 2: Buscar ---
def buscar_consola(dicc_consolas, dicc_ventas, sigla_buscar=None):
    if sigla_buscar is None:
        sigla_buscar = input("Ingresa la sigla de la consola a buscar: ")

    if sigla_buscar in dicc_consolas:
        nombre = dicc_consolas[sigla_buscar][0]
        fabricante = dicc_consolas[sigla_buscar][1]
        anio = dicc_consolas[sigla_buscar][2]
        precio = dicc_ventas[sigla_buscar][0]
        stock = dicc_ventas[sigla_buscar][1]
        
        print("\n=== Consola Encontrada ===")
        print(f"Sigla       : {sigla_buscar}")
        print(f"Nombre      : {nombre}")
        print(f"Fabricante  : {fabricante}")
        print(f"Año lanz.   : {anio}")
        print(f"Precio      : ${precio:,.2f}") # Agregado :,.2f para cumplir formato del enunciado
        print(f"Stock       : {stock} unidades")
        return True
    else:
        print(f"\nError: La consola con sigla '{sigla_buscar}' no se encontró.")
        return False

# --- Opción 3: Eliminar ---
def eliminar_consola(consolas, ventas): 
    sigla = input("Ingresa la sigla de la consola para eliminar: ")

    # CORRECCIÓN: Invocamos obligatoriamente a buscar_consola para validar si existe
    if buscar_consola(consolas, ventas, sigla):
        del consolas[sigla]
        del ventas[sigla]
        print(f"\n¡Éxito! La consola '{sigla}' ha sido eliminada.")
    # El "Else" ya no es necesario aquí porque buscar_consola ya avisa si no existe

# --- Opción 4: Mostrar todas ---
def mostrar_consolas(consolas, ventas):
    if len(consolas) == 0:
        print("\n" + "="*30)
        print("El sistema está vacío. No hay consolas registradas.")
        print("="*30)
        return
    
    print("\n" + "="*30)
    print("LISTADO COMPLETO DE CONSOLAS")
    print("="*30)

    for sigla in consolas:
        nombre = consolas[sigla][0]
        fabricante = consolas[sigla][1]
        anio = consolas[sigla][2]
        precio = ventas[sigla][0]
        stock = ventas[sigla][1]
        # Agregado :,.2f al precio para que coincida con el enunciado original
        print(f"Sigla: {sigla} | {nombre} | {fabricante} | {anio} | ${precio:,.2f} | Stock: {stock}")

    # CORRECCIÓN: Esto va fuera del ciclo for para que se imprima solo al final
    print("==============================")
    print(f"Total de consolas: {len(consolas)}\n")

# --- MENÚ PRINCIPAL ---
while True:
    mostrar_menu()
    opcion = elegir_opcion()

    if opcion == 1:
        agregar_consola(consolas, ventas)
    elif opcion == 2:
        buscar_consola(consolas, ventas) # CORRECCIÓN: Opción 2 es para buscar
    elif opcion == 3:
        eliminar_consola(consolas, ventas)
    elif opcion == 4:
        mostrar_consolas(consolas, ventas)
    elif opcion == 5:
        print("\nSaliendo del sistema... ¡Hasta luego!")
        break
    else:
        print("Error: Opción inválida. Elige un número del 1 al 5.")