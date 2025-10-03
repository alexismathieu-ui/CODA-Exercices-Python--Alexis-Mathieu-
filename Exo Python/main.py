import time
import random

def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Test de texte.")
    nom = input("Entrez votre nom : ")
    print("Bonjour", nom)

def exercice3():
    print("Exercice 3 : Afficher sur 3 ligne.")
    print("Bonjour")
    print("Je suis")
    print("Alexis")

def exercice4():
    print("Exercice 4 : Calculer l'âge.")
    année = int(input("Entrez votre année de naissance : "))
    calcule_année = 2025 - année
    print("Vous devez avoir ", calcule_année , "ans")

def exercice5():
    print("Exercice 5 : addition simple.")
    add1 = int(input("Entrez le premier nombre : "))
    add2 = int(input("Entrez le deuxième nombre : "))
    somme = add1 + add2
    print("La somme de", add1, "et", add2, "est :", somme)

def exercice6():
    print("Exercice 6 : soustraction simple")
    sous1 = int(input("Entrez le premier nombre : "))
    sous2 = int(input("Entrez le deuxième nombre : "))
    difference = sous1 - sous2
    print("La différence entre", sous1, "et", sous2, "est :", difference)

def exercice7():
    print("Exercice 7 : Multiplication simple")
    mult1 = int(input("Entrez le premier nombre : "))
    mult2 = int(input("Entrez le deuxième nombre : "))
    produit = mult1 * mult2
    print("Le Produit de", mult1, "et", mult2, "est :", produit)

def exercice8():
    print("Exercice 8 : Division simple")
    div1 = int(input("Entrez le premier nombre : "))
    div2 = int(input("Entrez le deuxième nombre : "))
    division = div1 / div2
    print("La division de", div1, "et", div2, "est :", division)

def exercice9():
    print("Exercice 9 : Carré d'un nombre")
    car = int(input("Entrez le premier nombre : "))
    carré = car ** 2
    print("La valeur de " , car , "au carré est" , carré)

def exercice10():
    print("Exercice 10 : Double d'un nombre")
    dou = int(input("Entrez le premier nombre : "))
    double = dou * 2
    print("La double de ", dou , "est" , double)

def exercice11():
    print("Exercice 11 : Moitié d'un nombre")
    moi = int(input("Entrez le premier nombre : "))
    moitié = moi/2
    print("La moitié de ", moi , "est" , moitié)

def exercice12():
    print("Exercice 12 : Afficher 5 Fois")
    n = 0
    while n <= 4 :
        print("Hello")
        n = n+1

def exercice13():
    print("Exercice 13 : Compter jusqu'à 5")
    for i in range(1, 6):
        print(i)

def exercice14():
    print("Exercice 14 : Table de 2")
    for i in range(1, 6):
        print(i, "x 2 = ", i*2) 

def exercice15():
    print("Exercice 15 : Périmètre du carré")
    ca = int(input("Entrez la taille d'un côté du carré : "))
    périmètre = ca * 4
    print("Le périmètre du carré est", périmètre)

def exercice16():
    print("Exercice 16 : Aire du carré")
    carr = int(input("Entrez la taille d'un côté du carré : "))
    aire = carr * 2
    print("Le aire du carré est", aire)

def exercice17():
    print("Exercice 17 : Conversion Euro en Dollar")
    euro = int(input("Entrez votre valeur en euro "))
    dollar = euro * 1.1
    print("La valeur de", euro, "€ est de", dollar, "$")

def exercice18():
    print("Exercice 18 : Conversion Minutes en secondes")
    minutes = int(input("Entrez votre valeur en minutes "))
    secondes = minutes * 60
    print(minutes, "minutes en secondes fais", secondes, "secondes")

def exercice19():
    print("Exercice 19 : Prix TTC")
    prixht = int(input("Entrez le PrixHT "))
    taxe = prixht * 1.2
    print("Avec la TVA, le PrixTTC est de", taxe, "€")
    
def exercice20():
    print("Exercice 20 : Message personalisée")
    nom = input("Entrez votre nom : ")
    âge = input("Entrez votre âge : ")
    print(nom, "a", âge, "ans")

def exercice21():
    print("Exercice 21 : Test Positif et Negatif")
    nombre = int(input("Entrez un nombre : "))
    if nombre < 0 :
        print(nombre, "est négatif")
    elif nombre == 0 :
        print(nombre, "est nul")
    elif nombre > 0 :
        print(nombre, "est positif")

def exercice22():
    print("Exercice 22 : Majeur ou Mineur")
    âge = int(input("Entrez un âge : "))
    if âge >= 18 :
        print("Vous êtes Majeur")
    else :
        print("Vous êtes Mineur")

def exercice23():
    print("Exercice 23 : Note validé")
    note = int(input("Entre une note : "))
    if note >= 10 :
        print("Félicitation ! Vous êtes Validé")
    else :
        print("Vous n'êtes pas Validé")

def exercice24():
    print("Exercice 24 : Plus Grand que")
    num1 = int(input("Entrez un nombre : "))
    num2 = int(input("Entrez un deuxième nombre : "))
    if num1 > num2 :
        print(num1, "est plus grand que ", num2)
    else :
        print(num2, "est plus grand que ", num1)

def exercice25():
    print("Exercice 25 : Ordre croissant")
    num1 = int(input("Entrez un nombre : "))
    num2 = int(input("Entrez un deuxième nombre : "))
    if num1 < num2 :
        print(num1, "et", num2, "sont dans l'ordre croissant")
    else :
        print(num1, "et", num2, "ne sont pas dans l'ordre croissant")

def exercice26():
    print("Exercice 26 : Divisible par 5")
    nombre = int(input("Entrez un nombre : "))
    if nombre % 5 == 0 :
                 print(nombre, "est divisible par 5")
    else :
        print (nombre, "n'est pas divisble par 5")

def exercice27():
    print("Exercice 27 : Catégorie d'âge")
    âge = int(input("Entrez un âge : "))
    if âge < 12 :
              print("Vous êtes un Enfant")
    elif âge >=18 :
        print("Vous êtes un Adulte")
    else :
        print("Vous êtes un Adolescent")

def exercice28():
    print("Exercice 28 : Température de l'eau")
    température_eau = int(input("Entrez la Température de l'eau : "))
    if température_eau < 0:
                          print("L'eau devient de la Glace")
    elif température_eau > 100:
        print("L'eau devient du Gaz")
    else :
        print("L'eau est liquide")

def exercice29():
    print("Exercice 29 : Mention au Bac")
    note = int(input("Entre une note : "))
    if note <= 8 :
        print("Recalé")
    elif note >= 9 and note <= 13 :
        print("Passable")
    elif note >=14 and note <= 16:
        print("Bien")
    else :
        print ("Très bien")

def exercice30():
    print("Exercice 30 : Comptez de 1 à N")
    n = int(input("Entrez un nombre : "))
    for i in range(1, n+1):
            print(i)
    
def exercice31():
    print("Exercice 31 : Compte à rebourd")
    n = int(input("Entrez un nombre : "))
    for i in reversed(range(1, n+1)):
        time.sleep(1)
        print(i)

def exercice32():
    print("Exercice 32 : Somme jusqu'à N")
    n = int(input("Entrez un nombre : "))
    s = 0
    for i in range(1, n+1):
        s += i
    print("S = ", s)

def exercice33():
    print("Exercice 33 : Table de multiplication")
    n = int(input("Entrez la table que vous voulez : "))
    for i in range(1, 11):
        print(i, "x ", n, "= ", i*n)

def exercice34():
    print("Exercice 34 : Nombre pairs jusqu'à N")
    n = int(input("Entrez un nombre : "))
    for i in range(1, n+1):
        if i % 2 == 0 :
            print(i)
        else :
            print("")

def exercice35():
    print("Exercice 35 : Carré Parfaits")
    n = int(input("Entrez la valeur que vous voulez : "))
    i=1
    while i*i < n :
        print(i*i)
        i = i+1

def exercice36():
    print("Exercice 36 : Répéter un mot")
    n = int(input("Entrez un nombre : "))
    i = 0
    while i < n :
        print("Bonjour !")
        i = i+1

def exercice37():
    print("Exercice 37 : Pyramide d'étoile")
    ligne = int(input("Entrez la taille de la pyramide : "))
    espace = ligne - 1
    étoile = 1
    for i in range(0, ligne):
        print(espace*" " + étoile*"*")
        espace -= 1
        étoile += 2

def exercice38():
    print("Exercice 38 : Calculatrice simple")

    print("  Veuillez taper dans le menu soit : 1 pour addition ou 2 pour soustraction ou 3 pour multiplication ou 4 pour division  ")
    menu = int(input("Choisissez l'opération faire : "))
    num1 = int(input("Entrez votre premier nombre : "))
    num2 = int(input("Entrez votre deuxième nombre : "))
    if menu == 1 :
        print(num1, "+ ", num2, "= ", num1+num2)
    elif menu == 2 :
        print(num1, "- ", num2, "= ", num1-num2)
    elif menu == 3 :
        print(num1, "x ", num2, "= ", num1*num2)
    elif menu == 4  :
        if num2 != 0 :
            print(num1, "/ ", num2, "= ", num1/num2)
        else :
            print("Erreur ! Vous ne pouvez pas divisez par 0")
    else :
        print("Vous n'avez rien choisit")

def exercice39():
    print("Exercice 39 : Pair ou Impair")
    nombre = random.randint(0, 100)
    choix  = input("Pair ou Impair  : ")
    if nombre % 2 == 0 and choix == 'Pair' :
        print("Bravo !!! le nombre était : ", nombre)
    elif nombre % 2 != 0 and choix == 'Impair':
        print("Bravo !!! le nombre était : ", nombre)
    else :
        print("Perdu, le nombre était : ", nombre)

def exercice40():
    print("Exercice 40 : Validation d'un mot de passe")
    mdp = input("Entrez un mot de passe : ")
    if len(mdp) < 6 :
        print("Non Validé, Trop Court !")
    else :
        print("Validé !")

def exercice41():
    print("Exercice 41 : Moyenne de 5 notes")
    note1 = int(input("Entrez la premier note : "))
    note2 = int(input("Entrez la deuxième note : "))
    note3 = int(input("Entrez la premier note : "))
    note4 = int(input("Entrez la deuxième note : "))
    note5 = int(input("Entrez la premier note : "))
    moyenne = (note1 + note2 + note3 + note4 + note5)/5
    print("La moyenne est de : ", moyenne)

def exercice42():
    print("Exercice 42 : Min et Max de 5 nombre")
    liste = [24,12,90,43,4]
    print("Le minimum de la liste est : ", min(liste))
    print("le maximum de la liste est ", max(liste))    

def exercice43():
    print("Exercice 43 : Compteur de voyelle")
    n = input("Entrez un mot (sans accent) : ")
    liste_voyelles=["a","e","i","o","u","y","A","E","I","O","U","Y"]
    voyelles = 0
    for lettre in n:
        if lettre in liste_voyelles:
            voyelles += 1

    if voyelles == 0 :
        print("Ce Mot ne comporte pas de voyelles")

    elif voyelles > 0 :
        print("Ce Mot comporte ",  voyelles, "voyelle(s)")

def exercice44():
    print("Exercice 44 : Mot inversés")
    n = input("Entrez un mot : ")
    mot_inversé = n[::-1]
    print(mot_inversé)

def exercice45():
    print("Exercice 45 : Somme d'une liste")
    liste = [4,7,9,13]
    print("La somme de la liste est", sum(liste))

def exercice46():
    print("Exercice 46 : Recherche dans une liste")
    liste = [4,2,11,0,5,9,7,19]
    chiffre = int(input("Demander si un nombre est dans la liste : "))
    if chiffre in liste :
                  print("Oui !, ", chiffre, "est bien dans la liste !")
    else :
        print("Non, ", chiffre, "n'est pas dans la liste !")

def exercice47():
    print("Exercice 47 : Compter les occurences")
    liste = [4,2,11,0,4,8,9,0,7,2,4,7,0,8,11,19,5,9,7,19]
    chiffre = int(input("Demander si un nombre est dans la liste : "))
    if chiffre in liste:
        print(chiffre, "apparait", liste.count(chiffre), "dans la liste")
    else :
        print(chiffre, "n'est pas dans la liste")

def exercice48():
    print("Exercice 48 : Liste des diviseurs")
    n = int(input("Entrez un nombre : "))
    for i in range(1,n+1):
        if n % i == 0 :
            print(i)

def exercice49():
    print("Exercice 49 : Nombre premier")
    n = int(input("Entrez un nombre : "))
    if n <=3 :
        print(n, "n'est pas un nombre premier")
        return
    a = 2
    while a < n and n % a != 0:
        a += 1

    if a == n:
        print(n, "est un nombre premier")
    else:
        print(n, "n'est pas un nombre premier")

def exercice50():
    print("Exercice 50 : Fibonacci jusqu'à N")
    n = int(input("Entrez la valeur que vous voulez : "))
    nombre0 = 0
    nombre1 = 1

    print(nombre0, ",", nombre1, end=", ") #end = copie une variable sur la même ligne
 
    for i in range(2, n):
      suivant = nombre0 + nombre1
      print(suivant, end=", ")
 
      nombre0 = nombre1
      nombre1 = suivant

def main():
    while True:
        print("\n=== Menu des exercices ===")
        print("q - Quitter")
        choix = input("Entrez le numéro de l'exercice à exécuter : ").strip().lower()

        if choix == "1":
            exercice1()
        elif choix == "2":
            exercice2()
        elif choix == "3":
            exercice3()
        elif choix == "4":
            exercice4()
        elif choix == "5":
            exercice5()
        elif choix == "6":
            exercice6()
        elif choix == "7":
            exercice7()
        elif choix == "8":
            exercice8()
        elif choix == "9":
            exercice9()
        elif choix == "10":
            exercice10()
        elif choix == "11":
            exercice11()
        elif choix == "12":
            exercice12()
        elif choix == "13":
            exercice13()
        elif choix == "14":
            exercice14()
        elif choix == "15":
            exercice15()
        elif choix == "16":
            exercice16()
        elif choix == "17":
            exercice17()
        elif choix == "18":
            exercice18()
        elif choix == "19":
            exercice19()
        elif choix == "20":
            exercice20()
        elif choix == "21":
            exercice21()
        elif choix == "22":
            exercice22()
        elif choix == "23":
            exercice23()
        elif choix == "24":
            exercice24()
        elif choix == "25":
            exercice25()
        elif choix == "26":
            exercice26()
        elif choix == "27":
            exercice27()
        elif choix == "28":
            exercice28()
        elif choix == "29":
            exercice29()
        elif choix == "30":
            exercice30()
        elif choix == "31":
            exercice31()
        elif choix == "32":
            exercice32()
        elif choix == "33":
            exercice33()
        elif choix == "34":
            exercice34()
        elif choix == "35":
            exercice35()
        elif choix == "36":
            exercice36()
        elif choix == "37":
            exercice37()
        elif choix == "38":
            exercice38()
        elif choix == "39":
            exercice39()
        elif choix == "40":
            exercice40()
        elif choix == "41":
            exercice41()
        elif choix == "42":
            exercice42()
        elif choix == "43":
            exercice43()
        elif choix == "44":
            exercice44()
        elif choix == "45":
            exercice45()
        elif choix == "46":
            exercice46()
        elif choix == "47":
            exercice47()
        elif choix == "48":
            exercice48()
        elif choix == "49":
            exercice49()
        elif choix == "50":
            exercice50()
        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")

        # Pause entre deux exécutions pour laisser le temps de lire
        input("\nAppuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()
