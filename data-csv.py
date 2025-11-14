import pandas as pd
import numpy as np
from PIL import Image, PngImagePlugin
import os

# ================================
# Création des dossiers challenges / outputs pour les csv de données / instructions
# ================================
os.makedirs("output", exist_ok=True)
os.makedirs("challenges", exist_ok=True)

# ================================
# 1 --> Génération du fichier des audiences 
# ================================
np.random.seed(42)
n = 5000

villes = [
    "Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Nantes",
    "Bordeaux", "Lille", "Rennes", "Strasbourg", "Montpellier",
    "Grenoble", "Dijon", "Angers", "Clermont-Ferrand", "Le Havre",
    "Saint-Étienne", "Toulon", "Le Mans", "Aix-en-Provence", "Brest",
    "Limoges", "Tours", "Amiens", "Perpignan", "Metz", "Besançon",
    "Orléans", "Mulhouse", "Rouen"
]

centres_interet = [
    "sport", "politique", "cosmétique", "crypto", "écologie", "automobile",
    "éducation", "technologie", "voyages", "musique", "cinéma",
    "santé", "gastronomie", "mode", "finance"
]

audience = pd.DataFrame({
    "user_id": np.arange(1, n+1),
    "age": np.random.randint(18, 70, n),
    "sexe": np.random.choice(["M", "F"], n),
    "ville": np.random.choice(villes, n),
    "centre_interet": np.random.choice(centres_interet, n),
    "score_persuasion": np.round(np.random.beta(2,5,n), 3)
})

audience.to_csv("output/audience.csv", index=False)

# ================================
# 2 --> Génération du fichier des messages
# ================================
np.random.seed(42)
n_messages = 30

themes = ["santé", "technologie", "écologie", "crypto", "mode", "sport", "politique", "éducation", "finance", "voyages"]
tons = ["neutre", "anxiogène", "positif", "autoritaire", "persuasif", "ironique"]
emotions = ["peur", "joie", "colère", "confiance", "surprise", "tristesse"]

contenus = [
    f"Découvrez comment {theme} peut radicalement transformer votre quotidien !" for theme in np.random.choice(themes, n_messages)
]

messages = pd.DataFrame({
    "message_id": [f"M{i}" for i in range(1, n_messages+1)],
    "contenu": contenus,
    "ton": np.random.choice(tons, n_messages),
    "emotion": np.random.choice(emotions, n_messages),
    "length": [len(c) for c in contenus],
    "theme": [c.split()[2] for c in contenus],
    "score_persuasion": np.round(np.random.uniform(0.3, 0.9, n_messages), 2)
})

messages.to_csv("output/messages.csv", index=False)

# ================================
# 3 --> Génération du fichier des engagements
# ================================
eng = pd.DataFrame({
    "message_id": messages["message_id"],
    "impressions": np.random.randint(1000, 20000, n_messages),
    "clics": np.random.randint(50, 2000, n_messages),
    "conversions": np.random.randint(10, 1000, n_messages),
})

eng.to_csv("output/engagements.csv", index=False)

# ================================
# 4 --> Génération du jeu de données micro-ciblées par utilisateur
# ================================
rows = 8000

ad = pd.DataFrame({
    "user_id": np.random.randint(1, n, rows),
    "message_id": np.random.choice(messages["message_id"], rows),
    "timestamp": pd.to_datetime(
        np.random.randint(1700000000, 1750000000, rows), unit='s'),
    "impression": 1,
    "share": np.random.choice([0,1], rows, p=[0.9, 0.1])
})

# anomaly row containing flag
anomaly = pd.DataFrame({
    "user_id": [999999],
    "message_id": ["FLAG{ANOMALY_DETECTED}"],
    "timestamp": [pd.Timestamp("2025-01-01")],
    "impression": [1],
    "share": [1]
})

ad = pd.concat([ad, anomaly], ignore_index=True)
ad.to_csv("output/ad_delivery.csv", index=False)

# ================================
# 5 --> Génération de l'image avec le flag
# ================================
img = Image.new("RGB", (400, 200), (255, 255, 255))
meta = PngImagePlugin.PngInfo()
meta.add_text("flag", "FLAG{HIDDEN_MESSAGE_OK}")
img.save("output/ad_image.png", "PNG", pnginfo=meta)

# ================================
# 6 --> Génération des fichiers d'instruction des challenges
# ================================
with open("challenges/challenge1_segmentation.md", "w") as f:
    f.write(
"""# 

Salut à toi jeune lycéen !

Voici ton premier challenge sur les méthodes de ciblage comportemental omniprésentes sur les RS et dans ton téléphone !
Notre premier point : la segmentation des données
Analyse le fichier que tu viens de créer `audience.csv` et identifie les trois segments présentant le score de persuasion (score_persuasion) moyen le plus élevé.
Le flag que l'on veut de toi : FLAG{SEG1-SEG2-SEG3}

""")

with open("challenges/challenge2_microtargeting.md", "w") as f:
    f.write(
"""# 

Here it is !

Re, analyste en herbe !

Ton deuxième défi porte sur le choix du message le plus efficace pour convaincre.
Analyse les fichiers `messages.csv` et `engagements.csv` : calcule le CTR (clic-through rate) et le taux de conversion pour chaque message.
Identifie le message ayant le meilleur impact comportemental.

Le flag que nous attendons : FLAG{MESSAGE_ID-X}

""")

with open("challenges/challenge3_propagation.md", "w") as f:
    f.write(
"""# 

Hey détective numérique !

Pour ce troisième challenge, tu vas jouer au chercheur d'anomalies.
Regarde dans `ad_delivery.csv` : il y a une ligne suspecte qui ne ressemble à aucune autre. 
Cette ligne représente une opération spéciale d’influence.
Ta mission : la retrouver.

Le flag est caché dans cette ligne.

""")


with open("challenges/challenge4_steganalysis.md", "w") as f:
    f.write(
"""# 

Salut explorateur du web !

Dernier challenge : de la stéganographie dans ton CTF !
Ouvre l'image `ad_image.png` et regarde ses métadonnées. 
Un flag y est caché pour tester ta capacité à détecter les informations invisibles.
Le flag que tu dois récupérer : FLAG{HIDDEN_MESSAGE_OK}

""")


print("La génération de ton challenge personnalisé est effectuée ! Les fichiers qui vont t'intéresser sont dans /output et /challenges")
