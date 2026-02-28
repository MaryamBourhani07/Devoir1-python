# Définition de la fonction qui affiche le menu des opérations
def menu(): 
    print("=========MENU CALCULATRICE=========")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
# Définition des fonctions pour chaque opération
def addition(x, y):
    return x + y
def soustraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y!=0:
        return x / y
    else:
        return "Erreur : Division par zéro impossible"
    
while True: 

    menu()
    # Demande à l'utilisateur les deux nombres et le choix de l'opération
    a=int(input("Entrer le premiere nombre :"))
    b=int(input("Entrer le deuxieme nombre :"))
    choix=int(input("Entrer votre choix :"))
    # Utilisation de match-case pour traiter le choix
    match choix:
        case 1:
            print("Resultat : ", addition(a, b))
            
        case 2:           
             print("Resultat : ", soustraction(a, b))
             
        case 3:            
             print("Resultat : ", multiplication(a, b))
             
        case 4:           
            print("Resultat : ", division(a, b))
            

        case 5:            
            print("Arrêter le programme.")
            
            

            