import os
import sys
import csv
import numpy as np
import pandas as pd
import time

def ComputeMean(): #création de la fonction moyenne
    tab_likes = []
    tab_dislikes = [] #tableaux pour faire la médiane par la suite et trouver les 5 vidéos avec le plus de likes
    nbrtotdl = 0 #variables avec le nombre total de likes / dislikes
    nbrtotl = 0
    moyenne_likes = 0 #variable pour la moyenne de likes
    moyenne_dislikes = 0  # variable pour la moyenne de dislikes
    cl = 0 #compteur pour calculer la moyenne
    df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16') #lire le fichier

    for nl in df['likes']: #lire la colonne des likes, en faire la somme et le mettre a la suite dans un tableau et faire un compteur pour la moyenne
        nbrtotl += nl
        cl += 1
        tab_likes.append(nl)

    for ndl in df['dislikes']: #faire comme pour les likes mais avec les dislikes, le compteur est déha créé
        nbrtotdl += ndl
        tab_dislikes.append(ndl)

    moyenne_likes = nbrtotl / cl #calculer les moyenne
    moyenne_dislikes = nbrtotdl / cl

    return moyenne_likes, moyenne_dislikes, tab_likes, tab_dislikes, nbrtotl, nbrtotdl #renvoyer les valeurs demandées

def ComputeMedian(tab_likes, tab_dislikes): #création de la fonction médianne avec les listes des likes et des dislikes en argument

    mediane_likes = 0 #initialiser les variables
    mediane_dislikes = 0
    df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16') #lire le fichier


    tab_likes.sort() #trier les liste pour trouver la médiane
    tab_dislikes.sort()

    a = len(tab_likes) // 2 #trouver l'index de la médianne du tableau de valeurs
    b = len (tab_dislikes) // 2

    if not len(tab_likes) % 2: #calculer les médianes
        mediane_likes = (tab_likes[a-1] + tab_likes[a]) / 2
    else:
        mediane_likes = tab_likes[a]

    if not len(tab_dislikes) % 2:
        mediane_dislikes = (tab_dislikes[b-1] + tab_dislikes[b]) / 2
    else:
        mediane_dislikes = tab_dislikes[b]

    return mediane_likes, mediane_dislikes #retourner les valeurs des médianes


df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16')#lire le fichier

print("Début du processus du calcul du top 5 des vidéos les plus likés, de moyenne et de médianne des likes / dislikes\n")
moyenne_likes,moyenne_dislikes, tab_likes, tab_dislikes, nbrtotl, nbrtotdl = ComputeMean() #récupérer les valeurs pour les moyennes et le top 5 des vidéos
time.sleep(2)
print("Présentation du top 5 des vidéos les plus likés : \n")
time.sleep(3)
for i in range (5): #Trouver les 5 vidéos les plus likés grâce à leur index dans la liste des likes totaux
    time.sleep(1)
    maxi = max(tab_likes)
    index = tab_likes.index(maxi)
    nom_video = df.loc[index,'title']
    nbr_likes = df.loc[index,'likes']
    print("La videos avec le plus de likes N°{} est la vidéo '{}' avec {} likes".format(i+1,nom_video,nbr_likes))
    tab_likes[index] = 0

print("Présentation du nombre total de likes / dislikes :\n")
time.sleep(2)
print("le nombre de total de likes est de {} likes".format(nbrtotl))#Donner le nombre total de likes et de dislikes
time.sleep(1)
print("le nombre de total de dislikes est de {} dislikes\n".format(nbrtotdl))
time.sleep(1)
mediane_likes, mediane_dislikes = ComputeMedian(tab_likes, tab_dislikes)#récupérer les valeurs pour les médianes
print("Présentation des moyennes de likes / dislike :\n")
time.sleep(2)
print("La moyenne de likes des vidéos YouTube est de {:.2f} likes, (arrondi au centième)".format(moyenne_likes))#afficher les moyennes
time.sleep(1)
print("La moyenne de dislikes des vidéos YouTube est de {:.2f} dislikes, (arrondi au centième)\n".format(moyenne_dislikes))

print("Présentation des médiannes de likes / dislike :\n")
time.sleep(2)
print("La valeur médiane des likes se situe à {} likes, cela signifie que la moitié des vidéos analysées "
      "ont un nombre de likes inférieur à  cette valeur et l'autre moitié un nombre supérieur à cette valeur".format(mediane_likes))
time.sleep(1)
print("La valeur médiane des dislikes se situe à {} dislikes, cela signifie que la moitié des vidéos analysées "
      "ont un nombre de dislikes inférieur à  cette valeur et l'autre moitié un nombre supérieur à cette valeur".format(mediane_dislikes))#afficher les médianes


