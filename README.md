# FactPulse SDK Python

Client Python officiel pour l'API FactPulse - Facturation électronique française.

## 🎯 Fonctionnalités

- **Factur-X** : Génération et validation de factures électroniques (profils MINIMUM, BASIC, EN16931, EXTENDED)
- **Chorus Pro** : Intégration avec la plateforme de facturation publique française
- **AFNOR PDP/PA** : Soumission de flux conformes à la norme XP Z12-013
- **Signature électronique** : Signature PDF (PAdES-B-B, PAdES-B-T, PAdES-B-LT)
- **Client simplifié** : Authentification JWT et polling intégrés via `factpulse_helpers`

## 🚀 Installation

```bash
pip install factpulse
```

## 📖 Démarrage rapide

### Méthode recommandée : Client simplifié avec helpers

Le module `factpulse_helpers` offre une API simplifiée avec authentification et polling automatiques :

```python
from factpulse_helpers import FactPulseClient

# Créer le client (authentification automatique)
client = FactPulseClient(
    email="votre_email@example.com",
    password="votre_mot_de_passe"
)

# Données de la facture
facture_data = {
    "numero_facture": "FAC-2025-001",
    "date_facture": "2025-01-15",
    "fournisseur": {
        "nom": "Mon Entreprise SAS",
        "siret": "12345678901234",
        "adresse_postale": {
            "ligne_un": "123 Rue Example",
            "code_postal": "75001",
            "nom_ville": "Paris",
            "pays_code_iso": "FR"
        }
    },
    "destinataire": {
        "nom": "Client SARL",
        "siret": "98765432109876",
        "adresse_postale": {
            "ligne_un": "456 Avenue Test",
            "code_postal": "69001",
            "nom_ville": "Lyon",
            "pays_code_iso": "FR"
        }
    },
    "montant_total": {
        "montant_ht_total": "1000.00",
        "montant_tva": "200.00",
        "montant_ttc_total": "1200.00",
        "montant_a_payer": "1200.00"
    },
    "lignes_de_poste": [{
        "numero": 1,
        "denomination": "Prestation de conseil",
        "quantite": "10.00",
        "unite": "PIECE",
        "montant_unitaire_ht": "100.00"
    }]
}

# Lire le PDF source
with open("facture_source.pdf", "rb") as f:
    pdf_source = f.read()

# Générer le PDF Factur-X (polling automatique)
pdf_bytes = client.generer_facturx(
    facture_data=facture_data,
    pdf_source=pdf_source,
    profil="EN16931",
    sync=True  # Attend le résultat automatiquement
)

# Sauvegarder
with open("facture_facturx.pdf", "wb") as f:
    f.write(pdf_bytes)
```

### Méthode alternative : SDK brut

Pour un contrôle total, utilisez le SDK généré directement :

```python
from factpulse import ApiClient, Configuration
from factpulse.api import TraitementFactureApi
import requests
import json

# 1. Obtenir le token JWT
response = requests.post(
    'https://factpulse.fr/api/token/',
    json={
        'username': 'votre_email@example.com',
        'password': 'votre_mot_de_passe'
    }
)
token = response.json()['access']

# 2. Configurer le client
config = Configuration(host='https://factpulse.fr/api/facturation')
config.access_token = token
client = ApiClient(configuration=config)

# 3. Appeler l'API
api = TraitementFactureApi(client)
response = api.generer_facture_api_v1_traitement_generer_facture_post(
    donnees_facture=json.dumps(facture_data),
    profil='EN16931',
    format_sortie='pdf',
    source_pdf=pdf_source
)

# 4. Polling manuel pour récupérer le résultat
task_id = response.id_tache
# ... (implémenter le polling)
```

## 🔧 Avantages de factpulse_helpers

| Fonctionnalité | SDK brut | factpulse_helpers |
|----------------|----------|-------------------|
| Authentification | Manuelle | Automatique |
| Refresh token | Manuel | Automatique |
| Polling tâches async | Manuel | Automatique (backoff) |
| Retry sur 401 | Manuel | Automatique |
| Conversion Decimal | Manuelle | Helper inclus |

## 🔑 Options d'authentification

### Client UID (multi-clients)

Si vous gérez plusieurs clients et souhaitez accéder aux credentials d'un client spécifique :

```python
client = FactPulseClient(
    email="votre_email@example.com",
    password="votre_mot_de_passe",
    client_uid="identifiant_client"  # UID du client cible
)
```

### Configuration avancée

```python
client = FactPulseClient(
    email="votre_email@example.com",
    password="votre_mot_de_passe",
    api_url="https://factpulse.fr",  # URL personnalisée
    polling_interval=2,  # Intervalle de polling initial (secondes)
    polling_timeout=120,  # Timeout de polling (secondes)
    max_retries=2  # Tentatives en cas de 401
)
```

## 💡 Formats de montants acceptés

L'API accepte plusieurs formats pour les montants monétaires :

```python
# String (recommandé pour la précision)
montant = "1234.56"

# Number (float)
montant = 1234.56

# Integer
montant = 1234

# Decimal Python
from decimal import Decimal
montant = Decimal("1234.56")

# Helper de formatage
montant_formate = FactPulseClient.format_montant(1234.5)  # "1234.50"
```

## 📚 Ressources

- **Documentation API** : https://factpulse.fr/api/facturation/documentation
- **Code source** : https://github.com/factpulse/sdk-python
- **Issues** : https://github.com/factpulse/sdk-python/issues
- **Support** : contact@factpulse.fr

## 📄 Licence

MIT License - Copyright (c) 2025 FactPulse
