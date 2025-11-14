import pandas as pd
import numpy as np
from PIL import Image, PngImagePlugin
import os

# ================================
# CREATE OUTPUT FOLDERS
# ================================
os.makedirs("output", exist_ok=True)
os.makedirs("challenges", exist_ok=True)

# ================================
# 1. GENERATE audience.csv
# ================================
np.random.seed(42)
n = 5000

audience = pd.DataFrame({
    "user_id": np.arange(1, n+1),
    "age": np.random.randint(18, 70, n),
    "sexe": np.random.choice(["M", "F"], n),
    "ville": np.random.choice(["Paris","Lyon","Marseille","Toulouse","Nice","Nantes"], n),
    "centre_interet": np.random.choice(
        ["sport","politique","cosmétique","crypto","écologie","automobile","éducation"], n),
    "score_persuasion": np.round(np.random.beta(2,5,n), 3)
})

audience.to_csv("output/audience.csv", index=False)


# ================================
# 2. GENERATE messages.csv
# ================================
messages = pd.DataFrame({
    "message_id": [f"M{i}" for i in range(1, 16)],
    "contenu": [f"Message publicitaire {i}" for i in range(1, 16)],
    "ton": np.random.choice(["neutre", "anxiogène", "positif", "autoritaire"], 15),
    "emotion": np.random.choice(["peur", "joie", "colère", "confiance"], 15),
})

messages.to_csv("output/messages.csv", index=False)


# ================================
# 3. GENERATE engagements.csv
# ================================
eng = pd.DataFrame({
    "message_id": messages["message_id"],
    "impressions": np.random.randint(1000, 20000, 15),
    "clics": np.random.randint(50, 2000, 15),
    "conversions": np.random.randint(10, 1000, 15),
})

eng.to_csv("output/engagements.csv", index=False)


# ================================
# 4. GENERATE ad_delivery.csv
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
# 5. GENERATE STEGO IMAGE
# ================================
img = Image.new("RGB", (400, 200), (255, 255, 255))
meta = PngImagePlugin.PngInfo()
meta.add_text("flag", "FLAG{HIDDEN_MESSAGE_OK}")

img.save("output/ad_image.png", "PNG", pnginfo=meta)


# ================================
# 6. GENERATE CHALLENGE STATEMENTS
# ================================
with open("challenges/challenge1_segmentation.md", "w") as f:
    f.write(
"""# Challenge 1 — Segmentation
Analyse `audience.csv` et identifie les trois segments présentant le score_persuasion moyen le plus élevé.
Flag: FLAG{SEG1-SEG2-SEG3}
""")

with open("challenges/challenge2_microtargeting.md", "w") as f:
    f.write(
"""# Challenge 2 — Message optimal
Analyse `messages.csv` et `engagements.csv`. Calcule CTR et taux de conversion.
Trouve le message le plus performant.
Flag: FLAG{MESSAGE_ID-X}
""")

with open("challenges/challenge3_propagation.md", "w") as f:
    f.write(
"""# Challenge 3 — Propagation
Analyse `ad_delivery.csv`.
Trouve la ligne anormale contenant un message_id différent des autres.
Flag inclus dans la ligne.
""")

with open("challenges/challenge4_steganalysis.md", "w") as f:
    f.write(
"""# Challenge 4 — Stéganographie
L'image `ad_image.png` contient un flag dans ses métadonnées PNG.
Flag: FLAG{HIDDEN_MESSAGE_OK}
""")

print("CTF generation complete! Files saved in /output and /challenges")
