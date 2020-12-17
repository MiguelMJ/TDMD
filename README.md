# Teoría de Dominios y Modelos Denotacionales
_Programas de los ejercicios prácticos de la asignatura TDMD 2020-2021 en la Universidad de Málaga._

## Ejercicios

### Tema 1. Dcpo y dcpos punteados.

Los ejercicios de este tema se solucionan en `poset.py`. Las funciones que se corresponden con cada ejercicio son:

1. `Poset.validate` : Comprueba que el conjunto y la relación forman un orden parcial ([poset](https://en.wikipedia.org/wiki/Partially_ordered_set)).
2. `allPosets` : Genera todos los posets dentro de un conjunto cualquiera (solución por fuerza bruta).
3. `Poset.subconjuntoDirigido` : Comprueba si un subconjunto del poset es dirigido. 
4. `Poset.isDCPO` : Comprueba si el poset es un [dcpo](https://en.wikipedia.org/wiki/Complete_partial_order).

### Tema 2. Funciones continuas

1. ` fmc` en `fmc-cadena.py` genera todas las posibles funciones crecientes entre dos cadenas de tamaños cualesquiera.

   `nfmc` en `numero-fmc-cadena.py` calcula el número de funciones entre dos cadenas de tamaños cualesquiera, pero sin generarlas.

2. `all_fmc` en `fmc-poset.py` genera todas las posibles funciones crecientes entre dos posets cualesquiera.

3. `all_continuas` en `fmc-poset.py` genera todas las posibles funciones continuas entre dos posets cualesquiera.

## To do

- Repaso estilo para dejar todas las funciones y variables con nombres en un mismo idioma y no mezclar inglés y español.
- Unificar los métodos relacionadas con funciones continuas en un solo fichero.
- Hacer un ejecutable principal, en lugar de librerías sueltas.
- Incluir algunos ejemplos de posets para usarlos en los ejercicios (en ficheros json).
- ¿Funciones de visualización?