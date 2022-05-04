# -*- coding: utf-8 -*-
"""
Created on Wed May  4 01:18:25 2022

@author: vicgu
"""

import requests
import db
import os

# Création de la base et suppresion si le fichier existe deja
if "Brut.db" in os.listdir():
    os.remove("Brut.db")

db.create_base()

# URL pour la connection des API
url_api_pages = "http://127.0.0.1:5000/pages"
url_api_videos = "http://127.0.0.1:5000/videos"
url_api_insight = "http://127.0.0.1:5000/videos_insight"

# Données à inséré pour la page + insert des données
insert_pages = {"name": "OurMedia France"}

r = requests.post(url_api_pages,
                  data=insert_pages)

print(r.content)
print(r.ok)

# Données à inséré dans vidéos + insert des données
insert_videos = [
    {"title": "Video 1",
     "page_id": "1"},
    {"title": "Video 2",
     "page_id": "1"}
]

for videos in insert_videos:

    r = requests.post(url_api_videos,
                      data=videos)
    print(r.content)
    print(r.ok)

# Données à inséré dans vidéos insight + insert des données
insight_videos = [
    {"video_id": 1,
     "views": 1000,
     "likes": 100},
    {"video_id": 2,
     "views": 1000,
     "likes": 100}
]

for insight in insight_videos:

    r = requests.post(url_api_insight,
                      data=insight)
    print(r.content)
    print(r.ok)

# Données à supprimer suppression vidéo 2 plus les insight (normalement réalisé automatiquement par le mode CASCADE)
r = requests.delete(url_api_videos, data={"title": "Video 2"})
print(r.content)
print(r.ok)
r = requests.delete(url_api_insight, data={"title": "Video 2"})
print(r.content)
print(r.ok)
