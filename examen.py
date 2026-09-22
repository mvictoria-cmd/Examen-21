# Examen práctico - Terminal de Expedición Espacial
# Nombre y apellido:
# Curso:
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
# =========================
nombre_piloto = input("Ingrese su nombre: ")

combustible = 25

Cantidad_viajes = 0

viajes_Luna = 0

viajes_Marte = 0

viajes_Saturno = 0

destinos = ["luna", "marte", "saturno"]

costos = ["20", "35", "50"]

print("Bienvenido a la Terminal de Expedición Espacial, ", nombre_piloto)
print("Combustible disponible: ", combustible, "unidades")



# =========================
# ETAPA 2 - NAVEGACIÓN
# =========================
print("elija un destino")
print("0. luna - 20 unidades de combustible")
print("1. marte - 35 unidades de combustible")
print("2. saturno - 50 unidades de combustible")

seleccion = int(input("Seleccione un destino: "))
if seleccion == 0:
    if combustible > 20:
        print("Destino seleccionado: luna")
        print("combustible necesario: 20 unidades")
        combustible_restante= combustible - 20
        viajes_Luna += 1
        print ("viaje realizado correctamente")
        print("Combustible restante: ", combustible_restante, "unidades")
    elif combustible < 20:
        print("No hay suficiente combustible para realizar el viaje a la luna.")
elif seleccion == 1: 
    if combustible > 35:
        print("Destino seleccionado: marte")
        print("combustible necesario: 35 unidades")
        combustible_restante = combustible - 35
        viajes_Marte += 1
        print ("viaje realizado correctamente")
        print("Combustible restante: ", combustible_restante, "unidades")
    elif combustible < 35: 
        print("No hay suficiente combustible para realizar el viaje a Marte.")
elif seleccion == 2:
    if combustible > 50:
        print("Destino seleccionado: saturno")
        print("combustible necesario: 50 unidades")
        combustible_restante = combustible - 50
        viajes_Saturno += 1
        print ("viaje realizado correctamente")
        print("Combustible restante: ", combustible_restante, "unidades")
    elif combustible < 50: 
        print("No hay suficiente combustible para realizar el viaje a Saturno.")
else:
    print("Opción inválida, seleccione un destino válido")






# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener destino y costo.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.
