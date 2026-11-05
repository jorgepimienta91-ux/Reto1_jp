# ==============================================================================
# 1. Sistema de Autenticación
# ==============================================================================
USUARIO_VALIDO = "admin"
PASSWORD_VALIDO = "1234"

usuario_proporcionado = input("Proporciona tu usuario: ")
password_proporcionado = input("Proporciona tu password: ")

if usuario_proporcionado == USUARIO_VALIDO and password_proporcionado == PASSWORD_VALIDO:
    print(f"Bienvenido al Sistema {usuario_proporcionado}")
elif usuario_proporcionado != USUARIO_VALIDO and password_proporcionado != PASSWORD_VALIDO:
    print("Usuario y Password incorrectos")
elif usuario_proporcionado != USUARIO_VALIDO:
    print("Usuario incorrecto")
else:
    print("Password incorrecto")

print("\n" + "="*50 + "\n")

# ==============================================================================
# 2. Sistema de Envíos
# ==============================================================================
destino = input("Ingresa el destino (nacional o internacional): ").strip().lower()
peso = float(input("Ingresa el peso del paquete en kilogramos: "))

if destino == "nacional":
    costo_envio = peso * 10
    print(f"El costo de envío nacional es: ${costo_envio}")
elif destino == "internacional":
    costo_envio = peso * 20
    print(f"El costo de envío internacional es: ${costo_envio}")
else:
    print("Destino no válido.")

print("\n" + "="*50 + "\n")

# ==============================================================================
# 3. Aplicación de Salud y Fitness
# ==============================================================================
nombre = input("Nombre del usuario: ")
pasos = int(input("Pasos caminados en el día: "))

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

calorias_quemadas = pasos * CALORIAS_POR_PASO
meta_alcanzada = pasos >= META_PASOS_DIARIO

print(f"Usuario: {nombre}")
print(f"Calorías quemadas aproximadas: {calorias_quemadas} kcal")
print(f"¿Meta de pasos alcanzada?: {meta_alcanzada}")

print("\n" + "="*50 + "\n")

# ==============================================================================
# 4. El mayor de dos números
# ==============================================================================
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

if num1 > num2:
    print(f"El mayor es: {num1}")
elif num2 > num1:
    print(f"El mayor es: {num2}")
else:
    print("Ambos números son iguales.")

print("\n" + "="*50 + "\n")

# ==============================================================================
# 5. Identifica la estación del año
# ==============================================================================
mes = int(input("Proporciona el valor de un mes (valor numérico entre 1 y 12): "))

if mes in [1, 2, 12]:
    print("Estación: invierno")
elif mes in [3, 4, 5]:
    print("Estación: primavera")
elif mes in [6, 7, 8]:
    print("Estación: verano")
elif mes in [9, 10, 11]:
    print("Estación: otoño")
else:
    print("Estación desconocida")

print("\n" + "="*50 + "\n")

# ==============================================================================
# 6. Sistema de Calificaciones (Actualizado con f-strings)
# ==============================================================================
calificacion = float(input("Ingresa una calificación numérica (entre 0 y 10): "))

if 9 <= calificacion <= 10:
    print(f"Para la nota {calificacion}, la calificación en letra es: A")
elif 8 <= calificacion < 9:
    print(f"Para la nota {calificacion}, la calificación en letra es: B")
elif 7 <= calificacion < 8:
    print(f"Para la nota {calificacion}, la calificación en letra es: C")
elif 6 <= calificacion < 7:
    print(f"Para la nota {calificacion}, la calificación en letra es: D")
elif 0 <= calificacion < 6:
    print(f"Para la nota {calificacion}, la calificación en letra es: F")
else:
    print(f"El valor {calificacion} está fuera del rango permitido (entre 0 y 10).")

print("\n" + "="*50 + "\n")

# ==============================================================================
# 7. Sistema de Reservación de Hotel
# ==============================================================================
nombre_cliente = input("Nombre del cliente: ")
dias_estadia = int(input("Días de estadía en el hotel: "))
vista_mar = input("¿Cuarto con vista al mar? (sí/no): ").strip().lower()

if vista_mar in ["sí", "si"]:
    costo_dia = 190.50
    tipo_cuarto = "Con vista al mar"
else:
    costo_dia = 150.50
    tipo_cuarto = "Sin vista al mar"

costo_total = dias_estadia * costo_dia

print(f"\n--- Resumen de Reservación ---")
print(f"Cliente: {nombre_cliente}")
print(f"Tipo de cuarto: {tipo_cuarto}")
print(f"Días de estadía: {dias_estadia}")
print(f"Costo total de la estadía: ${costo_total:.2f}")