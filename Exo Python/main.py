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
    âge = int(input("Entrez votre année de naissance : "))
    calcule_année = 2025 - âge
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
    for i in range(1, 5)
    print(i)

def exercice14():
    print("Exercice 14 : Moitié d'un nombre")

def exercice15():
    print("Exercice 15 : Moitié d'un nombre")

def exercice16():
    print("Exercice 16 : Moitié d'un nombre")

def exercice17():
    print("Exercice 17 : Moitié d'un nombre")

def exercice18():
    print("Exercice 18 : Moitié d'un nombre")

def exercice19():
    print("Exercice 19 : Moitié d'un nombre")

def exercice20():
    print("Exercice 20 : Moitié d'un nombre")

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
        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")

        # Pause entre deux exécutions pour laisser le temps de lire
        input("\nAppuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()
