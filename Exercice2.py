# Création d'une liste vide pour stocker les contacts
Contacts= []
# Définition d'une fonction qui affiche le menu
def Menu():
    print("=========MENU CARNET D'ADRESSES=========")
    print("1. Ajouter un contact.")
    print("2.Afficher les contacts.")
    print("3.Quitter.")
 
    
# Boucle infinie pour garder le menu actif jusqu'à ce que l'utilisateur quitte     
while True:
    # Appel de la fonction Menu pour afficher les options
    Menu()
    # Demander à l'utilisateur de saisir son choix et le convertir en entier
    chois=int(input("Entrer votre choix : "))
    if chois==1:
        nom=input("Entrer le nom du contact :  ")
        Contacts.append(nom)
        print("contact ajouter avec succes")
    elif chois==2:
        if len(Contacts)==0:
            print("Aucun contact trouvé.")
        else:
            print("\nListe des contacts :")
            for index, contact in enumerate(Contacts, start=1):
                print(f"{index}. {contact}") 
    elif chois==3:
        print("Au revoir !")
        break
        
    else:
        print("Choix invalide. Veuillez réessayer.")  
