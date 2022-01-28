# Créé par Titouan, le 27/01/2022 en Python 3.7
import os
import sys
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import time

df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16') #lire le fichier


ls_likes_tot = []
ls_likes_vrai =[]
ls_dislikes = []
plus = 0
moins = 0
somme = 0
ratio = 0
histo_plus = []
histo_moins = []

print("Début de la création des variables pour les figures")
#Boucles pour créer les liste et enlever les vidéos inutiles
for a in df['likes']:
    ls_likes_tot.append(a)
    index = len(ls_likes_tot) - 1
    if a == 0:
        if df.loc[index, 'dislikes'] == 0 :
            if df.loc[index, 'comments_disabled'] == True:
                pass
            else:
                ls_likes_vrai.append(a)
                ls_dislikes.append(df.loc[index, 'dislikes'])
        else:
            ls_likes_vrai.append(a)
            ls_dislikes.append(df.loc[index, 'dislikes'])
    else:
        ls_likes_vrai.append(a)
        ls_dislikes.append(df.loc[index, 'dislikes'])

#Boucle pour les diagrames
for b in range (len(ls_likes_vrai)):
    if ls_likes_vrai[b] >= ls_dislikes[b]:
        plus += 1
        somme = ls_likes_vrai[b] + ls_dislikes[b]
        if somme == 0:
            histo_plus.append(0)
        else:
            ratio = (100 / somme) * ls_likes_vrai[b]
            if ratio >= 90:
                histo_plus.append(90)
            elif 80 <= ratio < 90:
                histo_plus.append(80)
            elif 70 <= ratio < 80:
                histo_plus.append(70)
            elif 60 <= ratio < 70:
                histo_plus.append(60)
            else:
                histo_plus.append(50)
    else :
        moins += 1
        somme = ls_likes_vrai[b] + ls_dislikes[b]
        ratio = (100 / somme) * ls_dislikes[b]
        if ratio >= 90:
            histo_moins.append(90)
        elif 80 <= ratio < 90:
            histo_moins.append(80)
        elif 70 <= ratio < 80:
            histo_moins.append(70)
        elif 60 <= ratio < 70:
            histo_moins.append(60)
        else:
            histo_moins.append(50)

time.sleep(3)
print("Fin de la création des variables. Affichage des figure dans...")
for h in range (5,0,-1):
    print("{}...".format(h))
    time.sleep(1)

x1 = [plus, moins] #Valeurs pour le camembert
label1 = ["Video avec plus de likes que de dislikes", "video avec plus\n de dislikes que\n de likes"]

plt.subplot(1,2,1)
plt.pie(x1, labels=label1, explode=(0, 0.2), shadow=True, autopct='%1.1f%%')
plt.title("Pourcentage de vidéos avec plus de likes que de dislikes et vice-versa")

pl.subplot(2,2,2)
plt.hist(histo_plus)
plt.title("Vidéos qui ont plus de likes que de dislikes \n Vidéos avec un pourcentage de likes supérieur à 50, 60, 70, 80 et 90. Le zéro correspont aux vidéos qui n'ont ni likes ni dislikes.")

pl.subplot(2,2,4)
plt.hist(histo_moins)
plt.title("Vidéos qui ont plus de dislikes que de likes \n Vidéos avec un pourcentage de dislikes supérieur à 50, 60, 70, 80 et 90.")



plt.show()





