#Importer les bibliothèques
import os
import sys
import csv
import numpy as np
import pandas as pd

# Ouvrir le dossiers avec les fichiers et lister les fichiers
path = '../../data/raw/'
dirs = os.listdir(path)


#créer le fichier qui va recevoir la fusion
compil = open('../../data/processed/compil.csv', "r+", encoding='utf-16')


#A partir de la liste des fixhiers, les ouvrir un par un, lire chacune des lignes et les écrire dans le fichier crée en amont
for x in dirs:
    print(x)
    with open('../../data/raw/' + x, encoding='utf8') as csvfile:
        lignes = csvfile.readlines()
        for l in lignes:
            #print(l)
            compil.write(l)

#fermer le fichier
compil.close()

#lire le fichier en mode csv, supprimer la colonne desciption qui pose problème puis réécrire le fichier
df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16')
del df['description']
df.to_csv('../../data/processed/compil.csv', encoding='utf-16', index=True)
df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16', sep=",")

#print(df['likes'].nlargest(5))