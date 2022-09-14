# Número de baldosas a revisar y el número de baldosas que el sensor es capaz de guardar
N, K = input().split()
N, K = int(N), int(K)
# Baldosas revisadas por el sensor
M = input().split()


def rev_baldosas(lst):
    '''
    Funcion para verificar la cantidad de baldosas repetidas.
    Parameters
    ----------
    lst : Type (list)
        es la lista que contine los valores de las baldosas.
    Returns
    -------
    count: Type (int)
        Regresa el numero de examenes repetidos.
    '''
    rev_lst = []
    count = 0
    for i in lst:
        # Si ya se ha visto un baldosa, sumar una repetida.
        if i in rev_lst:
            count += 1
        # Si no se ha revisado la baldosa, agregarla a las revisadas.
        else:
            rev_lst.append(i)
    return count


def rev_sensor(N, K, lst):
    '''
    Funcion para verificar la cantidad de copias encontradas por el sensor.
    Parameters
    ----------
    k : Type (int)
      es un número entero que representa las baldosas revisadas por el sensor.
    lst = Type list
      es la lista que contine los valores de las baldosas.
    N : Type (int)
      es la cantidad total de baldosas.
    Returns
    -------
    count : Type (int)
      Regresa el numero de baldosas identificados por el sensor.
    '''
    count = 0
    # Iterar hasta la penultima baldosa.
    for i in range(0, len(lst) - 1):
        # Verificar que las baldosas restantes sean más de las revisadas.
        if len(lst) - i > K:
            num = K
            # Comparar el número de baldosas con el número de revisados.
            # Si el total - 1 baldosas es igual a las revisados, terminar.
            if count == (N - 1):
                break
            else:
                # Comparar las baldosas con las leidas por el sensor.
                while num > 0:
                    if lst[i] == lst[i + num]:
                        count += 1
                    num -= 1
        # Restar leidos si las baldosas son menos.
        else:
            K -= 1
    return count


print(rev_baldosas(M), rev_sensor(N, K, M), N)