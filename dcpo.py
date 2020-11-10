'''
autor: Miguel Mejía Jiménez
descr: Este archivo es la entrega final del Tema 1 de la  asignatura de
       Teoría de Dominios y Modelos Denotacionales 2020
'''
import sys

'''
Esta clase contiene los datos relacionados con un Poset y las funciones
para evaluar sus propiedades.
En todas las funciones se usa siguiente notación:
    P para referirse al conjunto del Poset
    R para referirse a la relación (conjunto de pares) del Poset
    M para referirse a cualquier subconjunto de P
'''
class Poset():
    '''
    Constructor
    '''
    def __init__(self, P,R):
        # Inicializar los atributos principales
        self.P = set(P)
        self.R = R
        
        # Inicializar algunas cachés
        self.cache_relaciones = {}
        self.cache_cotas_superiores = {}
        self.cache_sub_dirigidos = {}
        self.cache_has_bottom = {}
        self.cache_bottom = {}
    '''
    Función para comprobar que realmente es un Poset
    '''
    def validate(self):
        # Comprobar las propiedades de R
        if(len(self.R) == 0 and len(self.P) != 0):
            self.info = 'Relación vacía'
            return False
        for elemento in self.P:
            relaciones1 = self.relacionadosCon(elemento)
            # REFLEXIVA
            if(elemento not in relaciones1):
                self.info = 'Relación no reflexiva: {}'.format(elemento)
                return False
            relaciones1.remove(elemento)
            for r in relaciones1:
                # TRANSITIVA
                relaciones2 = self.relacionadosCon(r)
                for r2 in relaciones2:
                    if(r2 not in relaciones1):
                        if(r2 == elemento):
                            self.info = 'Relación no antisimétrica: {} <= {}'.format(r, elemento)
                            return False
                        else:
                            self.info = 'Relación no transitiva: {} <= {} <= {}'.format(elemento, r, r2)
                            return False
                # ANTISIMETRICA
                if(elemento in relaciones2):
                    self.info = 'Relación no antisimétrica: {} <= {}'.format(r, elemento)
                    return False
        # Si llegamos a este punto sin errores, P y R son un Poset y el 
        # objeto se construye sin errores
        return True
    '''
    Función auxiliar para obtener la lista de elementos relacionados con
    un elemento dado del conjunto.
    '''
    def relacionadosCon(self, elemento):
        if(elemento in self.cache_relaciones):
            return self.cache_relaciones[elemento]        
        relaciones = [n[1] for n in self.R if n[0] == elemento]
        self.cache_relaciones[elemento] = relaciones
        return relaciones
    '''
    Función para obtener la cota superior de un subconjunto M en el Poset
    '''
    def cotaSuperior(self,M):
        M = set(M)
        representacion = str(M)
        if(representacion in self.cache_cotas_superiores):
            return self.cache_cotas_superiores[representacion]
        
        cota = self.P
        for m in M:
            superiores = {y for [x,y] in self.R if x == m}
            cota = cota & superiores
        self.cache_cotas_superiores[representacion] = cota
        return cota
    '''
    Función para comprobar que un subconjunto M es dirigido
    '''
    def subconjuntoDirigido(self, M):
        M = list(set(M))
        representacion = str(M)
        if (representacion in self.cache_sub_dirigidos):
            return self.cache_sub_dirigidos[representacion]
        paresM = [[a,b] for i,a in enumerate(M) for b in M[i:]]
        for par in paresM:
            cotas = self.cotaSuperior(par)
            if(not bool(set(M) & cotas)):
                self.cache_sub_dirigidos[representacion] = False;
                return False;
        self.cache_sub_dirigidos[representacion] = True;
        return True
    '''
    Función para comprobar que el Poset tiene bottom
    '''
    def hasBottom(self):
        if (self.cache_has_bottom != None):
            return self.cache_has_bottom
        for elem in self.P:
            relaciones = self.relacionadosCon(elem)
            if(set(relaciones) == self.P):
                self.cache_bottom = elem
                self.cache_has_bottom = True
                return True
        self.cache_has_bottom = False
        return False
    '''
    Función para calcular el bottom del Poset, si lo tiene
    '''
    def bottom(self):
        if(self.hasBottom()):
            return self.cache_bottom
        return None
    '''
    Función para comprobar si el Poset es un DCPO punteado
    '''
    def isDCPO(P,R):
        return self.hasBottom()
        '''
        if (not hasBottom):
            return False, None
        partes = powerset(P)
        dirigidos = [sub for sub in partes if subconjuntoDirigido(P,R,sub)]
        for d in dirigidos:
            cota = cotaSuperior(P,R,d)
            if(not cota):
                return False
        return True
    '''
    
'''
Función para calcular el conjunto de partes de un conjunto S
'''
def powerset(S):
    result = []
    size = len(S)
    sizePow2 = 1 << size
    for i in range(sizePow2):
        result.append([S[j] for j in range(size) if (i & (1 << j))])
    return result
'''
Función para calcular todos los subconjuntos Poset de un conjunto S
'''
def allPoset(S):
    # TODAS LAS POSIBLES RELACIONES
    productoCartesiano = [[a,b] for i,a in enumerate(S) for b in S]
    todasRelaciones = powerset(productoCartesiano)
    result = []
    for relacion in todasRelaciones:
        poset = Poset(S, relacion)
        if(poset.validate()):
            result.append(poset)
    return result

'''
Poset para los tests

Diagrama de Hasse formado por P1 y R1
     
     5
    / \
   3   4
    \ /
     2
     |
     1
'''
P1 = [1,2,3,4,5]
R1 = [[1,1],
        [1,2],
        [1,3],
        [1,4],
        [1,5],
        [2,2],
        [2,3],
        [2,4],
        [2,5],
        [3,3],
        [3,5],
        [4,4],
        [4,5],
        [5,5]
    ]
'''
Funciones para los tests
'''
def print_poset_test(poset, test_name=None):
    ok = poset.validate()
    if(test_name):
        print('[{}] '.format(test_name), end='')
    print((ok and 'Is Poset' or poset.info))
def test01_poset():
    # Test 1: True
    print_poset_test(Poset(P1,R1), '1')
    # Test 2: No reflexiva
    R1.remove([2,2])
    print_poset_test(Poset(P1,R1), '2')
    # Test 3: No transitiva
    R1.append([2,2])
    R1.remove([1,4])
    print_poset_test(Poset(P1,R1), '3')
    # Test 4: No antisimetrica
    R1.append([1,4])
    R1.append([5,1])
    print_poset_test(Poset(P1,R1), '4')
    R1.remove([5,1])
    # Dejamos P1 y R1 como debería estar

def test02_allPosets(s):
    fmt = 'Nº de Posets posibles con {}: {}'
    x = allPoset(s)
    print(fmt.format(s,len(x)))

def print_sub_directed_test(poset, m, test_name=None):
    if(test_name):
        print('[{}] '.format(test_name), end='')
    if (poset.subconjuntoDirigido(m)):
        print(str(m)+" es un subconjunto dirigido")
    else:
        print(str(m)+" no es un subconjunto dirigido")

def test03_subDirected():
    poset = Poset(P1,R1)
    print_sub_directed_test(poset,{1,2,3},'1')
    print_sub_directed_test(poset,{2,4,5},'2')
    print_sub_directed_test(poset,{1,2,5},'3')
    print_sub_directed_test(poset,{1,3,4},'4')
    print_sub_directed_test(poset,{3,4,5},'5')
    
if __name__ == '__main__':
    test01_poset()
    test02_allPosets({'a','b','c'})
    test02_allPosets({'a','b','c','d'})
    test03_subDirected()
