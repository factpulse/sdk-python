#!/usr/bin/env python3
"""
Exemple exhaustif d'utilisation du SDK FactPulse Python.

Ce script démontre toutes les fonctionnalités du SDK avec les bonnes pratiques :
- Authentification et gestion des tokens
- Génération de factures Factur-X
- Validation de PDF/XML Factur-X
- Signature électronique de PDF
- Intégration Chorus Pro
- Intégration AFNOR PDP/PA
- Workflow complet de facturation

Auteur: FactPulse
Version: 2.0.29
"""

import logging
import os
import sys
from pathlib import Path
from datetime import date, timedelta

# Import du SDK FactPulse
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
    """Utilisation des helpers pour construire une facture proprement."""
    print("\n" + "=" * 60)
    print("2. HELPERS DE CONSTRUCTION DE FACTURE")
    print("=" * 60)

    # Helper montant() - convertit n'importe quel type en string formaté
    print("\n--- montant() ---")
    print(f"montant(100.50) = '{montant(100.50)}'")
    print(f"montant('200.00') = '{montant('200.00')}'")
    print(f"montant(1000) = '{montant(1000)}'")

    # Helper montant_total() - construit le bloc montant_total
    print("\n--- montant_total() ---")
    total = montant_total(
        ht=1000.00,
        tva=200.00,
        ttc=1200.00,
        a_payer=1200.00,
        acompte=0,
        remise_ttc=0,
    )
    print(f"montant_total() = {total}")

    # Helper ligne_de_poste() - construit une ligne de facture
    print("\n--- ligne_de_poste() ---")
    ligne = ligne_de_poste(
        numero=1,
        denomination="Prestation de conseil en informatique",
        quantite=5,
        unite="HEURE",
        prix_unitaire_ht=200.00,
        taux_tva=20.0,
        reference="REF-001",
        description="Analyse et audit du système d'information",
    )
    print(f"ligne_de_poste() = {ligne}")

    # Helper ligne_de_tva() - construit une ligne de TVA
    print("\n--- ligne_de_tva() ---")
    tva = ligne_de_tva(
        base_ht=1000.00,
        montant_tva=200.00,
        taux=20.0,
        categorie="S",  # S = Standard
    )
    print(f"ligne_de_tva() = {tva}")

    # Helper adresse_postale() - construit une adresse
    print("\n--- adresse_postale() ---")
    adresse = adresse_postale(
        ligne_un="123 Rue de la République",
        ligne_deux="Bâtiment A",
        code_postal="75001",
        ville="Paris",
        pays="FR",
    )
    print(f"adresse_postale() = {adresse}")

    # Helper adresse_electronique() - construit une adresse électronique
    print("\n--- adresse_electronique() ---")
    adresse_elec = adresse_electronique(
        identifiant="12345678901234",
        scheme_id="0009",  # SIRET
    )
    print(f"adresse_electronique() = {adresse_elec}")

    # Helper fournisseur() - construit les données fournisseur complètes
    print("\n--- fournisseur() ---")
    fourn = fournisseur(
        nom="Ma Société SAS",
        siret="12345678901234",
        numero_tva_intra="FR12345678901",
        iban="FR7630006000011234567890189",
        adresse=adresse_postale(
            ligne_un="123 Rue de la République",
            code_postal="75001",
            ville="Paris",
            pays="FR",
        ),
        adresse_elec=adresse_electronique(
            identifiant="12345678901234",
            scheme_id="0009",
        ),
    )
    print(f"fournisseur() = {fourn}")

    # Helper destinataire() - construit les données destinataire complètes
    print("\n--- destinataire() ---")
    dest = destinataire(
        nom="Client SARL",
        siret="98765432109876",
        adresse=adresse_postale(
            ligne_un="456 Avenue des Champs",
            code_postal="69001",
            ville="Lyon",
            pays="FR",
        ),
        adresse_elec=adresse_electronique(
            identifiant="98765432109876",
            scheme_id="0009",
        ),
        code_service="SERVICE01",
    )
    print(f"destinataire() = {dest}")

    return {
        "montant_total": total,
        "ligne": ligne,
        "tva": tva,
        "fournisseur": fourn,
        "destinataire": dest,
    }


def construire_facture_complete():
    """Construit une facture complète avec tous les helpers."""

    # Dates
    date_facture = date.today().isoformat()
    date_echeance = (date.today() + timedelta(days=30)).isoformat()

    return {
        "numero_facture": f"FAC-{date.today().year}-001",
        "date_facture": date_facture,
        "date_echeance_paiement": date_echeance,
        "mode_depot": "DEPOT_PDF_API",
        # Fournisseur avec helper
        "fournisseur": fournisseur(
            nom="Ma Société SAS",
            siret="12345678901234",
            numero_tva_intra="FR12345678901",
            iban="FR7630006000011234567890189",
            adresse=adresse_postale(
                ligne_un="123 Rue de la République",
                code_postal="75001",
                ville="Paris",
                pays="FR",
            ),
            adresse_elec=adresse_electronique(
                identifiant="12345678901234",
                scheme_id="0009",
            ),
        ),
        # Destinataire avec helper
        "destinataire": destinataire(
            nom="Client SARL",
            siret="98765432109876",
            adresse=adresse_postale(
                ligne_un="456 Avenue des Champs",
                code_postal="69001",
                ville="Lyon",
                pays="FR",
            ),
            adresse_elec=adresse_electronique(
                identifiant="98765432109876",
                scheme_id="0009",
            ),
        ),
        # Références
        "references": {
            "type_facture": "FACTURE",
            "type_tva": "TVA_SUR_DEBIT",
            "mode_paiement": "VIREMENT",
            "devise_facture": "EUR",
            "numero_bon_commande": "CMD-2025-042",
        },
        # Lignes de poste avec helper
        "lignes_de_poste": [
            ligne_de_poste(
                numero=1,
                denomination="Prestation de conseil",
                quantite=5,
                unite="HEURE",
                prix_unitaire_ht=200.00,
                taux_tva=20.0,
                reference="REF-CONSEIL-001",
            ),
            ligne_de_poste(
                numero=2,
                denomination="Formation développeurs",
                quantite=3,
                unite="JOUR",
                prix_unitaire_ht=500.00,
                taux_tva=20.0,
                reference="REF-FORM-002",
            ),
        ],
        # Lignes de TVA avec helper
        "lignes_de_tva": [
            ligne_de_tva(
                base_ht=2500.00,
                montant_tva=500.00,
                taux=20.0,
                categorie="S",
            ),
        ],
        # Montant total avec helper
        "montant_total": montant_total(
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

    # Lire le PDF source
    with open(pdf_source_path, "rb") as f:
        pdf_source = f.read()

    print(f"📄 PDF source: {pdf_source_path} ({len(pdf_source)} bytes)")
    print(f"📝 Facture: {facture_data['numero_facture']}")

    try:
        # Générer le PDF Factur-X (mode synchrone avec polling automatique)
        # Signature: generer_facturx(facture_data, pdf_source, profil, format_sortie, sync, timeout)
        pdf_bytes = client.generer_facturx(
            facture_data=facture_data,
            pdf_source=pdf_source,  # Peut être bytes ou chemin (str/Path)
            profil="EN16931",  # MINIMUM, BASIC, EN16931, EXTENDED
            format_sortie="pdf",  # pdf ou xml
            sync=True,  # Attend le résultat avec polling automatique
            timeout=120000,  # Timeout en ms (2 minutes)
        )

        # Sauvegarder le résultat
        output_path = f"facture_facturx_{facture_data['numero_facture']}.pdf"
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

        print(f"✅ PDF Factur-X généré: {output_path} ({len(pdf_bytes)} bytes)")
        return output_path

    except FactPulseValidationError as e:
        print(f"❌ Erreur de validation: {e}")
        for error in e.errors:
            print(f"   - {error.field}: {error.message}")
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

    with open(pdf_source_path, "rb") as f:
        pdf_source = f.read()

    # Mode asynchrone: retourne immédiatement avec un task_id
    result = client.generer_facturx(
        facture_data=facture_data,
        pdf_source=pdf_source,
        profil="EN16931",
        sync=False,  # Ne pas attendre
    )

    task_id = result.get("id_tache") or result.get("task_id")
    print(f"📋 Tâche créée: {task_id}")

    # Polling manuel avec la méthode poll_task
    result = client.poll_task(task_id, timeout=120000)

    if result.get("statut") == "SUCCESS":
        # Récupérer le fichier depuis le résultat
        pdf_b64 = result.get("resultat", {}).get("fichier_base64")
        if pdf_b64:
            import base64

            pdf_bytes = base64.b64decode(pdf_b64)
            print(f"✅ Génération terminée: {len(pdf_bytes)} bytes")
            return pdf_bytes
    else:
        print(f"❌ Échec: {result}")
        return None


# =============================================================================
# 4. VALIDATION DE PDF/XML FACTUR-X
# =============================================================================


def exemple_valider_pdf_facturx(client: FactPulseClient, pdf_path: str):
    """Valide un PDF Factur-X existant."""
    print("\n" + "=" * 60)
    print("4. VALIDATION PDF FACTUR-X")
    print("=" * 60)

    # Signature: valider_pdf_facturx(pdf_path=None, pdf_bytes=None, profil="EN16931")
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

    # Signature: valider_signature_pdf(pdf_path=None, pdf_bytes=None)
    result = client.valider_signature_pdf(pdf_path=pdf_path)

    print(f"📄 PDF analysé: {pdf_path}")
    print(f"✍️ Signatures trouvées: {result.get('nombre_signatures', 0)}")
    print(f"✅ Toutes valides: {result.get('toutes_valides', False)}")

    for sig in result.get("signatures", []):
        print(f"\n   Signature #{sig.get('index', '?')}:")
        print(f"   - Signataire: {sig.get('signataire', 'N/A')}")
        print(f"   - Date: {sig.get('date_signature', 'N/A')}")
        print(f"   - Valide: {sig.get('valide', False)}")
        print(f"   - Certificat: {sig.get('certificat', {}).get('subject', 'N/A')}")

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

    # Signature: signer_pdf(pdf_path, pdf_bytes, raison, localisation, contact,
    #                       use_pades_lt, use_timestamp, output_path)
    result = client.signer_pdf(
        pdf_path=pdf_path,
        raison="Validation de la facture",
        localisation="Paris, France",
        contact="contact@example.com",
        use_pades_lt=True,  # PAdES-B-LT (archivage long terme)
        use_timestamp=True,  # Horodatage RFC 3161
        output_path="facture_signee.pdf",  # Sauvegarde automatique
    )

    print("✅ PDF signé: facture_signee.pdf")
    return result


def exemple_generer_certificat_test(client: FactPulseClient):
    """Génère un certificat X.509 auto-signé pour les tests.

    Note: Ce certificat doit ensuite être configuré dans Django Admin.
    """
    print("\n" + "=" * 60)
    print("5b. GÉNÉRATION CERTIFICAT TEST")
    print("=" * 60)

    # Signature: generer_certificat_test(cn, organisation, email, duree_jours, taille_cle)
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

    # Signature: rechercher_structure_chorus(identifiant, type_identifiant="SIRET")
    result = client.rechercher_structure_chorus(
        identifiant=siret,
        type_identifiant="SIRET",
    )

    structures = result.get("structures", [])
    print(f"🔍 Recherche SIRET: {siret}")
    print(f"📊 Structures trouvées: {len(structures)}")

    for struct in structures:
        print("\n   Structure:")
        print(f"   - ID CPP: {struct.get('id_structure_cpp')}")
        print(f"   - Raison sociale: {struct.get('raison_sociale')}")
        print(f"   - SIRET: {struct.get('siret')}")
        print(f"   - Statut: {struct.get('statut')}")

    return result


def exemple_obtenir_id_chorus_depuis_siret(client: FactPulseClient, siret: str):
    """Obtient l'ID Chorus Pro à partir d'un SIRET (helper simplifié)."""
    print("\n" + "=" * 60)
    print("6b. OBTENIR ID CHORUS PRO DEPUIS SIRET")
    print("=" * 60)

    # Signature: obtenir_id_chorus_depuis_siret(siret)
    id_cpp = client.obtenir_id_chorus_depuis_siret(siret)

    print(f"🔍 SIRET: {siret}")
    print(f"📋 ID Chorus Pro: {id_cpp}")

    return id_cpp


def exemple_consulter_structure_chorus(client: FactPulseClient, id_structure_cpp: int):
    """Consulte les détails d'une structure Chorus Pro."""
    print("\n" + "=" * 60)
    print("6c. CONSULTER STRUCTURE CHORUS PRO")
    print("=" * 60)

    # Signature: consulter_structure_chorus(id_structure_cpp)
    result = client.consulter_structure_chorus(id_structure_cpp)

    print(f"📋 Structure #{id_structure_cpp}:")
    print(f"   - Raison sociale: {result.get('raison_sociale')}")
    print(f"   - SIRET: {result.get('siret')}")
    print(f"   - Adresse: {result.get('adresse')}")

    return result


def exemple_lister_services_structure_chorus(client: FactPulseClient, id_structure_cpp: int):
    """Liste les services d'une structure Chorus Pro."""
    print("\n" + "=" * 60)
    print("6d. LISTER SERVICES STRUCTURE CHORUS PRO")
    print("=" * 60)

    # Signature: lister_services_structure_chorus(id_structure_cpp)
    result = client.lister_services_structure_chorus(id_structure_cpp)

    services = result.get("services", [])
    print(f"📋 Structure #{id_structure_cpp}")
    print(f"📊 Services trouvés: {len(services)}")

    for svc in services:
        print("\n   Service:")
        print(f"   - Code: {svc.get('code_service')}")
        print(f"   - Nom: {svc.get('nom_service')}")
        print(f"   - Statut: {svc.get('statut')}")

    return result


def exemple_soumettre_facture_chorus(client: FactPulseClient, id_structure_cpp: int):
    """Soumet une facture à Chorus Pro.

    Note: Cette méthode nécessite d'avoir préalablement:
    1. Recherché la structure destinataire (rechercher_structure_chorus)
    2. Vérifié les paramètres requis (consulter_structure_chorus)
    3. Éventuellement uploadé le PDF via l'API transverses
    """
    print("\n" + "=" * 60)
    print("6e. SOUMETTRE FACTURE CHORUS PRO")
    print("=" * 60)

    # Signature: soumettre_facture_chorus(
    #     numero_facture, date_facture, date_echeance_paiement, id_structure_cpp,
    #     montant_ht_total, montant_tva, montant_ttc_total,
    #     piece_jointe_principale_id=None, piece_jointe_principale_designation="Facture",
    #     code_service=None, numero_engagement=None, numero_bon_commande=None,
    #     numero_marche=None, commentaire=None
    # )
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
    print(f"   Statut: {result.get('statut')}")

    return result


def exemple_consulter_facture_chorus(client: FactPulseClient, identifiant_facture_cpp: int):
    """Consulte une facture Chorus Pro."""
    print("\n" + "=" * 60)
    print("6f. CONSULTER FACTURE CHORUS PRO")
    print("=" * 60)

    # Signature: consulter_facture_chorus(identifiant_facture_cpp)
    result = client.consulter_facture_chorus(identifiant_facture_cpp)

    print(f"📋 Facture #{identifiant_facture_cpp}:")
    print(f"   - Numéro: {result.get('numero_facture')}")
    print(f"   - Statut: {result.get('statut')}")
    print(f"   - Montant TTC: {result.get('montant_ttc')}")

    return result


# =============================================================================
# 7. INTÉGRATION AFNOR PDP/PA
# =============================================================================


def exemple_healthcheck_afnor(client: FactPulseClient):
    """Vérifie la disponibilité du Flow Service AFNOR."""
    print("\n" + "=" * 60)
    print("7. HEALTHCHECK AFNOR")
    print("=" * 60)

    # Signature: healthcheck_afnor()
    result = client.healthcheck_afnor()

    print(f"🏥 Status AFNOR: {result.get('status', 'unknown')}")
    print(f"   Service: {result.get('service', 'N/A')}")

    return result


def exemple_soumettre_facture_afnor(
    client: FactPulseClient, pdf_path: str = None, pdf_bytes: bytes = None
):
    """Soumet une facture à une PDP via AFNOR."""
    print("\n" + "=" * 60)
    print("7b. SOUMETTRE FACTURE AFNOR")
    print("=" * 60)

    # Signature: soumettre_facture_afnor(flow_name, pdf_path=None, pdf_bytes=None,
    #                                    pdf_filename="facture.pdf", flow_syntax="CII",
    #                                    flow_profile="EN16931", tracking_id=None, sha256=None)

    # Exemple 1: Avec un chemin de fichier
    if pdf_path:
        result = client.soumettre_facture_afnor(
            flow_name="Facture FAC-2025-001",
            pdf_path=pdf_path,
            flow_syntax="CII",  # CII ou UBL
            flow_profile="EN16931",
            tracking_id="FAC-2025-001",  # Votre référence interne
            # sha256 est calculé automatiquement si non fourni
        )
    # Exemple 2: Avec des bytes (ex: après génération Factur-X)
    elif pdf_bytes:
        result = client.soumettre_facture_afnor(
            flow_name="Facture FAC-2025-001",
            pdf_bytes=pdf_bytes,
            pdf_filename="FAC-2025-001.pdf",  # Nom du fichier pour l'upload
            flow_syntax="CII",
            flow_profile="EN16931",
            tracking_id="FAC-2025-001",
        )
    else:
        raise ValueError("pdf_path ou pdf_bytes requis")

    print("✅ Facture soumise à la PDP AFNOR")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def exemple_generer_et_soumettre_afnor(client: FactPulseClient, pdf_source_path: str):
    """Génère une facture Factur-X puis la soumet directement à AFNOR (sans fichier intermédiaire)."""
    print("\n" + "=" * 60)
    print("7b-bis. GÉNÉRER ET SOUMETTRE AFNOR (WORKFLOW OPTIMISÉ)")
    print("=" * 60)

    # Construire les données de facture
    facture_data = construire_facture_complete()

    # Lire le PDF source
    with open(pdf_source_path, "rb") as f:
        pdf_source = f.read()

    # 1. Générer le PDF Factur-X
    print("📄 Génération du PDF Factur-X...")
    pdf_facturx = client.generer_facturx(
        facture_data=facture_data,
        pdf_source=pdf_source,
        profil="EN16931",
        sync=True,
    )
    print(f"   ✅ PDF généré: {len(pdf_facturx)} bytes")

    # 2. Soumettre directement les bytes à AFNOR (sans créer de fichier)
    print("📤 Soumission directe à AFNOR...")
    result = client.soumettre_facture_afnor(
        flow_name=f"Facture {facture_data['numero_facture']}",
        pdf_bytes=pdf_facturx,  # Passer directement les bytes !
        pdf_filename=f"{facture_data['numero_facture']}.pdf",
        tracking_id=facture_data["numero_facture"],
    )

    print("✅ Facture générée et soumise en un seul flux")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def exemple_rechercher_flux_afnor(client: FactPulseClient):
    """Recherche des flux de facturation AFNOR."""
    print("\n" + "=" * 60)
    print("7c. RECHERCHER FLUX AFNOR")
    print("=" * 60)

    # Signature: rechercher_flux_afnor(tracking_id=None, status=None, offset=0, limit=25)
    result = client.rechercher_flux_afnor(
        tracking_id="FAC-2025-001",  # Filtrer par tracking_id
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
    print("7d. TÉLÉCHARGER FLUX AFNOR")
    print("=" * 60)

    # Signature: telecharger_flux_afnor(flow_id)
    pdf_bytes = client.telecharger_flux_afnor(flow_id)

    output_path = f"flux_{flow_id}.pdf"
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)

    print(f"✅ Flux téléchargé: {output_path} ({len(pdf_bytes)} bytes)")

    return output_path


def exemple_rechercher_siret_afnor(client: FactPulseClient, siret: str):
    """Recherche une entreprise par SIRET dans le Directory Service AFNOR."""
    print("\n" + "=" * 60)
    print("7e. RECHERCHER SIRET AFNOR")
    print("=" * 60)

    # Signature: rechercher_siret_afnor(siret)
    result = client.rechercher_siret_afnor(siret)

    print(f"🔍 SIRET: {siret}")
    print(f"   Trouvé: {result.get('found', False)}")
    if result.get("found"):
        print(f"   Raison sociale: {result.get('raison_sociale')}")
        print(f"   Adresse: {result.get('adresse')}")

    return result


def exemple_rechercher_siren_afnor(client: FactPulseClient, siren: str):
    """Recherche une entreprise par SIREN dans le Directory Service AFNOR."""
    print("\n" + "=" * 60)
    print("7f. RECHERCHER SIREN AFNOR")
    print("=" * 60)

    # Signature: rechercher_siren_afnor(siren)
    result = client.rechercher_siren_afnor(siren)

    print(f"🔍 SIREN: {siren}")
    print(f"   Trouvé: {result.get('found', False)}")

    return result


def exemple_lister_codes_routage_afnor(client: FactPulseClient, siren: str):
    """Liste les codes de routage d'une entreprise."""
    print("\n" + "=" * 60)
    print("7g. LISTER CODES ROUTAGE AFNOR")
    print("=" * 60)

    # Signature: lister_codes_routage_afnor(siren)
    codes = client.lister_codes_routage_afnor(siren)

    print(f"🔍 SIREN: {siren}")
    print(f"📊 Codes de routage: {len(codes)}")

    for code in codes:
        print(f"   - {code.get('code')}: {code.get('description', 'N/A')}")

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

    # Lire le PDF source
    with open(pdf_source_path, "rb") as f:
        pdf_source = f.read()

    # Utiliser generer_facturx_complet() qui fait tout en une fois
    # Signature: generer_facturx_complet(
    #     facture, pdf_source_path=None, pdf_source_bytes=None, profil="EN16931",
    #     valider=True, signer=False, soumettre_afnor=False,
    #     afnor_flow_name=None, afnor_tracking_id=None,
    #     output_path=None, timeout=120000
    # )
    result = client.generer_facturx_complet(
        facture=facture_data,
        pdf_source_bytes=pdf_source,  # ou pdf_source_path="chemin/vers/pdf"
        profil="EN16931",
        valider=True,  # Valider le PDF après génération
        signer=True,  # Signer avec le certificat serveur
        soumettre_afnor=True,  # Soumettre à la PDP AFNOR
        afnor_flow_name=f"Facture {facture_data['numero_facture']}",
        afnor_tracking_id=facture_data["numero_facture"],
        output_path="facture_complete.pdf",
        timeout=180000,  # 3 minutes
    )

    print("✅ Workflow complet terminé:")
    print(f"   PDF généré: {result.get('pdf_bytes') is not None}")
    print(f"   Validation: {result.get('validation', {}).get('est_conforme', 'N/A')}")
    print(f"   Signé: {result.get('signe', False)}")
    print(f"   Soumis AFNOR: {result.get('soumis_afnor', False)}")
    if result.get("afnor"):
        print(f"   Flow ID: {result['afnor'].get('flowId')}")

    return result


# =============================================================================
# 9. GESTION DES ERREURS
# =============================================================================


def exemple_gestion_erreurs():
    """Démontre la gestion des erreurs du SDK."""
    print("\n" + "=" * 60)
    print("9. GESTION DES ERREURS")
    print("=" * 60)

    # Erreur d'authentification
    print("\n--- FactPulseAuthError ---")
    try:
        bad_client = FactPulseClient(
            email="mauvais@email.com",
            password="mauvais_mot_de_passe",
        )
        bad_client.ensure_authenticated()
    except FactPulseAuthError as e:
        print(f"✅ Erreur capturée: {e}")

    # Erreur de validation
    print("\n--- FactPulseValidationError ---")
    print("   Les erreurs de validation contiennent une liste d'erreurs détaillées:")
    print("   - e.errors: List[ValidationErrorDetail]")
    print("   - Chaque erreur a: field, message, code")

    # Timeout
    print("\n--- FactPulsePollingTimeout ---")
    print("   Se produit quand une tâche async dépasse le timeout configuré")
    print("   Paramètres: timeout en ms (défaut: 120000 = 2 minutes)")


# =============================================================================
# MAIN
# =============================================================================


def main():
    """Point d'entrée principal."""
    print("=" * 60)
    print("EXEMPLE EXHAUSTIF SDK FACTPULSE PYTHON")
    print("=" * 60)
    print("Version SDK: 2.0.21")
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
        # exemple_workflow_complet(client, pdf_source)
    else:
        print("\n💡 Pour tester la génération, fournissez un PDF source:")
        print(f"   python {sys.argv[0]} facture_source.pdf")

    # Démontrer les helpers (toujours)
    exemple_helpers_construction_facture()

    # Démontrer la recherche Chorus Pro (si credentials configurés)
    # exemple_rechercher_structure_chorus(client, "35600000000048")

    # Démontrer AFNOR (si credentials configurés)
    # exemple_healthcheck_afnor(client)

    print("\n" + "=" * 60)
    print("✅ EXEMPLES TERMINÉS")
    print("=" * 60)


if __name__ == "__main__":
    main()
