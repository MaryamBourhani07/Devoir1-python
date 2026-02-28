# Définition du mot de passe correct
mot_de_passe1 = "python123"
# Demande à l'utilisateur de saisir son mot de passe 
mot_de_passe = input("Entrez votre mot de passe : ")
# Boucle while qui continue tant que le mot de passe saisi est incorrect
while mot_de_passe != mot_de_passe1:
    # Message indiquant que le mot de passe est incorrect
    print("Mot de passe incorrect. Veuillez réessayer.")
    # Nouvelle demande de saisie du mot de passe
    mot_de_passe = input("Entrez votre mot de passe : ")
# Si la boucle est terminée, le mot de passe est correct
print("Mot de passe correct. Bienvenue !")
