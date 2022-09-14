if __name__ == '__main__':
    # Crear la base de datos de los productos en un diccionario.
    inventario = {
        1: ["Manzanas", 5000.0, 25],
        2: ["Limones", 2300.0, 15],
        3: ["Peras", 2700.0, 33],
        4: ["Arandanos", 9300.0, 5],
        5: ["Tomates", 2100.0, 42],
        6: ["Fresas", 4100.0, 3],
        7: ["Helado", 4500.0, 41],
        8: ["Galletas", 500.0, 8],
        9: ["Chocolates", 3500.0, 80],
        10: ["Jamon", 15000.0, 10]
    }

    # Función para agregar nuevos productos.
    def AGREGAR(db, info):
        '''
        Función para agregar un producto a la base de datos.
        Parameters
        ----------
        db : Type dict
            es la base de datos de los productos.
        info : Type list.
            es una lista con la información del producto a agregar.
        '''
        codigo = info[0]
        valor = info[1:]
        if codigo in db:
            raise KeyError
        else:
            db[codigo] = valor

    # Función para actualizar los productos.
    def ACTUALIZAR(db, info):
        '''
        Función para actualizar la información de un producto en base de datos.
        Parameters
        ----------
        db = Type dict
            es la base de datos de los productos.
        info = Type (list)
            es una lista con la información del producto a actualizar.
        '''
        codigo = info[0]
        if codigo in db:
            db.update({info[0]: info[1:]})
        else:
            raise KeyError

    # Funcion para borrar productos.
    def BORRAR(db, info):
        '''
        Función para eliminar un producto de la base de datos.
        Parameters
        ----------
        db : Type (8dict)
            es la base de datos de los productos.
        info : Type (list)
            es una lista con la información del producto a eliminar.
        '''
        codigo = info[0]
        del db[codigo]

    # Función para encontrar el producto con mayor precio.
    def mayorValor(db):
        '''
        Función para encontrar el producto con mayor precio.
        Parameters
        ----------
        db : Type dict
            es la base de datos de los productos.
        Returns
        -------
            Regresa una string con el nombre el producto con mayor precio.
        '''
        precio = 0
        inventario = ""
        for i in db:
            if db[i][1] > precio:
                inventario = db[i][0]
                precio = db[i][1]
        return inventario

    # Función para encontrar el producto con menor precio.
    def menorValor(db):
        '''
        Función para encontrar el producto con menor precio.
        Parameters
        ----------
        db = Type dict
            es la base de datos de los productos.
        Returns
        -------
            Regresa una string con el nombre el producto con menor precio.
        '''
        precio = 10000
        inventario = ""
        for i in db:
            if db[i][1] < precio:
                inventario = db[i][0]
                precio = db[i][1]
        return inventario

    # Función para obtener el promedio de precios.
    def promedioPrecios(db):
        '''
        Función para calcular el promedio de precios.
        Parameters
        ----------
        db : Type dict
            es la base de datos de los productos.
        Returns
        -------
            Regresa un float con el promedio de precios y 1 decimal.
        '''
        promedio = 0
        for i in db:
            promedio += db[i][1]
        return round((promedio / len(db)), 1)

    # Función para conocer el valor total del inventario.
    def valorTotal(db):
        '''
        Función para calcular el valor total del inventario.
        Parameters
        ----------
        db : Type dict
            es la base de datos de los productos.
        Returns
        -------
            Regresa un float con el valor total del inventario y 1 decimal.
        '''
        total = 0
        for i in db:
            total += (db[i][1] * db[i][2])
        return total

    # Capturar la operación a realizar en el inventario.
    operacion = input().lower()
    # Capturar la información del producto.
    prod_info = input().split()
    # Convertir los valores a datos númericos para posteriores cálculos.
    prod_info[0], prod_info[3] = int(prod_info[0]), int(prod_info[3])
    prod_info[2] = float(prod_info[2])
    try:
        # Actualizar la base de datos según los inputs.
        if operacion == "agregar":
            AGREGAR(inventario, prod_info)
        elif operacion == "actualizar":
            ACTUALIZAR(inventario, prod_info)
        elif operacion == "borrar":
            BORRAR(inventario, prod_info)
        # Mostrar mayor precio, menor precio, promedio y total del inventario.
        print(mayorValor(inventario),
              menorValor(inventario),
              promedioPrecios(inventario),
              valorTotal(inventario))
    except KeyError:
        # En caso de no encontrar el artículo, mostrar el mensaje de error.
        print("ERROR")