from poset import Poset
from functools import reduce

# DATOS DE LOS POSETS
'''''''''''''''''''''''''''
Apartado (a)

a   b     a   b
\ /   ->  \ /
1         1

'''''''''''''''''''''''''''
Pa = ['a','b','1']
Ra = [('1','1'), 
    ('1','a'), 
    ('1','b'), 
    ('a','a'), 
    ('b','b')]
'''''''''''''''''''''''''''
Apartado (b)

a b c     a b c
\|/   ->  \|/
1         1

'''''''''''''''''''''''''''
Pb = ['a','b','c','1']
Rb = [('1','1'),
    ('1','a'),
    ('1','b'),
    ('1','c'),
    ('a','a'),
    ('b','b'),
    ('c','c')]
'''''''''''''''''''''''''''
Apartado (c)

2         2
/ \       / \
a   b     a   b
\ /   ->  \ /
1         1

'''''''''''''''''''''''''''
Pc = ['a','b','1','2']
Rc = [('1','1'),
    ('1','a'),
    ('1','b'),
    ('1','2'),
    ('a','a'),
    ('a','2'),
    ('b','b'),
    ('b','2'),
    ('2','2')]

'''
Función recursiva auxiliar para all_fmc
'''
def all_fmc_rec(poset1, poset2, bounds):
    # caso base
    if(len(poset1) == 0):
        return [set()]
    # caso recursivo
    # separamos en partes el poset origen
    head = list(poset1.P)[0]
    tail = poset1.copy()
    tail.remove(head)
    mayores1 = set(poset1.mayoresQue(head))
    menores1 = set(poset1.menoresQue(head))
    # los posibles pares dependen de los vinculos de head
    pertinentBounds = [dest for (orig,dest) in bounds if head in orig]
    destPosible = set(poset2.P)
    for bound in pertinentBounds:
        destPosible &= bound
    
    result = []
    # hacemos una llamada recursiva por cada posible destino
    # de head, cambiando el destino vinculado para el set de
    # elementos mayores
    for dest in destPosible:
        pair = (head, dest)
        mayores2 = set(poset2.mayoresQue(dest))
        menores2 = set(poset2.menoresQue(dest))
        newBounds = list(bounds)
        newBounds += [(menores1, menores2), (mayores1, mayores2)]
        subcall = all_fmc_rec(tail, poset2, newBounds)
        for subrel in subcall:
            subrel.add(pair)
        result += subcall
    return result

'''
Función para calcular todas las funciones monótonas crecientes
entre dos posets cualesquiera
'''
def all_fmc(poset1, poset2):
    return all_fmc_rec(poset1, poset2, [])

'''
Función para calcular todas las funciones continuas entre dos
poosets cualesquiera
'''
def all_continuas(poset1, poset2):
    crecientes = all_fmc(poset1, poset2)
    dirigidos = poset1.allDirigidos()
    continuas = []
    for f in crecientes:
        ok = True
        for M in dirigidos:
            supM = min(poset1.cotaSuperior(M))
            imgM = {b for (a,b) in f if b in M}
            supImgM = min(poset2.cotaSuperior(M))
            if supM != supImgM:
                ok = False
                break
        if ok:
            continuas.append(f)
    return continuas
            

# MAIN
if (__name__ == '__main__'):
    # asignamos el apartado a cada poset
    posets = {'a':Poset(Pa, Ra),
            'b':Poset(Pb, Rb),
            'c':Poset(Pc, Rc)}
    
    for apartado in posets:
        poset = posets[apartado]
        print('=== APARTADO ({}) ==='.format(apartado))
        # print('POSET:')
        # print(poset.toJSON())
        # print('FUNCIONES MONOTONAS CRECIENTES')
        # funciones = all_fmc(poset, poset)
        funciones = all_continuas(poset, poset)
        # EL SIGUIENTE CÓDIGO ES SOLO PARA IMPRIMIRLO BONITO Y EN ORDEN
        print("\n".join([str(sorted(f, key=lambda x: x[0])) for f in funciones]))
        print("Nº de funciones: {}".format(len(funciones)))
    
