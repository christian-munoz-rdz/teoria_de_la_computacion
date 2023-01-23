def power(L, n):
    if n == 0:
        return set([""])
    elif n == 1:
        return L
    else:
        return set([x + y for x in L for y in power(L, n-1)])

def sort(L):
    return sorted(L, key=lambda x: (len(x), x))

def main():
    L_str = input("Defina el lenguaje: ")
    L = set(L_str.split(','))
    n = int(input("Defina la potencia: "))
    L_n = sort(power(L, n))
    print("L^{} = {}".format(n, L_n))

if __name__ == "__main__":
    main()
