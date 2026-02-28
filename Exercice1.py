# Demander l'âge à l'utilisateur
age = input(" votre âge est : ")

# Conversion en entier
age = int(age)

# Analyse de la catégorie d'âge
if age >= 0 and age <= 12:
    print("Vous êtes un Enfant.")
elif age >= 13 and age <= 17:
    print("Vous êtes un Adolescent.")
elif age >= 18 and age <= 64:
    print("Vous êtes un Adulte.")
elif age >= 65:
    print("Vous êtes un Senior.")
else:
    print("Âge invalide.")