"""
Ecrire l'algorithme de la suite de fibonacci:
C'est une suite définie par Un = Un-1 + Un-2
Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)
"""

import fonction

def fibo(nombre):
    elem_fibonacci=[0,1]
    for i in range(2,nombre):
        elem_fibonacci.insert(i,elem_fibonacci[i-1]+elem_fibonacci[i-2])
    print(elem_fibonacci)

nombreSerie=0
while nombreSerie<=1:
    msg="Entrer un entier positif plus que 1 correspondant à nombre d'elements souhaités de la serie Fibonacci"
    nombreSerie=fonction.input_int_positif(msg)

fibo(nombreSerie)