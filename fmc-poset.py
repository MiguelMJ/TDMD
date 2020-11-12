from dcpo import Poset

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
Función para calcular todas las funciones monótonas crecientes 
entre dos posets cualquiera
'''
def all_fmc_rec(poset1, poset2):
	# caso base
	if(len(poset1) == 0):
		return [set()]
	# caso recursivo
	

# MAIN
if (__name__ == '__main__'):
	# Creamos los posets y los validamos
	posets = [Poset(Pa, Ra),
			  Poset(Pb, Rb),
			  Poset(Pc, Rc)]
	
