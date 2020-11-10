import sys
'''
fmc_rec (funciones monotonas crecientes - recursiva)
Devuelve una lista de relaciones (relación = conjunto de pares (tuplas))
N: lista ordenada
M: lista ordenada
'''
def fmc_rec(N, M):
    # caso base
    if(N == [] or M == []):
        return [set()]
    # caso recursivo
    head = N[0]
    tail = N[1:]
    result = []
    # hacemos una llamada recursiva por cada subcadena de M apta para ser
    # una función monotona creciente
    for i,v in enumerate(M):
        pair = (head,v)
        img = M[i:]
        subcall = fmc_rec(tail, img)
        for subrel in subcall:
            subrel.add(pair)
        result += subcall
    return result

'''
fmc (funciones monotonas crecientes)
Devuelve la lista de todas las funciones crecientes entre un poset cadena
de tamaño N y otro poset cadena de tamaño M.
'''
def fmc(N,M):
    # creamos las cadenas con el número de elementos adecuado
    l1 = list(range(N))
    l2 = list(range(M))
    # llamamos a la versión recursiva con las listas completas
    return fmc_rec(l1, l2);

#
# MAIN
#
if (__name__=="__main__"):
    if(len(sys.argv) == 3):
        N = int(sys.argv[1])
        M = int(sys.argv[2])
    else:
        N = 3
        M = 2
    funciones = fmc(N,M)
    # EL SIGUIENTE CÓDIGO ES SOLO PARA IMPRIMIRLO BONITO Y EN ORDEN
    print("N: {}\nM: {}".format(list(range(N)),list(range(M))))
    print("\n".join([str(sorted(f, key=lambda x: x[0])) for f in funciones]))
    print("Nº de funciones: {}".format(len(funciones)))
