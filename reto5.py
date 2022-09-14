if __name__ == '__main__':
    # Crear la base de datos de los productos en un diccionario.
    productos = {
        1: ["Naranjas", 7000.0, 35],
        2: ["Limones", 2500.0, 15],
        3: ["Peras", 2700.0, 65],
        4: ["Arandanos", 9300.0, 34],
        5: ["Tomates", 2100.0, 42],
        6: ["Fresas", 9100.0, 20],
        7: ["Helado", 4500.0, 41],
        8: ["Galletas", 500.0, 8],
        9: ["Chocolates", 4500.0, 80],
        10: ["Jamon", 17000.0, 48]
    }

    # Función para agregar nuevos productos.
    def agregar(db, info):
        '''
        Función para agregar un producto a la base de datos.
        Parameters
        ----------
        db : Type dict
            es la base de datos de los productos.
        info : Type list.
            es una lista con la información del producto a agregar.
        '''
        prod_key = info[0]
        prod_value = info[1:]
        if prod_key in db:
            raise KeyError
        else:
            db[prod_key] = prod_value

    # Función para actualizar los productos.
    def actualizar(db, info):
        '''
        Función para actualizar la información de un producto en base de datos.
        Parameters
        ----------
        db = Type dict
            es la base de datos de los productos.
        info = Type (list)
            es una lista con la información del producto a actualizar.
        '''
        prod_key = info[0]
        if prod_key in db:
            db.update({info[0]: info[1:]})
        else:
            raise KeyError

    # Funcion para borrar productos.
    def borrar(db, info):
        '''
        Función para eliminar un producto de la base de datos.
        Parameters
        ----------
        db : Type (8dict)
            es la base de datos de los productos.
        info : Type (list)
            es una lista con la información del producto a eliminar.
        '''
        prod_key = info[0]
        del db[prod_key]

    # Función para encontrar el producto con mayor precio.
    def mayor_precio(db):
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
        valor = 0
        producto = ""
        for i in db:
            if db[i][1] > valor:
                producto = db[i][0]
                valor = db[i][1]
        return producto

    # Función para encontrar el producto con menor precio.
    def menor_precio(db):
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
        valor = 10000
        producto = ""
        for i in db:
            if db[i][1] < valor:
                producto = db[i][0]
                valor = db[i][1]
        return producto

    # Función para obtener el promedio de precios.
    def promedio_precios(db):
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
    def valor_inventario(db):
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
            agregar(productos, prod_info)
        elif operacion == "actualizar":
            actualizar(productos, prod_info)
        elif operacion == "borrar":
            borrar(productos, prod_info)
        # Mostrar mayor precio, menor precio, promedio y total del inventario.
        print(mayor_precio(productos),
              menor_precio(productos),
              promedio_precios(productos),
              valor_inventario(productos))
    except KeyError:
        # En caso de no encontrar el artículo, mostrar el mensaje de error.
        print("ERROR")