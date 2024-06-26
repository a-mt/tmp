prix_metre_carre = 260
superficie_maison = 250
prix_total = prix_metre_carre + superficie_maison

print("Le prix de la maison:", prix_total)
print(type(prix_total))
prix_total = 123.45
print(type(prix_total))

nom = "Mistri"
prenom = "Aurelie"
memo = '''
Ligne A
Ligne B
Ligne C
'''
age = 12
print(nom, prenom, age, memo)

chaine = nom + " - " + prenom + " - " + str(age) + "ans - " + " - " + memo
print(chaine)

chaine = f"{nom} - {prenom} - {age} ans - {memo}"
print(chaine)

var1, var2 = "value1", "value2"
print(var1, var2)

x = 0
if x < 0:
    print("x est négatif")
elif x == 0:
    print("x est null")
else:
    print("x est positif")

liste = [2, -3, 8, 12, -4]
print(liste)
print(liste[:2])
print(liste[2:])

liste[2:4] = [0, 1]
print(liste)