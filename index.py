import numpy as np
import pandas as pd

# Exercice 1: Numppy
np.random.seed(42)

Commande_ID = np.arange(1001, 1501)
print(f"Commande_ID: {Commande_ID}")


Prix_Unitaire = np.round(
    np.random.uniform(15, 150, 500),
    2
)
print(f"Prix_Unitaire: {Prix_Unitaire}")

Quantite = np.random.randint(1, 6, 500)
print(f"Quantite: {Quantite}")

Frais_Livraison = np.abs(
    np.random.normal(loc=8.0, scale=2.0, size=500)
)
print(f"Frais_Livraison: {Frais_Livraison}")

Satisfaction_Client = np.random.randint(1, 6, 500).astype(float)

indices_nan = np.random.choice(500, size=25, replace=False)
Satisfaction_Client[indices_nan] = np.nan
print(f"Satisfaction_Client: {Satisfaction_Client}")

# Exercice 2: Pandas
df_ventes = pd.DataFrame({
    "Commande_ID": Commande_ID,
    "Prix_Unitaire": Prix_Unitaire,
    "Quantite": Quantite,
    "Frais_Livraison": Frais_Livraison, 
    "Satisfaction_Client": Satisfaction_Client
})
print(df_ventes.head())

categories = [
    "Électronique",
    "Vêtements",
    "Maison",
    "Livres"
]

modes_livraison = [
    "Standard",
    "Express",
    "Point Relais"
]

# Une catégorie aléatoire pour chaque commande
df_ventes["Categorie"] = np.random.choice(
    categories,
    size=500
)

# Un mode de livraison aléatoire pour chaque commande
df_ventes["Mode_Livraison"] = np.random.choice(
    modes_livraison,
    size=500
)

df_ventes["Montant_Total"] = (
    df_ventes["Prix_Unitaire"] * df_ventes["Quantite"]
    + df_ventes["Frais_Livraison"]
)

df_ventes["Satisfaction_Client"] = (
    df_ventes
    .groupby("Categorie")["Satisfaction_Client"]
    .transform(
        lambda x: x.fillna(x.median())
    )
)

print(df_ventes.head())

print("\nDimensions du DataFrame :")
print(df_ventes.shape)

print("\nValeurs manquantes :")
print(df_ventes.isna().sum())


