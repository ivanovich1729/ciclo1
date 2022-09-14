# Capturar la primera línea, total examenes y recordados.
examen, profesor = input().split()
examen, profesor = int(examen), int(profesor)
# Capturar los valores de los exámenes.
exam_lst = input().split()


def check_exam(lst):
    '''
    Funcion para verificar la cantidad de exámenes repetidos.
    Parameters
    ----------
    lst : Type (list)
        es la lista que contine los valores de los exámenes.
    Returns
    -------
    count: Type (int)
        Regresa el numero de examenes repetidos.
    '''
    check_lst = []
    count = 0
    for i in lst:
        # Si ya se ha visto un examen, sumar una copia.
        if i in check_lst:
            count += 1
        # Si no se ha visto un examen, agregarlo a los vistos.
        else:
            check_lst.append(i)
    return count


def profesor_check(examen, profesor, lst):
    '''
    Funcion para verificar la cantidad de copias encontradas por el profesor.
    Parameters
    ----------
    profesor : Type (int)
      es un número entero que representa los exámenes recordados.
    lst = Type list
      es la lista que contine los valores de los exámenes.
    examen : Type (int)
      es la cantidad total de examenes.
    Returns
    -------
    count : Type (int)
      Regresa el numero de examenes identificados por el profesor.
    '''
    count = 0
    # Iterar hasta el penúltimo examen.
    for i in range(0, len(lst) - 1):
        # Verificar que los exámenes restantes sean más de los recordados.
        if len(lst) - i > profesor:
            num = profesor
            # Comparar el número de exámenes con el número de copiados.
            # Si el total - 1 examenes es igual a los copiados, terminar.
            if count == (examen - 1):
                break
            else:
                # Comparar los exámenes con los recordados.
                while num > 0:
                    if lst[i] == lst[i + num]:
                        count += 1
                    num -= 1
        # Restar recordados si los examenes son menos.
        else:
            profesor -= 1
    return count


print(check_exam(exam_lst), profesor_check(examen, profesor, exam_lst))