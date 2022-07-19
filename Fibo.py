"""
Ecrire l'algorithme de la suite de fibonacci:
C'est une suite définie par Un = Un-1 + Un-2
Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)
"""

def input_int(message:str)->int:
    """
    function pour entrer un nombre integer
    """
    carac = input(message)
    try:
        nombre = int(carac)
    except ValueError as value_err:
        print("entrer un ENTIER !")
        print(value_err)
        nombre = input_int(message)
    return nombre
    
def input_int_positif(message:str)->int:
    """
    function pour entrer integer positif
    """
    nombre_pos = input_int(message)
    if nombre_pos < 0:
        print("entrer un POSITIF !")
        nombre_pos = input_int_positif(message)
    return nombre_pos

def fibonacci(nombre):
    """
    function de calcul fibonacci
    """
    elem_fibonacci=[0,1]
    for i in range(2,nombre):
        elem_fibonacci.insert(i,elem_fibonacci[i-1]+elem_fibonacci[i-2])
    print(elem_fibonacci)

nombreSerie=0
while nombreSerie<=1:
    message_1="Entrer un entier positif plus que 1 correspondant à nombre \
        d'elements souhaités de la serie Fibonacci"
    nombreSerie=input_int_positif(message_1)

fibonacci(nombreSerie)
