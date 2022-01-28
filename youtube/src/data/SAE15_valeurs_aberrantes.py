# Créé par Titouan, le 26/01/2022 en Python 3.7
import os
import sys
import csv
import numpy as np
import pandas as pd
import time
import pyexcel
from pyexcel.cookbook import merge_all_to_a_book

df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16', sep=",")
#print(df.info()) #afficher les informations sur le fichier

#création des variables
va = 0 #Somme des valeurs aberrantes
vavi = 0 #Valeurs aberrantes des video_ID
vatd = 0 #Valeurs aberrantes des trending_date
vaci = 0 #Valeurs aberrantes des category_id
vapt = 0 #Valeurs aberrantes des publish_time
vata = 0 #Valeurs aberranetes des tags
vav = 0 #Valeurs aberrantes des views
val = 0 #Valeurs aberrantes des likes
vadl = 0 #Valeurs aberrantes des dislikes
vacc = 0 #Valeurs aberrantes des comment_count
vatl = 0 #valeurs aberrantes des thumbnail_link
vacd = 0 #Valeurs aberrantes des comments disabled
vard = 0 #Valeurs aberrantes des ratings_disabled
vaveor = 0 #Valeurs aberrantes des video_error_or_removed
va_likes = [] #tableau pour comparer les likes à zéro et la colonne rating_disabled
va_dislikes = [] #tableau pour comparer les dislikes à zéro et la colonne rating_disabled
va_rating = [] #tableau pour comparer les True / False avec les likes et les dislikes
va_nb_comments = [] #Tableau pour comparer les nombres de commentaires avec la colonne comments_disabled
va_comments = [] #tableau pour comparer les True / False avec lenombre de commentaires
id = [1,2,10,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44] #Liste pour vérifier les ID YouTube
thumb_link = 'https://i.ytimg.com/vi/' #chaine de caractères pour vérifier les liens thumbnails
#Il n'ya pas de variables pour les titres des vidéos et pour les titres de chaine YouTube car il est difficile d'analyser des chaine arabes ou chinoises mais
#surtout car un titre contient ce que l'on veut et l'on considère qu'il n'ya rien d'aberrant dedans

#Analyse des ID youtubes
print("Analyse de la colonne 'video_id'")
for a in df['video_id']:
    if len(a) != 11:
        vavi += 1
    else :
        pass
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vavi))
time.sleep(2)
print("Analyse de la colonne 'trending_date'")
for b in df['trending_date']:
    date_split = b.split('.')
    date_split = list(map(int, date_split))
    if 17 <= date_split[0] <= 18 and 1 <= date_split[1] <= 31 and 1 <= date_split[2] <= 12:
        pass
    else :
        vatd += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vatd))
time.sleep(2)
print("Analyse de la colonne 'category_id'")
for e in df['category_id']:
    if e not in id:
        vaci += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vaci))
time.sleep(2)
print("Analyse de la colonne 'publish_time'")
for f in df['publish_time']:
    if len(f) != 24:
        vapt += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vapt))
time.sleep(2)
print("Analyse de la colonne 'tags'")
for g in df['tags']:
    pass
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vata))
time.sleep(2)
print("Analyse de la colonne 'views'")
for h in df['views']:
    if h < 0:
        vav += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vav))
time.sleep(2)
print("Analyse de la colonne 'likes'")
for i in df['likes']:
    va_likes.append(i)
    if i < 0:
        val += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(val))
time.sleep(2)
print("Analyse de la colonne 'dislikes'")
for j in df['dislikes']:
    va_dislikes.append(j)
    if j < 0:
        vadl += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vadl))
time.sleep(2)
print("Analyse de la colonne 'comment_count'")
for k in df['comment_count']:
    va_nb_comments.append(k)
    if k < 0:
        vacc += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vacc))
time.sleep(2)
print("Analyse de la colonne 'thumbnail_link'")
for l in df['thumbnail_link']:
    if thumb_link in l:
        pass
    else :
        vatl += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vatl))
time.sleep(2)
print("Analyse de la colonne 'comments_disabled'")
for m in df['comments_disabled']:
    va_comments.append(m)
    if m != True and m != False :
        vacd += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vacd))
time.sleep(2)
print("Analyse de la colonne 'ratings_disabled'")
for n in df['ratings_disabled']:
    va_rating.append(n)
    if n != True and n != False :
        vard += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vard))
time.sleep(2)
print("Analyse de la colonne 'video_error_or_removed'")
for o in df['video_error_or_removed']:
    if o != True and o != False :
        vaveor += 1
print("Après analyse, nous avons trouvé {} valeurs aberrantes dans cette colonne\n".format(vaveor))
time.sleep(2)

print("Analyse de la cohérence entre la colonne 'comments_disabled' et le nombre de likes / dislikes")
for p in range(len(df)):
    if va_rating[p] == True:
        if va_likes[p] == 0 and va_dislikes[p] == 0:
            pass
        elif va_likes[p] !=0 and va_dislikes[p] == 0:
            val += 1
        elif va_likes[p] ==0 and va_dislikes[p] != 0:
            vadl += 1
        else:
            val += 1
            vadl += 1
    else:
        pass

for q in range(len(df)):
    if va_comments[q] == True:
        if va_nb_comments[q] == 0:
            pass
        else:
            vacc += 1
    else:
        pass
print("Après deuxième analyse nous avons trouvé {} incohérences pour les likes et {} pour les dislikes".format(val, vadl))
time.sleep(2)
va = vadl + val + vacc + vard + vaveor + vav + vata + vapt + vacd + vaci + vatd + vavi + vatl

print("Après analyse complète du fichier nous avons trouvé {} valeurs aberrantes. Nous pouvons passer à la convertion du fichier csv en fichier excel avec un affichage lisible\n".format(va))
print("Début de la convertion vers fichier excel\n")
sheet = pyexcel.get_sheet(file_name="../../data/processed/compil.csv", delimiter=",", encoding='utf-16')
sheet.save_as("../../data/cleaned/propre.xlsx")
print("Fin de la convertion")