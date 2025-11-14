# HERE IS THE FUCKING BULLSHIT CTF MAN ! CTF — microciblage comportemental 🕵️‍♂️

## 🎯 Présentation du CTF

Bienvenue dans ce CTF sur ce que l'on appelle le **(micro)ciblage comportemental et l'usage des données dans le profilage des individus via leur activité numérique**.  
Au cours de ce défi, tu exploreras des jeux de données réalistes et découvriras les mécanismes permettant de **segmenter, microcibler et analyser des audiences**, exactement comme dans les campagnes d'influence / lobbying.

Ce CTF est autonome : aucun serveur ou installation complexe n’est nécessaire.  
Tous les fichiers sont fournis dans le dossier `output` et les épreuves dans le dossier `challenges` que tu vas toi-même créer au début du CTF.

## Prérequis

Pour résoudre ce CTF, tu auras besoin de :

- Python 3.x  
- Quelques bibliothèques Python (optionnel, seulement si tu veux manipuler les CSV) : _pip install pandas numpy pillow_
- Logiciel pour lire les CSV (Excel, LibreOffice, Google Sheets, ou Python/pandas)
- Logiciel pour inspecter les métadonnées des images (ex. ExifTool ou Python Pillow)

## Lancer ton CTF

Première étape : lancer ton fichier python à l'aide de la commande _python data-csv.py_
  
1️⃣ Partie 1 : L'exploration des données

_Ouvre output/audience.csv pour explorer les profils utilisateurs et leurs centres d’intérêt.

Ouvre output/messages.csv pour analyser les messages publicitaires.

Ouvre output/engagements.csv pour comprendre le taux de clics et de conversions.

Ouvre output/ad_delivery.csv pour observer l’historique des impressions publicitaires.

Inspecte output/ad_image.png pour le challenge de stéganographie._

2️⃣ Lis les énoncés des challenges

Tous les challenges sont dans le dossier challenges/.

Lis chaque fichier Markdown pour comprendre ce que l’on attend de toi.

3️⃣ C'est à toi de jouer !

_Lis les consignes pour chaque challenge._

4️⃣ Si tu as réussi...

_Chaque challenge possède un flag de la forme FLAG{...}.

Exemple : FLAG{SEG1-SEG2-SEG3}_

## Quelques conseils

Python et pandas permettent d’analyser rapidement les CSV :

_import pandas as pd

audience = pd.read_csv("output/audience.csv")
messages = pd.read_csv("output/messages.csv")
eng = pd.read_csv("output/engagements.csv")
ad_delivery = pd.read_csv("output/ad_delivery.csv")_

# Un exemple : trouver les segments avec score_persuasion moyen le plus élevé
_audience.groupby("centre_interet")["score_persuasion"].mean().sort_values(ascending=False)_

Pour le challenge de stéganographie :

_from PIL import Image, PngImagePlugin

img = Image.open("output/ad_image.png")
print(img.info)_

## Notre objectif pédagogique :

Ce CTF a pour bit de te permettre de :

_Comprendre comment segmenter des audiences et analyser leurs comportements

Étudier l’efficacité des messages publicitaires

Détecter des anomalies dans la diffusion de messages

Découvrir la stéganographie et l’insertion de données cachées_


## Bonne chance et amuse-toi bien jeune padawan !

