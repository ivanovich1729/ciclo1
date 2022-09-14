# Registrar los criterios para la seleccion del carro.
criterios = {
    "cc": 1200,
    "max_cc": 3600,
    "año": 2018,
    "max_km": 30000,
    "max_gas": 35,
    "ahorro": 12000,
    "cap_endeuda": 14000,
    "hermano": 13500
}
# Solicitar la cantidad de líneas.
lineas = int(input())
# Registrar cada línea
catalogo = {}
for i in range(lineas):
    linea = input().split()
    # Convertir cada elemento a entero para poder realizar los calculos.
    linea = [int(x) for x in linea]
    # Agregar la nueva lista al diccionario.
    catalogo.update({i: linea})


def seleccion(lineas, criterios, catalogo):
    '''
    Funcion para seleccionar el carro que cumpla los criterios del usuario.
    Parameters
    ----------
    lineas : Type int
        es la cantidad de entradas a comparar.
    criterios : Type dict
        contiene los criterios a evaluar.
    catalogo : Type dict
        contiene los valores de cada carro a comparar.
    '''
    # Inicializar variables de control.
    deuda = 0
    count = 0
    for i in range(lineas):
        # Verificar si el carro es de mayor valor al del hermano.
        if criterios["hermano"] > catalogo[i][4]:
            continue
        # Vefirivar si el cilindraje es mayor que 1200 y menor que 3600.
        elif criterios["cc"] >= catalogo[i][0] or (
         criterios["max_cc"] <= catalogo[i][0]):
            continue
        # Verificar que el año sea 2018 o superio.
        elif criterios["año"] >= catalogo[i][1]:
            continue
        # Verificar que no tenga más de 30000 km recorridos.
        elif criterios["max_km"] <= catalogo[i][2]:
            continue
        # Verificar que el consumo no sea superor a 35 km/gal
        elif criterios["max_gas"] <= catalogo[i][3]:
            continue
        else:
            # Calcular el valor extra a pagar.
            deuda = catalogo[i][4] - criterios["ahorro"]
        # Verificar que el valor extra no supere la capacidad de endeudamiento.
        if deuda < criterios["cap_endeuda"]:
            # Mostrar el valor extra.
            print(deuda)
            count += 1
    # Si ningún carro cumple los criterios, mostrar el mensaje.
    if count == 0:
        print("NO DISPONIBLE")


seleccion(lineas, criterios, catalogo)