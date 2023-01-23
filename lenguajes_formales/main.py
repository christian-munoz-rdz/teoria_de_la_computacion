def power(L, n):
    """
    Esta función toma como entrada un lenguaje "L" y una potencia "n", 
    y devuelve el lenguaje elevado a la potencia "n" en forma de un conjunto.
    """
    if n == 0:
        return set([""])
    elif n == 1:
        return L
    else:
        """
        Utiliza una comprensión de lista para generar un nuevo conjunto de palabras combinando
        cada palabra del lenguaje con cada palabra de la potencia "n-1" del lenguaje.
        """
        return set([x + y for x in L for y in power(L, n-1)])

def sort(L):
    """
    Esta función toma como entrada un lenguaje "L" y devuelve el mismo lenguaje ordenado 
    alfabéticamente y por longitud de las palabras.
    """
    return sorted(L, key=lambda x: (len(x), x))

def main():
    L_str = input("Defina el lenguaje: ")
    L = set(L_str.split(','))
    n = int(input("Defina la potencia: "))
    L_n = sort(power(L, n))
    print("L^{} = {}".format(n, L_n))

if __name__ == "__main__":
    main()
