# Créé par Titouan, le 26/01/2022 en Python 3.7
import os
import sys
import csv
import numpy as np
import pandas as pd

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
for a in df['video_id']:
    if len(a) != 11:
        vavi += 1
    else :
        pass

for b in df['trending_date']:
    date_split = b.split('.')
    date_split = list(map(int, date_split))
    if 17 <= date_split[0] <= 18 and 1 <= date_split[1] <= 31 and 1 <= date_split[2] <= 12:
        pass
    else :
        vatd += 1

for e in df['category_id']:
    if e not in id:
        vaci += 1


for f in df['publish_time']:
    if len(f) != 24:
        vapt += 1

for g in df['tags']:
    pass

for h in df['views']:
    if h < 0:
        vav += 1

for i in df['likes']:
    va_likes.append(i)
    if i < 0:
        val += 1

for j in df['dislikes']:
    va_dislikes.append(j)
    if j < 0:
        vadl += 1

for k in df['comment_count']:
    va_nb_comments.append(k)
    if k < 0:
        vacc += 1

for l in df['thumbnail_link']:
    if thumb_link in l:
        pass
    else :
        vatl += 1

for m in df['comments_disabled']:
    va_comments.append(m)
    if m != True and m != False :
        vacd += 1

for n in df['ratings_disabled']:
    va_rating.append(n)
    if n != True and n != False :
        vard += 1

for o in df['video_error_or_removed']:
    if o != True and o != False :
        vaveor += 1

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







