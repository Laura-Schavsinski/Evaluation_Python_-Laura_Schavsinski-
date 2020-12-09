from colorama import init				#
init()									#Couleur du texte (pas essayer) -> fore, permet de changer la couleur du background
from colorama import Fore, Back, Style	#

chance=8 #nombre de chance
findefaite=(chance==0)	#Défaite
motfin=(motadeviner==finvictoire) #Réussite

from random import randrange										#
list = ['BANQUE', 'AIRBUS', 'CAMERA', 'DEVOIR', 'FABLES', 'PLANTE']	#Choisir un mot random pour le motus (fonctionne)/print(list[motliste])
motliste = randrange(len(list))										#

print("Motus, veuillez choisir votre mot vous avez", chance, "chance pour trouver votre mot.")	#
print("Le mot à deviner fait 6 lettres")														#Print, fait apparaitre le texte (fonctionne)
print("_ _ _ _ _ _")																			#

mottest=input()	#Le joueur va écrire le mot qu'il pense être correcte (à replacer)

def motadeviner():

while findefaite or finvictoire:
								#manque un truc ici, mais quoi ?
print("Veuillez choisir un autre mot, il vous reste ", chance, "chance pour trouver votre mot")
  motadeviner=input()
  motadeviner=list(motadeviner)
  chance=chance-1
   
if findefaite:
  print("Perdu, le mot etait :", motliste)	#Vérifier motliste ne donne pas un mot au hasard different que celui de base (debut du code)
   
if finvictoire:
  print("Bravo vous avez trouvé le mot :", motliste) #Voir plus haut
