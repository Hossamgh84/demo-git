"""

Ecrire l'algorithme qui permet de vérifier si un triangle est rectangle

Rappel un triangle est rectangle si il respecte le triplet pythagoricien a²+b²=c²


"""
arr = []

# Tant que l'utilisateur n'a pas rentrer 3 chiffres il recommence
while len(arr) != 3:
    numbers = input("Entrez les 3 longueurs (séparée d'un espace) :")
    arr = numbers.split()  # split est une méthode qui s'applique sur des chaines de caractères pour les transformer en tableau de "mots"
    # "15 2 8" devient [ "15" , "2" , "8" ]
    numbers.strip()

Pythagore=False
arr_num=[]
for i in range(len(arr)):
    arr_num[i]=float(arr[i])
if arr[0]>arr[1]:
    if arr[0]>arr[2]:
        if arr[0]**2==arr[1]**2+arr[2]**2:
            Pythagore=True
    elif arr[2]**2==arr[0]**2+arr[1]**2:
            Pythagore=True
elif arr[1]>arr[2]:
    if arr[1]**2==arr[0]**2+arr[2]**2:
        Pythagore=True
    elif arr[2]**2==arr[0]**2+arr[1]**2:
        Pythagore=True

if Pythagore:
    print(f"le triangle de trois cotés de : {arr} respecte le triple de Pythagore.")
else:
    print(f"le triangle de trois cotés de : {arr} ne respecte pas le triple de Pythagore.")
