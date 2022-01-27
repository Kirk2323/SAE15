# Créé par Titouan, le 26/01/2022 en Python 3.7
import os
import sys
import csv
import numpy as np
import pandas as pd

df = pd.read_csv('../../data/processed/compil.csv', encoding='utf-16', sep=",")
#print(df.info()) #afficher les informations sur le fichier

#création des variables
vavi = 0 #Valeurs aberrantes des video_ID
vatd = 0 #Valeurs aberrantes des trending_date
vati = 0 #Valeurs aberrantes des title
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
id = [1,2,10,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44] #Liste pour vérifier les ID YouTube

#Analyse des ID youtubes
for a in df['video_id']:
    if len(a) != 11:
        vavi += 1
    else :
        pass

for b in df['trending_date']:
    pass

for c in df['title']:
    pass

for d in df['channel_title']:
    pass

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
    if k < 0:
        vacc += 1

for l in df['thumbnail_link']:
    pass

for m in df['comments_disabled']:
    pass

for n in df['ratings_disabled']:
    va_rating.append(n)


for o in df['video_error_or_removed']:
    pass


for p in range(len(df)):
    if va_likes == 0:
        if va_rating == True:
            pass
        else:
            val += 1
    else:
        pass


