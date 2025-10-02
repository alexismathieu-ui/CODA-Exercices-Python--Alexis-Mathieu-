import time

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

def exercice33():
    print("Exercice 33 : Conversion Euro en Dollar")

def exercice34():
    print("Exercice 34 : Conversion Euro en Dollar")

def exercice35():
    print("Exercice 35 : Conversion Euro en Dollar")


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
        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")

        # Pause entre deux exécutions pour laisser le temps de lire
        input("\nAppuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()
