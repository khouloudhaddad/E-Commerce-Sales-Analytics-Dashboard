import numpy as np

np.random.seed(42)

Commande_ID = np.arange(1001, 15001)
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

