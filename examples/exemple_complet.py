#!/usr/bin/env python3
"""
Exemple exhaustif d'utilisation du SDK FactPulse Python.

Ce script démontre toutes les fonctionnalités du SDK avec les bonnes pratiques :
- Authentification et gestion des tokens
- Génération de factures Factur-X avec les helpers
- Validation de PDF/XML Factur-X
- Signature électronique de PDF
- Intégration Chorus Pro
- Intégration AFNOR PDP/PA
- Workflow complet de facturation

Auteur: FactPulse
Version: 2.0.32
"""

import logging
import os
import sys
from pathlib import Path
from datetime import date, timedelta

# Import du SDK FactPulse - Client et Helpers
from factpulse_helpers import (
    # Client principal
    FactPulseClient,
    # Credentials pour mode Zero-Trust
    ChorusProCredentials,
    AFNORCredentials,
    # Helpers pour construire les données de facture
    montant,
    montant_total,
    ligne_de_poste,
    ligne_de_tva,
    adresse_postale,
    adresse_electronique,
    fournisseur,
    destinataire,
    # Exceptions
    FactPulseAuthError,
    FactPulsePollingTimeout,
    FactPulseValidationError,
)

# Configuration du logging pour voir les détails
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# =============================================================================
# CONFIGURATION
# =============================================================================

# Variables d'environnement (recommandé pour la production)
EMAIL = os.getenv("FACTPULSE_EMAIL", "votre_email@example.com")
PASSWORD = os.getenv("FACTPULSE_PASSWORD", "votre_mot_de_passe")
CLIENT_UID = os.getenv("FACTPULSE_CLIENT_UID")  # Optionnel, pour multi-clients

# URL de l'API (par défaut: production)
API_URL = os.getenv("FACTPULSE_API_URL", "https://www.factpulse.fr")


# =============================================================================
# 1. INITIALISATION DU CLIENT
# =============================================================================


def exemple_initialisation_simple():
    """Initialisation simple du client avec email/password."""
    print("\n" + "=" * 60)
    print("1. INITIALISATION SIMPLE")
    print("=" * 60)

    client = FactPulseClient(
        email=EMAIL,
        password=PASSWORD,
        api_url=API_URL,
    )

    print("✅ Client initialisé avec succès")
    print(f"   API URL: {client.api_url}")
    return client


def exemple_initialisation_multi_client():
    """Initialisation avec client_uid pour accéder aux credentials d'un client spécifique."""
    print("\n" + "=" * 60)
    print("1b. INITIALISATION MULTI-CLIENT")
    print("=" * 60)

    client = FactPulseClient(
        email=EMAIL,
        password=PASSWORD,
        api_url=API_URL,
        client_uid=CLIENT_UID,  # UUID du client cible
    )

    print(f"✅ Client initialisé avec client_uid: {CLIENT_UID}")
    return client


def exemple_initialisation_zero_trust():
    """Initialisation en mode Zero-Trust (credentials passés à chaque requête)."""
    print("\n" + "=" * 60)
    print("1c. INITIALISATION MODE ZERO-TRUST")
    print("=" * 60)

    # Credentials Chorus Pro (jamais stockés côté serveur)
    chorus_creds = ChorusProCredentials(
        piste_client_id="votre_piste_client_id",
        piste_client_secret="votre_piste_client_secret",
        chorus_pro_login="votre_login_chorus",
        chorus_pro_password="votre_password_chorus",
        sandbox=True,  # True pour les tests, False pour la production
    )

    # Credentials AFNOR PDP (jamais stockés côté serveur)
    afnor_creds = AFNORCredentials(
        flow_service_url="https://api.votre-pdp.fr/flow/v1",
        token_url="https://auth.votre-pdp.fr/oauth/token",
        client_id="votre_client_id_pdp",
        client_secret="votre_client_secret_pdp",
    )

    client = FactPulseClient(
        email=EMAIL,
        password=PASSWORD,
        api_url=API_URL,
        chorus_credentials=chorus_creds,
        afnor_credentials=afnor_creds,
    )

    print("✅ Client initialisé en mode Zero-Trust")
    print("   Les credentials Chorus Pro et AFNOR seront passés à chaque requête")
    return client


# =============================================================================
# 2. HELPERS POUR CONSTRUIRE LES DONNÉES DE FACTURE
# =============================================================================


def exemple_helpers_construction_facture():
    """Utilisation des helpers pour construire une facture proprement.

    Ces helpers génèrent des dictionnaires conformes à l'API FactPulse,
    avec les clés en camelCase et le bon format pour chaque champ.
    """
    print("\n" + "=" * 60)
    print("2. HELPERS DE CONSTRUCTION DE FACTURE")
    print("=" * 60)

    # -------------------------------------------------------------------------
    # Helper montant() - convertit n'importe quel type en string formaté
    # -------------------------------------------------------------------------
    print("\n--- montant(value) ---")
    print("Convertit une valeur en string de montant pour l'API.")
    print(f"  montant(100.50) = '{montant(100.50)}'")  # "100.50"
    print(f"  montant('200.00') = '{montant('200.00')}'")  # "200.00"
    print(f"  montant(1000) = '{montant(1000)}'")  # "1000.00"
    print(f"  montant(None) = '{montant(None)}'")  # "0.00"

    # -------------------------------------------------------------------------
    # Helper montant_total() - construit le bloc montant_total
    # -------------------------------------------------------------------------
    print(
        "\n--- montant_total(ht, tva, ttc, a_payer, remise_ttc=None, motif_remise=None, acompte=None) ---"
    )
    print("Crée un objet MontantTotal simplifié.")
    total = montant_total(
        ht=1000.00,
        tva=200.00,
        ttc=1200.00,
        a_payer=1200.00,
    )
    print(f"  montant_total(1000, 200, 1200, 1200) = {total}")
    # Résultat: {'montantHtTotal': '1000.00', 'montantTva': '200.00',
    #            'montantTtcTotal': '1200.00', 'montantAPayer': '1200.00'}

    # Avec remise et acompte
    total_avec_remise = montant_total(
        ht=1000.00,
        tva=180.00,
        ttc=1080.00,
        a_payer=980.00,
        remise_ttc=100.00,
        motif_remise="Remise fidélité",
        acompte=100.00,
    )
    print(f"  montant_total avec remise = {total_avec_remise}")

    # -------------------------------------------------------------------------
    # Helper ligne_de_poste() - construit une ligne de facture
    # -------------------------------------------------------------------------
    print("\n--- ligne_de_poste() ---")
    print("Crée une ligne de poste pour l'API FactPulse.")
    print("Signature: ligne_de_poste(numero, denomination, quantite, montant_unitaire_ht,")
    print(
        "                           montant_total_ligne_ht, taux_tva=None, taux_tva_manuel='20.00',"
    )
    print("                           categorie_tva='S', unite='FORFAIT', reference=None, ...)")

    # Exemple basique avec taux_tva_manuel (par défaut 20%)
    ligne1 = ligne_de_poste(
        numero=1,
        denomination="Prestation de conseil en informatique",
        quantite=5,
        montant_unitaire_ht=200.00,
        montant_total_ligne_ht=1000.00,  # 5 x 200
        unite="HEURE",
        reference="REF-001",
    )
    print(f"  Ligne 1 (TVA 20% par défaut): {ligne1}")

    # Exemple avec code TVA prédéfini (taux_tva)
    ligne2 = ligne_de_poste(
        numero=2,
        denomination="Documentation technique",
        quantite=1,
        montant_unitaire_ht=500.00,
        montant_total_ligne_ht=500.00,
        taux_tva="TVA10",  # Code TVA au lieu de valeur
        unite="FORFAIT",
    )
    print(f"  Ligne 2 (avec code TVA10): {ligne2}")

    # Exemple avec TVA à taux réduit (5.5%)
    ligne3 = ligne_de_poste(
        numero=3,
        denomination="Produit alimentaire",
        quantite=10,
        montant_unitaire_ht=5.50,
        montant_total_ligne_ht=55.00,
        taux_tva_manuel="5.50",
        categorie_tva="S",
        unite="PIECE",
    )
    print(f"  Ligne 3 (TVA 5.5%): {ligne3}")

    # Exemple avec remise
    ligne4 = ligne_de_poste(
        numero=4,
        denomination="Prestation avec remise",
        quantite=2,
        montant_unitaire_ht=300.00,
        montant_total_ligne_ht=540.00,  # 600 - 60 (10% remise)
        montant_remise_ht=60.00,
        code_raison_reduction="95",  # Code standard
        raison_reduction="Remise commerciale 10%",
    )
    print(f"  Ligne 4 (avec remise): {ligne4}")

    # Exemple avec période de facturation
    ligne5 = ligne_de_poste(
        numero=5,
        denomination="Abonnement mensuel",
        quantite=1,
        montant_unitaire_ht=99.00,
        montant_total_ligne_ht=99.00,
        date_debut_periode="2025-01-01",
        date_fin_periode="2025-01-31",
    )
    print(f"  Ligne 5 (avec période): {ligne5}")

    # -------------------------------------------------------------------------
    # Helper ligne_de_tva() - construit une ligne de TVA
    # -------------------------------------------------------------------------
    print("\n--- ligne_de_tva() ---")
    print("Crée une ligne de TVA pour l'API FactPulse.")
    print(
        "Signature: ligne_de_tva(montant_base_ht, montant_tva, taux=None, taux_manuel='20.00', categorie='S')"
    )

    # Exemple avec taux manuel
    tva1 = ligne_de_tva(
        montant_base_ht=1000.00,
        montant_tva=200.00,
        taux_manuel="20.00",
        categorie="S",  # S = Standard
    )
    print(f"  TVA 20%: {tva1}")

    # Exemple avec code taux
    tva2 = ligne_de_tva(
        montant_base_ht=500.00,
        montant_tva=50.00,
        taux="TVA10",
        categorie="S",
    )
    print(f"  TVA 10% (code): {tva2}")

    # Catégories TVA disponibles:
    # S = Standard, Z = Zéro, E = Exonéré, AE = Autoliquidation, K = Intracommunautaire

    # -------------------------------------------------------------------------
    # Helper adresse_postale() - construit une adresse
    # -------------------------------------------------------------------------
    print("\n--- adresse_postale() ---")
    print("Crée une adresse postale pour l'API FactPulse.")
    print(
        "Signature: adresse_postale(ligne1, code_postal, ville, pays='FR', ligne2=None, ligne3=None)"
    )

    adresse = adresse_postale(
        ligne1="123 Rue de la République",
        code_postal="75001",
        ville="Paris",
    )
    print(f"  Adresse simple: {adresse}")

    adresse_complete = adresse_postale(
        ligne1="456 Avenue des Champs-Élysées",
        code_postal="75008",
        ville="Paris",
        pays="FR",
        ligne2="Bâtiment A, 3ème étage",
        ligne3="Bureau 301",
    )
    print(f"  Adresse complète: {adresse_complete}")

    # -------------------------------------------------------------------------
    # Helper adresse_electronique() - construit une adresse électronique
    # -------------------------------------------------------------------------
    print("\n--- adresse_electronique() ---")
    print("Crée une adresse électronique pour l'API FactPulse.")
    print("Signature: adresse_electronique(identifiant, scheme_id='0009')")
    print("Schemes: 0009=SIREN, 0225=FR-SIRET, 0088=EAN, 0096=DUNS, 0130=Codification propre")

    adresse_elec_siren = adresse_electronique("123456789", "0009")  # SIREN
    print(f"  Adresse SIREN: {adresse_elec_siren}")

    adresse_elec_siret = adresse_electronique("12345678901234", "0225")  # SIRET
    print(f"  Adresse SIRET: {adresse_elec_siret}")

    # -------------------------------------------------------------------------
    # Helper fournisseur() - construit les données fournisseur complètes
    # -------------------------------------------------------------------------
    print("\n--- fournisseur() ---")
    print("Crée un fournisseur (émetteur) avec auto-calcul SIREN et TVA intracommunautaire.")
    print("Signature: fournisseur(nom, siret, adresse_ligne1, code_postal, ville,")
    print("                       id_fournisseur=0, siren=None, numero_tva_intra=None,")
    print("                       iban=None, pays='FR', adresse_ligne2=None, ...)")

    fourn = fournisseur(
        nom="Ma Société SAS",
        siret="12345678900001",
        adresse_ligne1="123 Rue de la République",
        code_postal="75001",
        ville="Paris",
        iban="FR7630006000011234567890189",
    )
    print(f"  Fournisseur (auto-calcul SIREN/TVA): {fourn}")
    # Le helper calcule automatiquement:
    # - siren: 123456789 (extrait du SIRET)
    # - numeroTvaIntra: FR12123456789 (calculé depuis le SIREN)
    # - adresseElectronique et adressePostale

    # Exemple avec tous les paramètres
    fourn_complet = fournisseur(
        nom="Grande Entreprise SA",
        siret="98765432100001",
        adresse_ligne1="1 Place de l'Entreprise",
        code_postal="69001",
        ville="Lyon",
        pays="FR",
        adresse_ligne2="Tour Europa",
        iban="FR7630004000031234567890143",
        numero_tva_intra="FR12987654321",  # Fourni manuellement
        code_service=12345,  # ID service Chorus Pro
        code_coordonnees_bancaires=67890,  # Code coordonnées bancaires Chorus Pro
    )
    print(f"  Fournisseur complet: {fourn_complet}")

    # -------------------------------------------------------------------------
    # Helper destinataire() - construit les données destinataire complètes
    # -------------------------------------------------------------------------
    print("\n--- destinataire() ---")
    print("Crée un destinataire (client) avec auto-calcul SIREN.")
    print("Signature: destinataire(nom, siret, adresse_ligne1, code_postal, ville,")
    print("                        siren=None, pays='FR', adresse_ligne2=None,")
    print("                        code_service_executant=None)")

    dest = destinataire(
        nom="Client SARL",
        siret="98765432109876",
        adresse_ligne1="456 Avenue des Champs",
        code_postal="69001",
        ville="Lyon",
    )
    print(f"  Destinataire simple: {dest}")

    # Avec code service (pour Chorus Pro)
    dest_chorus = destinataire(
        nom="Ministère de l'Économie",
        siret="11004601800013",
        adresse_ligne1="139 Rue de Bercy",
        code_postal="75012",
        ville="Paris",
        code_service_executant="SERVICE_COMPTA",
    )
    print(f"  Destinataire Chorus Pro: {dest_chorus}")

    return {
        "montant_total": total,
        "lignes": [ligne1, ligne2, ligne3, ligne4, ligne5],
        "tva": [tva1, tva2],
        "fournisseur": fourn,
        "destinataire": dest,
    }


def construire_facture_complete():
    """Construit une facture complète avec tous les helpers.

    Cette fonction montre comment assembler une facture prête à être
    envoyée à l'API FactPulse pour génération Factur-X.
    """

    # Dates
    date_facture = date.today().isoformat()
    date_echeance = (date.today() + timedelta(days=30)).isoformat()

    return {
        "numeroFacture": f"FAC-{date.today().year}-001",
        "dateFacture": date_facture,
        "dateEcheancePaiement": date_echeance,
        "modeDepot": "DEPOT_PDF_API",
        # Fournisseur avec helper (génère automatiquement les adresses et TVA)
        "fournisseur": fournisseur(
            nom="Ma Société SAS",
            siret="12345678900001",
            adresse_ligne1="123 Rue de la République",
            code_postal="75001",
            ville="Paris",
            iban="FR7630006000011234567890189",
        ),
        # Destinataire avec helper
        "destinataire": destinataire(
            nom="Client SARL",
            siret="98765432109876",
            adresse_ligne1="456 Avenue des Champs",
            code_postal="69001",
            ville="Lyon",
        ),
        # Références
        "references": {
            "typeFacture": "FACTURE",
            "typeTva": "TVA_SUR_DEBIT",
            "modePaiement": "VIREMENT",
            "deviseFacture": "EUR",
            "numeroBonCommande": "CMD-2025-042",
        },
        # Lignes de poste avec helper
        "lignesDePoste": [
            ligne_de_poste(
                numero=1,
                denomination="Prestation de conseil",
                quantite=5,
                montant_unitaire_ht=200.00,
                montant_total_ligne_ht=1000.00,
                taux_tva_manuel="20.00",
                unite="HEURE",
                reference="REF-CONSEIL-001",
            ),
            ligne_de_poste(
                numero=2,
                denomination="Formation développeurs",
                quantite=3,
                montant_unitaire_ht=500.00,
                montant_total_ligne_ht=1500.00,
                taux_tva_manuel="20.00",
                unite="JOUR",
                reference="REF-FORM-002",
            ),
        ],
        # Lignes de TVA avec helper
        "lignesDeTva": [
            ligne_de_tva(
                montant_base_ht=2500.00,
                montant_tva=500.00,
                taux_manuel="20.00",
                categorie="S",
            ),
        ],
        # Montant total avec helper
        "montantTotal": montant_total(
            ht=2500.00,
            tva=500.00,
            ttc=3000.00,
            a_payer=3000.00,
        ),
        "commentaire": "Facture pour prestations du mois en cours",
    }


# =============================================================================
# 3. GÉNÉRATION DE FACTURES FACTUR-X
# =============================================================================


def exemple_generer_facturx(client: FactPulseClient, pdf_source_path: str):
    """Génère une facture Factur-X à partir d'un PDF source."""
    print("\n" + "=" * 60)
    print("3. GÉNÉRATION FACTUR-X")
    print("=" * 60)

    # Construire les données de facture avec les helpers
    facture_data = construire_facture_complete()

    print(f"📄 PDF source: {pdf_source_path}")
    print(f"📝 Facture: {facture_data['numeroFacture']}")

    try:
        # Générer le PDF Factur-X (mode synchrone avec polling automatique)
        # La méthode accepte:
        # - facture_data: dict, JSON string, ou modèle Pydantic
        # - pdf_source: bytes ou chemin (str/Path)
        pdf_bytes = client.generer_facturx(
            facture_data=facture_data,
            pdf_source=pdf_source_path,  # Chemin vers le PDF source
            profil="EN16931",  # MINIMUM, BASIC, EN16931, EXTENDED
            format_sortie="pdf",  # pdf ou xml
            sync=True,  # Attend le résultat avec polling automatique
            timeout=120000,  # Timeout en ms (2 minutes)
        )

        # Sauvegarder le résultat
        output_path = f"facture_facturx_{facture_data['numeroFacture']}.pdf"
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

        print(f"✅ PDF Factur-X généré: {output_path} ({len(pdf_bytes)} bytes)")
        return output_path

    except FactPulseValidationError as e:
        print(f"❌ Erreur de validation: {e}")
        for error in e.errors:
            print(f"   - [{error.item}] {error.reason}")
        raise
    except FactPulsePollingTimeout as e:
        print(f"❌ Timeout lors de la génération: {e}")
        raise


def exemple_generer_facturx_async(client: FactPulseClient, pdf_source_path: str):
    """Génère une facture Factur-X en mode asynchrone (polling manuel)."""
    print("\n" + "=" * 60)
    print("3b. GÉNÉRATION FACTUR-X (ASYNC)")
    print("=" * 60)

    facture_data = construire_facture_complete()

    # Mode asynchrone: retourne immédiatement avec un task_id
    task_id = client.generer_facturx(
        facture_data=facture_data,
        pdf_source=pdf_source_path,
        profil="EN16931",
        sync=False,  # Ne pas attendre
    )

    print(f"📋 Tâche créée: {task_id}")

    # Polling manuel avec la méthode poll_task
    result = client.poll_task(
        task_id.decode() if isinstance(task_id, bytes) else task_id, timeout=120000
    )

    if result.get("contenu_b64"):
        import base64

        pdf_bytes = base64.b64decode(result["contenu_b64"])
        print(f"✅ Génération terminée: {len(pdf_bytes)} bytes")
        return pdf_bytes
    else:
        print(f"❌ Résultat inattendu: {result}")
        return None


# =============================================================================
# 4. VALIDATION DE PDF/XML FACTUR-X
# =============================================================================


def exemple_valider_pdf_facturx(client: FactPulseClient, pdf_path: str):
    """Valide un PDF Factur-X existant."""
    print("\n" + "=" * 60)
    print("4. VALIDATION PDF FACTUR-X")
    print("=" * 60)

    result = client.valider_pdf_facturx(
        pdf_path=pdf_path,
        profil="EN16931",
    )

    print(f"📄 PDF validé: {pdf_path}")
    print(f"✅ Conforme: {result.get('est_conforme', False)}")
    print(f"📊 Profil détecté: {result.get('profil_detecte', 'N/A')}")

    if result.get("erreurs"):
        print("❌ Erreurs:")
        for err in result["erreurs"]:
            print(f"   - {err}")

    if result.get("avertissements"):
        print("⚠️ Avertissements:")
        for warn in result["avertissements"]:
            print(f"   - {warn}")

    return result


def exemple_valider_signature_pdf(client: FactPulseClient, pdf_path: str):
    """Valide les signatures électroniques d'un PDF."""
    print("\n" + "=" * 60)
    print("4b. VALIDATION SIGNATURE PDF")
    print("=" * 60)

    result = client.valider_signature_pdf(pdf_path=pdf_path)

    print(f"📄 PDF analysé: {pdf_path}")
    print(f"✍️ Signé: {result.get('is_signed', False)}")

    for sig in result.get("signatures", []):
        print("\n   Signature:")
        print(f"   - Signataire: {sig.get('signer_cn', 'N/A')}")
        print(f"   - Date: {sig.get('signing_time', 'N/A')}")
        print(f"   - Valide: {sig.get('valid', False)}")

    return result


# =============================================================================
# 5. SIGNATURE ÉLECTRONIQUE DE PDF
# =============================================================================


def exemple_signer_pdf(client: FactPulseClient, pdf_path: str):
    """Signe un PDF avec le certificat configuré côté serveur.

    Note: Le certificat doit être préalablement configuré dans Django Admin
    et associé au client_uid du JWT.
    """
    print("\n" + "=" * 60)
    print("5. SIGNATURE ÉLECTRONIQUE PDF")
    print("=" * 60)

    result = client.signer_pdf(
        pdf_path=pdf_path,
        raison="Validation de la facture",
        localisation="Paris, France",
        contact="contact@example.com",
        use_pades_lt=True,  # PAdES-B-LT (archivage long terme)
        use_timestamp=True,  # Horodatage RFC 3161
        output_path="facture_signee.pdf",  # Sauvegarde automatique
    )

    print(f"✅ PDF signé: {result}")
    return result


def exemple_generer_certificat_test(client: FactPulseClient):
    """Génère un certificat X.509 auto-signé pour les tests.

    Note: Ce certificat doit ensuite être configuré dans Django Admin.
    """
    print("\n" + "=" * 60)
    print("5b. GÉNÉRATION CERTIFICAT TEST")
    print("=" * 60)

    result = client.generer_certificat_test(
        cn="Test FactPulse",
        organisation="Ma Société SAS",
        email="contact@masociete.fr",
        duree_jours=365,
        taille_cle=2048,
    )

    print("✅ Certificat généré")
    print(f"   CN: {result.get('cn')}")
    print(f"   Organisation: {result.get('organisation')}")
    print(f"   Validité: {result.get('duree_jours')} jours")

    # Le résultat contient:
    # - certificat_pem: Certificat au format PEM
    # - cle_privee_pem: Clé privée au format PEM
    # - pkcs12_base64: PKCS#12 encodé en base64 (pour Django Admin)

    return result


# =============================================================================
# 6. INTÉGRATION CHORUS PRO
# =============================================================================


def exemple_rechercher_structure_chorus(client: FactPulseClient, siret: str):
    """Recherche une structure Chorus Pro par SIRET."""
    print("\n" + "=" * 60)
    print("6. RECHERCHE STRUCTURE CHORUS PRO")
    print("=" * 60)

    result = client.rechercher_structure_chorus(
        identifiant_structure=siret,
        type_identifiant="SIRET",
    )

    structures = result.get("liste_structures", [])
    print(f"🔍 Recherche SIRET: {siret}")
    print(f"📊 Structures trouvées: {len(structures)}")

    for struct in structures:
        print("\n   Structure:")
        print(f"   - ID CPP: {struct.get('id_structure_cpp')}")
        print(f"   - Désignation: {struct.get('designation_structure')}")
        print(f"   - SIRET: {struct.get('identifiant_structure')}")

    return result


def exemple_obtenir_id_chorus_depuis_siret(client: FactPulseClient, siret: str):
    """Obtient l'ID Chorus Pro à partir d'un SIRET (helper simplifié)."""
    print("\n" + "=" * 60)
    print("6b. OBTENIR ID CHORUS PRO DEPUIS SIRET")
    print("=" * 60)

    result = client.obtenir_id_chorus_depuis_siret(siret)

    print(f"🔍 SIRET: {siret}")
    print(f"📋 ID Chorus Pro: {result.get('id_structure_cpp')}")
    print(f"📋 Désignation: {result.get('designation_structure')}")

    return result


def exemple_consulter_structure_chorus(client: FactPulseClient, id_structure_cpp: int):
    """Consulte les détails d'une structure Chorus Pro."""
    print("\n" + "=" * 60)
    print("6c. CONSULTER STRUCTURE CHORUS PRO")
    print("=" * 60)

    result = client.consulter_structure_chorus(id_structure_cpp)

    print(f"📋 Structure #{id_structure_cpp}:")
    print(f"   - Désignation: {result.get('designation_structure')}")
    print(f"   - SIRET: {result.get('identifiant_structure')}")

    # Vérifier les paramètres obligatoires
    params = result.get("parametres", {})
    if params.get("code_service_doit_etre_renseigne"):
        print("   ⚠️ Code service OBLIGATOIRE")
    if params.get("numero_ej_doit_etre_renseigne"):
        print("   ⚠️ Numéro engagement OBLIGATOIRE")

    return result


def exemple_lister_services_structure_chorus(client: FactPulseClient, id_structure_cpp: int):
    """Liste les services d'une structure Chorus Pro."""
    print("\n" + "=" * 60)
    print("6d. LISTER SERVICES STRUCTURE CHORUS PRO")
    print("=" * 60)

    result = client.lister_services_structure_chorus(id_structure_cpp)

    services = result.get("liste_services", [])
    print(f"📋 Structure #{id_structure_cpp}")
    print(f"📊 Services trouvés: {len(services)}")

    for svc in services:
        if svc.get("est_actif"):
            print("\n   Service actif:")
            print(f"   - Code: {svc.get('code_service')}")
            print(f"   - Libellé: {svc.get('libelle_service')}")

    return result


def exemple_soumettre_facture_chorus(client: FactPulseClient, id_structure_cpp: int):
    """Soumet une facture à Chorus Pro."""
    print("\n" + "=" * 60)
    print("6e. SOUMETTRE FACTURE CHORUS PRO")
    print("=" * 60)

    result = client.soumettre_facture_chorus(
        numero_facture="FAC-2025-001",
        date_facture="2025-01-15",
        date_echeance_paiement="2025-02-14",
        id_structure_cpp=id_structure_cpp,
        montant_ht_total="2500.00",
        montant_tva="500.00",
        montant_ttc_total="3000.00",
        code_service="SERVICE01",  # Si requis par la structure
        numero_bon_commande="CMD-2025-042",
        commentaire="Facture de prestations",
    )

    print("✅ Facture soumise à Chorus Pro")
    print(f"   ID Facture CPP: {result.get('identifiant_facture_cpp')}")
    print(f"   Numéro flux dépôt: {result.get('numero_flux_depot')}")

    return result


def exemple_consulter_facture_chorus(client: FactPulseClient, identifiant_facture_cpp: int):
    """Consulte une facture Chorus Pro."""
    print("\n" + "=" * 60)
    print("6f. CONSULTER FACTURE CHORUS PRO")
    print("=" * 60)

    result = client.consulter_facture_chorus(identifiant_facture_cpp)

    print(f"📋 Facture #{identifiant_facture_cpp}:")
    print(f"   - Numéro: {result.get('numero_facture')}")
    statut = result.get("statut_courant", {})
    print(f"   - Statut: {statut.get('code', 'N/A')}")
    print(f"   - Montant TTC: {result.get('montant_ttc_total')}")

    return result


# =============================================================================
# 7. INTÉGRATION AFNOR PDP/PA
# =============================================================================


def exemple_healthcheck_afnor(client: FactPulseClient):
    """Vérifie la disponibilité du Flow Service AFNOR."""
    print("\n" + "=" * 60)
    print("7. HEALTHCHECK AFNOR")
    print("=" * 60)

    result = client.healthcheck_afnor()

    print(f"🏥 Status AFNOR: {result.get('status', 'unknown')}")
    print(f"   Service: {result.get('service', 'N/A')}")

    return result


def exemple_soumettre_facture_afnor(client: FactPulseClient, pdf_path: str):
    """Soumet une facture à une PDP via AFNOR."""
    print("\n" + "=" * 60)
    print("7b. SOUMETTRE FACTURE AFNOR")
    print("=" * 60)

    # Avec un chemin de fichier
    result = client.soumettre_facture_afnor(
        flow_name="Facture FAC-2025-001",
        pdf_path=pdf_path,
        flow_syntax="CII",  # CII ou UBL
        flow_profile="EN16931",
        tracking_id="FAC-2025-001",  # Votre référence interne
        # sha256 est calculé automatiquement si non fourni
    )

    print("✅ Facture soumise à la PDP AFNOR")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def exemple_soumettre_facture_afnor_bytes(client: FactPulseClient, pdf_bytes: bytes):
    """Soumet une facture à une PDP via AFNOR avec des bytes."""
    print("\n" + "=" * 60)
    print("7b-bis. SOUMETTRE FACTURE AFNOR (BYTES)")
    print("=" * 60)

    # Avec des bytes (ex: après génération Factur-X)
    result = client.soumettre_facture_afnor(
        flow_name="Facture FAC-2025-001",
        pdf_bytes=pdf_bytes,  # Passer directement les bytes
        pdf_filename="FAC-2025-001.pdf",  # Nom du fichier pour l'upload
        flow_syntax="CII",
        flow_profile="EN16931",
        tracking_id="FAC-2025-001",
    )

    print("✅ Facture soumise à la PDP AFNOR")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def exemple_generer_et_soumettre_afnor(client: FactPulseClient, pdf_source_path: str):
    """Génère une facture Factur-X puis la soumet directement à AFNOR."""
    print("\n" + "=" * 60)
    print("7c. GÉNÉRER ET SOUMETTRE AFNOR (WORKFLOW OPTIMISÉ)")
    print("=" * 60)

    # Construire les données de facture
    facture_data = construire_facture_complete()

    # 1. Générer le PDF Factur-X
    print("📄 Génération du PDF Factur-X...")
    pdf_facturx = client.generer_facturx(
        facture_data=facture_data,
        pdf_source=pdf_source_path,
        profil="EN16931",
        sync=True,
    )
    print(f"   ✅ PDF généré: {len(pdf_facturx)} bytes")

    # 2. Soumettre directement les bytes à AFNOR (sans créer de fichier)
    print("📤 Soumission directe à AFNOR...")
    result = client.soumettre_facture_afnor(
        flow_name=f"Facture {facture_data['numeroFacture']}",
        pdf_bytes=pdf_facturx,  # Passer directement les bytes
        pdf_filename=f"{facture_data['numeroFacture']}.pdf",
        tracking_id=facture_data["numeroFacture"],
    )

    print("✅ Facture générée et soumise en un seul flux")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def exemple_rechercher_flux_afnor(client: FactPulseClient, tracking_id: str = None):
    """Recherche des flux de facturation AFNOR."""
    print("\n" + "=" * 60)
    print("7d. RECHERCHER FLUX AFNOR")
    print("=" * 60)

    result = client.rechercher_flux_afnor(
        tracking_id=tracking_id,  # Filtrer par tracking_id
        status=None,  # Filtrer par status (submitted, processing, delivered, etc.)
        offset=0,
        limit=25,
    )

    flows = result.get("flows", [])
    print(f"📊 Flux trouvés: {result.get('total', len(flows))}")

    for flow in flows:
        print("\n   Flux:")
        print(f"   - Flow ID: {flow.get('flowId')}")
        print(f"   - Tracking ID: {flow.get('trackingId')}")
        print(f"   - Status: {flow.get('status')}")
        print(f"   - Date: {flow.get('createdAt')}")

    return result


def exemple_telecharger_flux_afnor(client: FactPulseClient, flow_id: str):
    """Télécharge le fichier PDF d'un flux AFNOR."""
    print("\n" + "=" * 60)
    print("7e. TÉLÉCHARGER FLUX AFNOR")
    print("=" * 60)

    pdf_bytes = client.telecharger_flux_afnor(flow_id)

    output_path = f"flux_{flow_id}.pdf"
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)

    print(f"✅ Flux téléchargé: {output_path} ({len(pdf_bytes)} bytes)")

    return output_path


def exemple_rechercher_siret_afnor(client: FactPulseClient, siret: str):
    """Recherche une entreprise par SIRET dans le Directory Service AFNOR."""
    print("\n" + "=" * 60)
    print("7f. RECHERCHER SIRET AFNOR")
    print("=" * 60)

    result = client.rechercher_siret_afnor(siret)

    print(f"🔍 SIRET: {siret}")
    print(f"   Résultat: {result}")

    return result


def exemple_rechercher_siren_afnor(client: FactPulseClient, siren: str):
    """Recherche une entreprise par SIREN dans le Directory Service AFNOR."""
    print("\n" + "=" * 60)
    print("7g. RECHERCHER SIREN AFNOR")
    print("=" * 60)

    result = client.rechercher_siren_afnor(siren)

    print(f"🔍 SIREN: {siren}")
    print(f"   Résultat: {result}")

    return result


def exemple_lister_codes_routage_afnor(client: FactPulseClient, siren: str):
    """Liste les codes de routage d'une entreprise."""
    print("\n" + "=" * 60)
    print("7h. LISTER CODES ROUTAGE AFNOR")
    print("=" * 60)

    codes = client.lister_codes_routage_afnor(siren)

    print(f"🔍 SIREN: {siren}")
    print(f"📊 Codes de routage: {len(codes)}")

    for code in codes:
        print(f"   - {code.get('code_routage')}: {code.get('description', 'N/A')}")

    return codes


# =============================================================================
# 8. WORKFLOW COMPLET
# =============================================================================


def exemple_workflow_complet(client: FactPulseClient, pdf_source_path: str):
    """Workflow complet: génération + validation + signature + soumission."""
    print("\n" + "=" * 60)
    print("8. WORKFLOW COMPLET")
    print("=" * 60)

    # Construire les données de facture
    facture_data = construire_facture_complete()

    # Utiliser generer_facturx_complet() qui fait tout en une fois
    result = client.generer_facturx_complet(
        facture=facture_data,
        pdf_source_path=pdf_source_path,
        profil="EN16931",
        valider=True,  # Valider le PDF après génération
        signer=True,  # Signer avec le certificat serveur
        soumettre_afnor=True,  # Soumettre à la PDP AFNOR
        afnor_flow_name=f"Facture {facture_data['numeroFacture']}",
        afnor_tracking_id=facture_data["numeroFacture"],
        output_path="facture_complete.pdf",
        timeout=180000,  # 3 minutes
    )

    print("✅ Workflow complet terminé:")
    print(f"   PDF généré: {result.get('pdf_bytes') is not None}")
    print(f"   Validation: {result.get('validation', {}).get('est_conforme', 'N/A')}")
    print(f"   Signé: {result.get('signature', {}).get('signe', False)}")
    if result.get("afnor"):
        print(f"   Flow ID AFNOR: {result['afnor'].get('flowId')}")
    if result.get("pdf_path"):
        print(f"   Fichier sauvegardé: {result['pdf_path']}")

    return result


# =============================================================================
# 9. GESTION DES ERREURS
# =============================================================================


def exemple_gestion_erreurs():
    """Démontre la gestion des erreurs du SDK."""
    print("\n" + "=" * 60)
    print("9. GESTION DES ERREURS")
    print("=" * 60)

    # Hiérarchie des exceptions:
    # FactPulseError (base)
    #   ├── FactPulseAuthError (401) - Authentification échouée
    #   ├── FactPulseValidationError (400, 422) - Erreur de validation avec détails
    #   ├── FactPulsePollingTimeout - Timeout lors du polling
    #   ├── FactPulseNotFoundError (404) - Ressource non trouvée
    #   └── FactPulseServiceUnavailableError (503) - Service indisponible

    print("\n--- FactPulseAuthError (401) ---")
    print("   Se produit quand: email/password invalides, token expiré")
    try:
        bad_client = FactPulseClient(
            email="mauvais@email.com",
            password="mauvais_mot_de_passe",
        )
        bad_client.ensure_authenticated()
    except FactPulseAuthError as e:
        print(f"   ✅ Erreur capturée: {e.message}")

    print("\n--- FactPulseValidationError (400, 422) ---")
    print("   Se produit quand: données de facture invalides, PDF non conforme")
    print("   Contient une liste d'erreurs détaillées:")
    print("   - e.errors: List[ValidationErrorDetail]")
    print("   - e.error_code: Code d'erreur (ex: SCHEMATRON_VALIDATION_FAILED)")
    print("   Chaque erreur a: level, item, reason, source, code")

    print("\n--- FactPulsePollingTimeout ---")
    print("   Se produit quand: une tâche async dépasse le timeout")
    print("   Propriétés: task_id, timeout")
    print("   Paramètre par défaut: 120000 ms (2 minutes)")

    print("\n--- FactPulseNotFoundError (404) ---")
    print("   Se produit quand: flux AFNOR, structure Chorus Pro non trouvés")
    print("   Propriétés: resource, identifier")

    print("\n--- FactPulseServiceUnavailableError (503) ---")
    print("   Se produit quand: PDP AFNOR, Chorus Pro, API indisponibles")
    print("   Propriétés: service_name, original_error")


# =============================================================================
# MAIN
# =============================================================================


def main():
    """Point d'entrée principal."""
    print("=" * 60)
    print("EXEMPLE EXHAUSTIF SDK FACTPULSE PYTHON")
    print("=" * 60)
    print("Version SDK: 2.0.30")
    print(f"API URL: {API_URL}")

    # Vérifier les credentials
    if EMAIL == "votre_email@example.com":
        print("\n⚠️  ATTENTION: Configurez vos credentials dans les variables d'environnement:")
        print("   export FACTPULSE_EMAIL='votre_email@example.com'")
        print("   export FACTPULSE_PASSWORD='votre_mot_de_passe'")
        print("\nCe script va démontrer uniquement les helpers (sans appels API).")

        # Démontrer les helpers
        exemple_helpers_construction_facture()

        # Démontrer la gestion des erreurs
        exemple_gestion_erreurs()

        print("\n✅ Helpers démontrés avec succès!")
        return

    # Créer le client
    client = exemple_initialisation_simple()

    # Vérifier si un PDF source est fourni
    pdf_source = sys.argv[1] if len(sys.argv) > 1 else None

    if pdf_source and Path(pdf_source).exists():
        # Workflow complet avec un vrai PDF
        exemple_generer_facturx(client, pdf_source)
    else:
        print("\n💡 Pour tester la génération, fournissez un PDF source:")
        print(f"   python {sys.argv[0]} facture_source.pdf")

    # Démontrer les helpers (toujours)
    exemple_helpers_construction_facture()

    print("\n" + "=" * 60)
    print("✅ EXEMPLES TERMINÉS")
    print("=" * 60)


if __name__ == "__main__":
    main()
