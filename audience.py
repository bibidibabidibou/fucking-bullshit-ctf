import pandas as pd
import numpy as np
from PIL import Image, PngImagePlugin

# generate audience.csv
np.random.seed(0)
n=5000
audience = pd.DataFrame({
    "user_id": np.arange(1,n+1),
    "age": np.random.randint(18,70,n),
    "sexe": np.random.choice(["M","F"], n),
    "ville": np.random.choice(["Paris","Lyon","Marseille","Toulouse","Nice","Nantes"], n),
    "centre_interet": np.random.choice(
        ["sport","politique","cosmétique","crypto","écologie","automobile","éducation"], n),
    "score_persuasion": np.round(np.random.beta(2,5,n),3)
})
audience.to_csv("/mnt/data/audience.csv", index=False)

# messages.csv
messages = pd.DataFrame({
    "message_id":[f"M{i}" for i in range(1,16)],
    "contenu":[f"Message publicitaire {i}" for i in range(1,16)],
    "ton": np.random.choice(["neutre","anxiogène","positif","autoritaire"],15),
    "emotion": np.random.choice(["peur","joie","colère","confiance"],15)
})
messages.to_csv("/mnt/data/messages.csv", index=False)

# engagements.csv
eng = pd.DataFrame({
    "message_id": messages["message_id"],
    "impressions": np.random.randint(1000,20000,15),
    "clics": np.random.randint(50,2000,15),
    "conversions": np.random.randint(10,1000,15)
})
eng.to_csv("/mnt/data/engagements.csv", index=False)

# ad_delivery.csv
rows=8000
ad = pd.DataFrame({
    "user_id": np.random.randint(1,n,rows),
    "message_id": np.random.choice(messages["message_id"], rows),
    "timestamp": pd.to_datetime(
        np.random.randint(1700000000, 1750000000, rows), unit='s'),
    "impression": 1,
    "share": np.random.choice([0,1], rows, p=[0.9,0.1])
})
# Insert anomaly row with flag
anomaly = pd.DataFrame({
    "user_id":[999999],
    "message_id":["M99"],
    "timestamp":[pd.Timestamp("2025-01-01")],
    "impression":[1],
    "share":[1]
})
ad = pd.concat([ad, anomaly], ignore_index=True)
ad.to_csv("/mnt/data/ad_delivery.csv", index=False)

# create stego image
img = Image.new("RGB",(400,200),(255,255,255))
meta = PngImagePlugin.PngInfo()
meta.add_text("flag","FLAG{HIDDEN_MESSAGE_OK}")
img.save("/mnt/data/ad_image.png","PNG", pnginfo=meta)

# create markdown challenge statements
ch1 = """# Challenge 1 — Segmentation
Analyse `audience.csv` et identifie les trois segments ayant le plus haut score_persuasion moyen.
Format du flag : FLAG{SEG1-SEG2-SEG3}"""
with open("/mnt/data/challenge1_segmentation.md","w") as f: f.write(ch1)

ch2 = """# Challenge 2 — Message optimal
Analyse `messages.csv` et `engagements.csv`, calcule CTR & taux de conversion.
Trouve le message avec le ROI comportemental maximal.
Flag : FLAG{MESSAGE_ID-X}"""
with open("/mnt/data/challenge2_microtargeting.md","w") as f: f.write(ch2)

ch3 = """# Challenge 3 — Propagation
Analyse `ad_delivery.csv`, détecte une ligne anormale liée à une opération d'influence.
Flag présent dans la ligne anormale."""
with open("/mnt/data/challenge3_propagation.md","w") as f: f.write(ch3)

ch4 = """# Challenge 4 — Stéganographie
L'image `ad_image.png` contient un flag dans ses métadonnées.
Flag : FLAG{HIDDEN_MESSAGE_OK}"""
with open("/mnt/data/challenge4_steganalysis.md","w") as f: f.write(ch4)

"/mnt/data"
