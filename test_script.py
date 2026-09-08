from script import calculer_prix_final

# Cas 1: montant <= 0
def test_montant_negatif_ou_nul():
    assert calculer_prix_final(0) == "Erreur : Le montant doit etre strictement positif."

# Cas 2: montant > 1000
def test_montant_superieur_ou_egal_1000():
    assert calculer_prix_final(1000) == "Rabais applique (15%). Total a payer : 850.00 $"

# Cas 3: montant > 500
def test_montant_superieur_ou_egal_500():
    assert calculer_prix_final(500) == "Rabais applique (10%). Total a payer : 450.00 $"

# Cas 4: montant > 100
def test_montant_superieur_ou_egal_100():
    assert calculer_prix_final(100) == "Rabais applique (5%). Total a payer : 95.00 $"

# Cas 5: montant > 0 et < 100
def test_montant_sans_rabais():
    assert calculer_prix_final(25) == "Aucun rabais applicable. Total a payer : 25.00 $"
