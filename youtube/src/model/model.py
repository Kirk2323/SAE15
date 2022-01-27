import os
import sys
import csv
import numpy as np
import pandas as pd


def ComputeMean():
    tab_likes = []
    tab_dislikes = []
    nbrtotdl = 0
    nbrtotl = 0
    moyenne_likes = 0 #variable pour la moyenne de likes
    moyenne_dislikes = 0  # variable pour la moyenne de dislikes
    cl = 0 #compteur pour calculer la moyenne
    df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16') #lire le fichier

    for nl in df['likes']:
        nbrtotl += nl
        cl += 1
        tab_likes.append(nl)

    for ndl in df['dislikes']:
        nbrtotdl += ndl
        tab_dislikes.append(ndl)

    moyenne_likes = nbrtotl / cl
    moyenne_dislikes = nbrtotdl / cl

    return moyenne_likes, moyenne_dislikes, tab_likes, tab_dislikes, nbrtotl, nbrtotdl

def ComputeMedian(tab_likes, tab_dislikes):

    mediane_likes = 0
    mediane_dislikes = 0
    df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16')


    tab_likes.sort()
    tab_dislikes.sort()

    a = len(tab_likes) / 2
    b = len (tab_dislikes) / 2

    mediane_likes = tab_likes[int(a)]
    mediane_dislikes = tab_dislikes[int(a)]

    return mediane_likes, mediane_dislikes
    
    
df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16')

moyenne_likes,moyenne_dislikes, tab_likes, tab_dislikes, nbrtotl, nbrtotdl = ComputeMean()
for i in range (5):
    maxi = max(tab_likes)
    index = tab_likes.index(maxi)
    nom_video = df.loc[index,'title']
    nbr_likes = df.loc[index,'likes']
    print("La videos avec le plus de likes N°{} est la vidéo '{}' avec {} likes".format(i+1,nom_video,nbr_likes))
    tab_likes[index] = 0


print("\n le nombre de total de likes est de {} likes".format(nbrtotl))
print("le nombre de total de dislikes est de {} dislikes\n".format(nbrtotdl))

mediane_likes, mediane_dislikes = ComputeMedian(tab_likes, tab_dislikes)

print("La moyenne de likes des vidéos YouTube est de {:.2f} likes, (arrondi au centième)".format(moyenne_likes))
print("La moyenne de dislikes des vidéos YouTube est de {:.2f} dislikes, (arrondi au centième)\n".format(moyenne_dislikes))
print("La valeur médiane des likes se situe à {} likes, cela signifie que la moitié des vidéos analysées "
      "ont un nombre de likes inférieur à  cette valeur et l'autre moitié un nombre supérieur à cette valeur".format(mediane_likes))
print("La valeur médiane des dislikes se situe à {} dislikes, cela signifie que la moitié des vidéos analysées "
      "ont un nombre de dislikes inférieur à  cette valeur et l'autre moitié un nombre supérieur à cette valeur".format(mediane_dislikes))


