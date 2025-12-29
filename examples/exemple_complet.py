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
Version: 3.0.7
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
    amount,
    invoice_totals,
    invoice_line,
    vat_line,
    postal_address,
    electronic_address,
    supplier,
    recipient,
    payee,  # Pour l'affacturage (BG-10 / PayeeTradeParty)
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
    # Helper amount() - convertit n'importe quel type en string formaté
    # -------------------------------------------------------------------------
    print("\n--- amount(value) ---")
    print("Convertit une valeur en string de montant pour l'API.")
    print(f"  amount(100.50) = '{amount(100.50)}'")  # "100.50"
    print(f"  amount('200.00') = '{amount('200.00')}'")  # "200.00"
    print(f"  amount(1000) = '{amount(1000)}'")  # "1000.00"
    print(f"  amount(None) = '{amount(None)}'")  # "0.00"

    # -------------------------------------------------------------------------
    # Helper invoice_totals() - builds the invoice totals block
    # -------------------------------------------------------------------------
    print(
        "\n--- invoice_totals(total_excl_tax, total_vat, total_incl_tax, amount_due, discount_incl_tax=None, discount_reason=None, prepayment=None) ---"
    )
    print("Creates a simplified InvoiceTotals object.")
    total = invoice_totals(
        total_excl_tax=1000.00,
        total_vat=200.00,
        total_incl_tax=1200.00,
        amount_due=1200.00,
    )
    print(f"  invoice_totals(1000, 200, 1200, 1200) = {total}")
    # Résultat: {'totalNetAmount': '1000.00', 'vatAmount': '200.00',
    #            'totalGrossAmount': '1200.00', 'amountDue': '1200.00'}

    # Avec remise et acompte
    total_avec_remise = invoice_totals(
        total_excl_tax=1000.00,
        total_vat=180.00,
        total_incl_tax=1080.00,
        amount_due=980.00,
        discount_incl_tax=100.00,
        discount_reason="Remise fidélité",
        prepayment=100.00,
    )
    print(f"  invoice_totals avec remise = {total_avec_remise}")

    # -------------------------------------------------------------------------
    # Helper invoice_line() - builds an invoice line
    # -------------------------------------------------------------------------
    print("\n--- invoice_line() ---")
    print("Creates an invoice line item for the FactPulse API.")
    print("Signature: invoice_line(line_number, description, quantity, unit_price_excl_tax,")
    print(
        "                           line_total_excl_tax, vat_rate_code=None, vat_rate_value='20.00',"
    )
    print("                           vat_category='S', unit='LUMP_SUM', reference=None, ...)")

    # Basic example with vat_rate_value (default 20%)
    line1 = invoice_line(
        line_number=1,
        description="IT consulting services",
        quantity=5,
        unit_price_excl_tax=200.00,
        line_total_excl_tax=1000.00,  # 5 x 200
        unit="HOUR",
        reference="REF-001",
    )
    print(f"  Line 1 (VAT 20% default): {line1}")

    # Example with predefined VAT code (vat_rate_code)
    line2 = invoice_line(
        line_number=2,
        description="Documentation technique",
        quantity=1,
        unit_price_excl_tax=500.00,
        line_total_excl_tax=500.00,
        vat_rate_code="VAT10",  # Code TVA au lieu de valeur
        unit="LUMP_SUM",
    )
    print(f"  Line 2 (with VAT10 code): {line2}")

    # Exemple avec TVA à taux réduit (5.5%)
    ligne3 = invoice_line(
        line_number=3,
        description="Produit alimentaire",
        quantity=10,
        unit_price_excl_tax=5.50,
        line_total_excl_tax=55.00,
        vat_rate_value="5.50",
        vat_category="S",
        unit="PIECE",
    )
    print(f"  Ligne 3 (TVA 5.5%): {ligne3}")

    # Exemple avec remise
    ligne4 = invoice_line(
        line_number=4,
        description="Prestation avec remise",
        quantity=2,
        unit_price_excl_tax=300.00,
        line_total_excl_tax=540.00,  # 600 - 60 (10% remise)
        discount_excl_tax=60.00,
        discount_reason_code="95",  # Code standard
        discount_reason="Remise commerciale 10%",
    )
    print(f"  Ligne 4 (avec remise): {ligne4}")

    # Exemple avec période de facturation
    ligne5 = invoice_line(
        line_number=5,
        description="Abonnement mensuel",
        quantity=1,
        unit_price_excl_tax=99.00,
        line_total_excl_tax=99.00,
        period_start_date="2025-01-01",
        period_end_date="2025-01-31",
    )
    print(f"  Ligne 5 (avec période): {ligne5}")

    # -------------------------------------------------------------------------
    # Helper vat_line() - construit une ligne de TVA
    # -------------------------------------------------------------------------
    print("\n--- vat_line() ---")
    print("Crée une ligne de TVA pour l'API FactPulse.")
    print(
        "Signature: vat_line(base_amount_excl_tax, vat_amount, rate_code=None, rate_value='20.00', category='S')"
    )

    # Exemple avec taux manuel
    tva1 = vat_line(
        base_amount_excl_tax=1000.00,
        vat_amount=200.00,
        rate_value="20.00",
        category="S",  # S = Standard
    )
    print(f"  TVA 20%: {tva1}")

    # Exemple avec code taux
    tva2 = vat_line(
        base_amount_excl_tax=500.00,
        vat_amount=50.00,
        rate_code="VAT10",
        category="S",
    )
    print(f"  TVA 10% (code): {tva2}")

    # Catégories TVA disponibles:
    # S = Standard, Z = Zéro, E = Exonéré, AE = Autoliquidation, K = Intracommunautaire

    # -------------------------------------------------------------------------
    # Helper postal_address() - construit une adresse
    # -------------------------------------------------------------------------
    print("\n--- postal_address() ---")
    print("Crée une adresse postale pour l'API FactPulse.")
    print(
        "Signature: postal_address(line1, postal_code, city, country='FR', line2=None, line3=None)"
    )

    adresse = postal_address(
        line1="123 Rue de la République",
        postal_code="75001",
        city="Paris",
    )
    print(f"  Adresse simple: {adresse}")

    adresse_complete = postal_address(
        line1="456 Avenue des Champs-Élysées",
        postal_code="75008",
        city="Paris",
        country="FR",
        line2="Bâtiment A, 3ème étage",
        line3="Bureau 301",
    )
    print(f"  Adresse complète: {adresse_complete}")

    # -------------------------------------------------------------------------
    # Helper electronic_address() - construit une adresse électronique
    # -------------------------------------------------------------------------
    print("\n--- electronic_address() ---")
    print("Crée une adresse électronique pour l'API FactPulse.")
    print("Signature: electronic_address(identifier, scheme_id='0009')")
    print("Schemes: 0009=SIREN, 0225=FR-SIRET, 0088=EAN, 0096=DUNS, 0130=Codification propre")

    adresse_elec_siren = electronic_address("123456789", "0009")  # SIREN
    print(f"  Adresse SIREN: {adresse_elec_siren}")

    adresse_elec_siret = electronic_address("12345678901234", "0225")  # SIRET
    print(f"  Adresse SIRET: {adresse_elec_siret}")

    # -------------------------------------------------------------------------
    # Helper supplier() - construit les données fournisseur complètes
    # -------------------------------------------------------------------------
    print("\n--- supplier() ---")
    print("Crée un fournisseur (émetteur) avec auto-calcul SIREN et TVA intracommunautaire.")
    print("Signature: supplier(name, siret, address_line1, postal_code, city,")
    print("                       supplier_id=0, siren=None, vat_number=None,")
    print("                       iban=None, country='FR', address_line2=None, ...)")

    fourn = supplier(
        name="Ma Société SAS",
        siret="12345678900001",
        address_line1="123 Rue de la République",
        postal_code="75001",
        city="Paris",
        iban="FR7630006000011234567890189",
    )
    print(f"  Fournisseur (auto-calcul SIREN/TVA): {fourn}")
    # Le helper calcule automatiquement:
    # - siren: 123456789 (extrait du SIRET)
    # - vatNumber: FR12123456789 (calculé depuis le SIREN)
    # - electronicAddress et postalAddress

    # Exemple avec tous les paramètres
    fourn_complet = supplier(
        name="Grande Entreprise SA",
        siret="98765432100001",
        address_line1="1 Place de l'Entreprise",
        postal_code="69001",
        city="Lyon",
        country="FR",
        address_line2="Tour Europa",
        iban="FR7630004000031234567890143",
        vat_number="FR12987654321",  # Fourni manuellement
        service_code=12345,  # ID service Chorus Pro
        bank_details_code=67890,  # Code coordonnées bancaires Chorus Pro
    )
    print(f"  Fournisseur complet: {fourn_complet}")

    # -------------------------------------------------------------------------
    # Helper recipient() - construit les données destinataire complètes
    # -------------------------------------------------------------------------
    print("\n--- recipient() ---")
    print("Crée un destinataire (client) avec auto-calcul SIREN.")
    print("Signature: recipient(name, siret, address_line1, postal_code, city,")
    print("                        siren=None, country='FR', address_line2=None,")
    print("                        service_code=None)")

    dest = recipient(
        name="Client SARL",
        siret="98765432109876",
        address_line1="456 Avenue des Champs",
        postal_code="69001",
        city="Lyon",
    )
    print(f"  Destinataire simple: {dest}")

    # Avec code service (pour Chorus Pro)
    dest_chorus = recipient(
        name="Ministère de l'Économie",
        siret="11004601800013",
        address_line1="139 Rue de Bercy",
        postal_code="75012",
        city="Paris",
        service_code="SERVICE_COMPTA",
    )
    print(f"  Destinataire Chorus Pro: {dest_chorus}")

    # -------------------------------------------------------------------------
    # Helper payee() - construit les données du factor (affacturage)
    # -------------------------------------------------------------------------
    print("\n--- payee() ---")
    print("Crée un bénéficiaire (factor) pour l'affacturage.")
    print("Signature: payee(name, siret=None, siren=None, iban=None, bic=None)")
    print("\nL'affacturage permet de céder une créance à un factor qui reçoit le paiement.")
    print("Types de documents affacturés: 393 (facture), 396 (avoir), 501, 502, 472, 473")

    factor = payee(
        name="FACTOR SAS",
        siret="30000000700033",
        iban="FR76 3000 4000 0500 0012 3456 789",
    )
    print(f"  Factor (auto-calcul SIREN): {factor}")
    # Le helper calcule automatiquement:
    # - siren: 300000007 (extrait du SIRET)

    # Exemple minimal (juste le nom)
    factor_minimal = payee(name="Mon Factor")
    print(f"  Factor minimal: {factor_minimal}")

    return {
        "invoice_totals": total,
        "lines": [line1, line2, ligne3, ligne4, ligne5],
        "vat": [tva1, tva2],
        "supplier": fourn,
        "recipient": dest,
        "payee": factor,
    }


def build_complete_invoice():
    """Build a complete invoice using all helpers.

    This function shows how to assemble an invoice ready to be
    sent to the FactPulse API for Factur-X generation.
    """

    # Dates
    invoice_date = date.today().isoformat()
    due_date = (date.today() + timedelta(days=30)).isoformat()

    return {
        "invoiceNumber": f"FAC-{date.today().year}-001",
        "invoiceDate": invoice_date,
        "paymentDueDate": due_date,
        "depositMode": "DEPOT_PDF_API",
        # Supplier with helper (auto-generates addresses and VAT)
        "supplier": supplier(
            name="Ma Société SAS",
            siret="12345678900001",
            address_line1="123 Rue de la République",
            postal_code="75001",
            city="Paris",
            iban="FR7630006000011234567890189",
        ),
        # Recipient with helper
        "recipient": recipient(
            name="Client SARL",
            siret="98765432109876",
            address_line1="456 Avenue des Champs",
            postal_code="69001",
            city="Lyon",
        ),
        # References
        "references": {
            "invoiceType": "INVOICE",
            "vatType": "VAT_ON_DEBIT",
            "paymentMethod": "TRANSFER",
            "invoiceCurrency": "EUR",
            "purchaseOrderNumber": "CMD-2025-042",
        },
        # Lignes de poste avec helper
        "invoiceLines": [
            invoice_line(
                line_number=1,
                description="Prestation de conseil",
                quantity=5,
                unit_price_excl_tax=200.00,
                line_total_excl_tax=1000.00,
                vat_rate_value="20.00",
                unit="HOUR",
                reference="REF-CONSEIL-001",
            ),
            invoice_line(
                line_number=2,
                description="Formation développeurs",
                quantity=3,
                unit_price_excl_tax=500.00,
                line_total_excl_tax=1500.00,
                vat_rate_value="20.00",
                unit="DAY",
                reference="REF-FORM-002",
            ),
        ],
        # Lignes de TVA avec helper
        "vatLines": [
            vat_line(
                base_amount_excl_tax=2500.00,
                vat_amount=500.00,
                rate_value="20.00",
                category="S",
            ),
        ],
        # Montant total avec helper
        "invoiceTotals": invoice_totals(
            total_excl_tax=2500.00,
            total_vat=500.00,
            total_incl_tax=3000.00,
            amount_due=3000.00,
        ),
        "comment": "Facture pour prestations du mois en cours",
    }


def build_factored_invoice():
    """Build a complete factored invoice using all helpers.

    Factoring allows assigning a receivable to a factor who receives the payment.
    For a factored invoice, you need:
    1. A factored document type (393 = factored invoice)
    2. A payee (the factor)
    3. An ACC note with the subrogation mention
    4. The factor's IBAN (not the supplier's)
    """

    # Dates
    invoice_date = date.today().isoformat()
    due_date = (date.today() + timedelta(days=30)).isoformat()

    return {
        "invoiceNumber": f"FAC-{date.today().year}-001-AFF",
        "invoiceDate": invoice_date,
        "paymentDueDate": due_date,
        "depositMode": "DEPOT_PDF_API",
        # Supplier (invoice issuer)
        "supplier": supplier(
            name="Ma Société SAS",
            siret="12345678900001",
            address_line1="123 Rue de la République",
            postal_code="75001",
            city="Paris",
            # Note: the supplier's IBAN is not used for payment
            # as the payee (factor) has its own IBAN
        ),
        # Recipient (customer who pays)
        "recipient": recipient(
            name="Client SARL",
            siret="98765432109876",
            address_line1="456 Avenue des Champs",
            postal_code="69001",
            city="Lyon",
        ),
        # PAYEE (factor) - receives the payment
        "payee": payee(
            name="FACTOR SAS",
            siret="30000000700033",
            iban="FR76 3000 4000 0500 0012 3456 789",  # Factor's IBAN
            bic="BNPAFRPP",
        ),
        # References - FACTORED TYPE
        "references": {
            "invoiceType": "393",  # 393 = Facture affacturée (voir BR-FR-04)
            "vatType": "VAT_ON_DEBIT",
            "paymentMethod": "TRANSFER",
            "invoiceCurrency": "EUR",
            "purchaseOrderNumber": "CMD-2025-042",
        },
        # Notes obligatoires incluant ACC (subrogation)
        "notes": [
            {
                "content": "Taux de pénalités de retard : 3 fois le taux d'intérêt légal",
                "subjectCode": "PMD",  # Pénalités de retard
            },
            {
                "content": "Indemnité forfaitaire pour frais de recouvrement : 40 €",
                "subjectCode": "PMT",  # Modalités de paiement
            },
            {
                "content": "Pas d'escompte pour paiement anticipé",
                "subjectCode": "AAB",  # Escompte
            },
            {
                # NOTE ACC OBLIGATOIRE pour l'affacturage (BR-FR-05)
                "content": "Cette créance a été cédée à FACTOR SAS. "
                "Tout paiement doit être effectué à l'ordre du factor. "
                "Contrat n° AFF-2025-001",
                "subjectCode": "ACC",  # Clause de subrogation factoring
            },
        ],
        # Lignes de poste
        "invoiceLines": [
            invoice_line(
                line_number=1,
                description="Prestation de conseil",
                quantity=5,
                unit_price_excl_tax=200.00,
                line_total_excl_tax=1000.00,
                vat_rate_value="20.00",
                unit="HOUR",
            ),
        ],
        # Lignes de TVA
        "vatLines": [
            vat_line(
                base_amount_excl_tax=1000.00,
                vat_amount=200.00,
                rate_value="20.00",
                category="S",
            ),
        ],
        # Montant total
        "invoiceTotals": invoice_totals(
            total_excl_tax=1000.00,
            total_vat=200.00,
            total_incl_tax=1200.00,
            amount_due=1200.00,
        ),
        "comment": "Facture affacturée - Paiement à effectuer au factor",
    }


# =============================================================================
# 3. GÉNÉRATION DE FACTURES FACTUR-X
# =============================================================================


def example_generate_facturx(client: FactPulseClient, pdf_source_path: str):
    """Generates a Factur-X invoice from a source PDF."""
    print("\n" + "=" * 60)
    print("3. FACTUR-X GENERATION")
    print("=" * 60)

    # Build invoice data with helpers
    invoice_data = build_complete_invoice()

    print(f"📄 PDF source: {pdf_source_path}")
    print(f"📝 Invoice: {invoice_data['invoiceNumber']}")

    try:
        # Generate Factur-X PDF (synchronous mode with automatic polling)
        # The method accepts:
        # - invoice_data: dict, JSON string, or Pydantic model
        # - pdf_source: bytes or path (str/Path)
        pdf_bytes = client.generate_facturx(
            invoice_data=invoice_data,
            pdf_source=pdf_source_path,  # Path to source PDF
            profile="EN16931",  # MINIMUM, BASIC, EN16931, EXTENDED
            output_format="pdf",  # pdf or xml
            sync=True,  # Wait for result with automatic polling
            timeout=120000,  # Timeout in ms (2 minutes)
        )

        # Save result
        output_path = f"invoice_facturx_{invoice_data['invoiceNumber']}.pdf"
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

        print(f"✅ Factur-X PDF generated: {output_path} ({len(pdf_bytes)} bytes)")
        return output_path

    except FactPulseValidationError as e:
        print(f"❌ Validation error: {e}")
        for error in e.errors:
            print(f"   - [{error.item}] {error.reason}")
        raise
    except FactPulsePollingTimeout as e:
        print(f"❌ Generation timeout: {e}")
        raise


def example_generate_facturx_async(client: FactPulseClient, pdf_source_path: str):
    """Generates a Factur-X invoice in asynchronous mode (manual polling)."""
    print("\n" + "=" * 60)
    print("3b. FACTUR-X GENERATION (ASYNC)")
    print("=" * 60)

    invoice_data = build_complete_invoice()

    # Async mode: returns immediately with a task_id
    task_id = client.generate_facturx(
        invoice_data=invoice_data,
        pdf_source=pdf_source_path,
        profile="EN16931",
        sync=False,  # Don't wait
    )

    print(f"📋 Task created: {task_id}")

    # Manual polling with poll_task method
    result = client.poll_task(
        task_id.decode() if isinstance(task_id, bytes) else task_id, timeout=120000
    )

    if result.get("content_b64"):
        import base64

        pdf_bytes = base64.b64decode(result["content_b64"])
        print(f"✅ Generation completed: {len(pdf_bytes)} bytes")
        return pdf_bytes
    else:
        print(f"❌ Unexpected result: {result}")
        return None


# =============================================================================
# 4. VALIDATION DE PDF/XML FACTUR-X
# =============================================================================


def example_validate_facturx_pdf(client: FactPulseClient, pdf_path: str):
    """Validates an existing Factur-X PDF."""
    print("\n" + "=" * 60)
    print("4. FACTUR-X PDF VALIDATION")
    print("=" * 60)

    result = client.validate_facturx_pdf(
        pdf_path=pdf_path,
        profile="EN16931",
    )

    print(f"📄 PDF validated: {pdf_path}")
    print(f"✅ Compliant: {result.get('is_compliant', False)}")
    print(f"📊 Detected profile: {result.get('detected_profile', 'N/A')}")

    if result.get("errors"):
        print("❌ Errors:")
        for err in result["errors"]:
            print(f"   - {err}")

    if result.get("warnings"):
        print("⚠️ Warnings:")
        for warn in result["warnings"]:
            print(f"   - {warn}")

    return result


def example_validate_pdf_signature(client: FactPulseClient, pdf_path: str):
    """Validates electronic signatures of a PDF."""
    print("\n" + "=" * 60)
    print("4b. PDF SIGNATURE VALIDATION")
    print("=" * 60)

    result = client.validate_pdf_signature(pdf_path=pdf_path)

    print(f"📄 PDF analyzed: {pdf_path}")
    print(f"✍️ Signed: {result.get('is_signed', False)}")

    for sig in result.get("signatures", []):
        print("\n   Signature:")
        print(f"   - Signer: {sig.get('signer_cn', 'N/A')}")
        print(f"   - Date: {sig.get('signing_time', 'N/A')}")
        print(f"   - Valid: {sig.get('valid', False)}")

    return result


# =============================================================================
# 5. SIGNATURE ÉLECTRONIQUE DE PDF
# =============================================================================


def example_sign_pdf(client: FactPulseClient, pdf_path: str):
    """Signs a PDF with the server-side configured certificate.

    Note: The certificate must be pre-configured in Django Admin
    and associated with the JWT's client_uid.
    """
    print("\n" + "=" * 60)
    print("5. PDF ELECTRONIC SIGNATURE")
    print("=" * 60)

    result = client.sign_pdf(
        pdf_path=pdf_path,
        reason="Invoice validation",
        location="Paris, France",
        contact="contact@example.com",
        use_pades_lt=True,  # PAdES-B-LT (long-term archival)
        use_timestamp=True,  # RFC 3161 timestamping
        output_path="signed_invoice.pdf",  # Automatic save
    )

    print(f"✅ PDF signed: {result}")
    return result


def example_generate_test_certificate(client: FactPulseClient):
    """Generates a self-signed X.509 certificate for testing.

    Note: This certificate must then be configured in Django Admin.
    """
    print("\n" + "=" * 60)
    print("5b. TEST CERTIFICATE GENERATION")
    print("=" * 60)

    result = client.generate_test_certificate(
        cn="Test FactPulse",
        organization="Ma Société SAS",
        email="contact@masociete.fr",
        validity_days=365,
        key_size=2048,
    )

    print("✅ Certificate generated")
    print(f"   CN: {result.get('cn')}")
    print(f"   Organization: {result.get('organization')}")
    print(f"   Validity: {result.get('validity_days')} days")

    # Result contains:
    # - certificate_pem: Certificate in PEM format
    # - private_key_pem: Private key in PEM format
    # - pkcs12_base64: PKCS#12 encoded in base64 (for Django Admin)

    return result


# =============================================================================
# 6. INTÉGRATION CHORUS PRO
# =============================================================================


def example_search_structure_chorus(client: FactPulseClient, siret: str):
    """Searches for a Chorus Pro structure by SIRET."""
    print("\n" + "=" * 60)
    print("6. CHORUS PRO STRUCTURE SEARCH")
    print("=" * 60)

    result = client.search_structure_chorus(
        structure_identifier=siret,
        identifier_type="SIRET",
    )

    structures = result.get("structure_list", [])
    print(f"🔍 SIRET search: {siret}")
    print(f"📊 Structures found: {len(structures)}")

    for struct in structures:
        print("\n   Structure:")
        print(f"   - CPP ID: {struct.get('structure_cpp_id')}")
        print(f"   - Name: {struct.get('structure_name')}")
        print(f"   - SIRET: {struct.get('structure_identifier')}")

    return result


def example_get_chorus_id_from_siret(client: FactPulseClient, siret: str):
    """Gets the Chorus Pro ID from a SIRET (simplified helper)."""
    print("\n" + "=" * 60)
    print("6b. GET CHORUS PRO ID FROM SIRET")
    print("=" * 60)

    result = client.get_chorus_id_from_siret(siret)

    print(f"🔍 SIRET: {siret}")
    print(f"📋 Chorus Pro ID: {result.get('structure_cpp_id')}")
    print(f"📋 Name: {result.get('structure_name')}")

    return result


def example_get_structure_details_chorus(client: FactPulseClient, structure_cpp_id: int):
    """Gets details of a Chorus Pro structure."""
    print("\n" + "=" * 60)
    print("6c. CHORUS PRO STRUCTURE DETAILS")
    print("=" * 60)

    result = client.get_structure_details_chorus(structure_cpp_id)

    print(f"📋 Structure #{structure_cpp_id}:")
    print(f"   - Name: {result.get('structure_name')}")
    print(f"   - SIRET: {result.get('structure_identifier')}")

    # Check required parameters
    params = result.get("parameters", {})
    if params.get("service_code_required"):
        print("   ⚠️ Service code REQUIRED")
    if params.get("engagement_number_required"):
        print("   ⚠️ Engagement number REQUIRED")

    return result


def example_list_structure_services_chorus(client: FactPulseClient, structure_cpp_id: int):
    """Lists services of a Chorus Pro structure."""
    print("\n" + "=" * 60)
    print("6d. CHORUS PRO STRUCTURE SERVICES")
    print("=" * 60)

    result = client.list_structure_services_chorus(structure_cpp_id)

    services = result.get("service_list", [])
    print(f"📋 Structure #{structure_cpp_id}")
    print(f"📊 Services found: {len(services)}")

    for svc in services:
        if svc.get("is_active"):
            print("\n   Active service:")
            print(f"   - Code: {svc.get('service_code')}")
            print(f"   - Label: {svc.get('service_label')}")

    return result


def example_submit_invoice_chorus(client: FactPulseClient, structure_cpp_id: int):
    """Submits an invoice to Chorus Pro."""
    print("\n" + "=" * 60)
    print("6e. SUBMIT INVOICE TO CHORUS PRO")
    print("=" * 60)

    result = client.submit_invoice_chorus(
        invoice_number="FAC-2025-001",
        invoice_date="2025-01-15",
        payment_due_date="2025-02-14",
        structure_cpp_id=structure_cpp_id,
        total_net_amount="2500.00",
        vat_amount="500.00",
        total_gross_amount="3000.00",
        service_code="SERVICE01",  # If required by structure
        purchase_order_number="CMD-2025-042",
        comment="Invoice for services",
    )

    print("✅ Invoice submitted to Chorus Pro")
    print(f"   Invoice CPP ID: {result.get('invoice_cpp_id')}")
    print(f"   Deposit flow number: {result.get('deposit_flow_number')}")

    return result


def example_get_invoice_status_chorus(client: FactPulseClient, invoice_cpp_id: int):
    """Gets the status of a Chorus Pro invoice."""
    print("\n" + "=" * 60)
    print("6f. CHORUS PRO INVOICE STATUS")
    print("=" * 60)

    result = client.get_invoice_status_chorus(invoice_cpp_id)

    print(f"📋 Invoice #{invoice_cpp_id}:")
    print(f"   - Number: {result.get('invoice_number')}")
    status = result.get("current_status", {})
    print(f"   - Status: {status.get('code', 'N/A')}")
    print(f"   - Total amount: {result.get('total_gross_amount')}")

    return result


# =============================================================================
# 7. INTÉGRATION AFNOR PDP/PA
# =============================================================================


def example_healthcheck_afnor(client: FactPulseClient):
    """Checks the availability of the AFNOR Flow Service."""
    print("\n" + "=" * 60)
    print("7. AFNOR HEALTHCHECK")
    print("=" * 60)

    result = client.healthcheck_afnor()

    print(f"🏥 AFNOR Status: {result.get('status', 'unknown')}")
    print(f"   Service: {result.get('service', 'N/A')}")

    return result


def example_submit_invoice_afnor(client: FactPulseClient, pdf_path: str):
    """Submits an invoice to a PDP via AFNOR."""
    print("\n" + "=" * 60)
    print("7b. SUBMIT INVOICE AFNOR")
    print("=" * 60)

    # With a file path
    result = client.submit_invoice_afnor(
        flow_name="Invoice FAC-2025-001",
        pdf_path=pdf_path,
        flow_syntax="CII",  # CII or UBL
        flow_profile="EN16931",
        tracking_id="FAC-2025-001",  # Your internal reference
        # sha256 is calculated automatically if not provided
    )

    print("✅ Invoice submitted to AFNOR PDP")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def example_submit_invoice_afnor_bytes(client: FactPulseClient, pdf_bytes: bytes):
    """Submits an invoice to a PDP via AFNOR with bytes."""
    print("\n" + "=" * 60)
    print("7b-bis. SUBMIT INVOICE AFNOR (BYTES)")
    print("=" * 60)

    # With bytes (e.g., after Factur-X generation)
    result = client.submit_invoice_afnor(
        flow_name="Invoice FAC-2025-001",
        pdf_bytes=pdf_bytes,  # Pass bytes directly
        pdf_filename="FAC-2025-001.pdf",  # Filename for upload
        flow_syntax="CII",
        flow_profile="EN16931",
        tracking_id="FAC-2025-001",
    )

    print("✅ Invoice submitted to AFNOR PDP")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def example_generate_and_submit_afnor(client: FactPulseClient, pdf_source_path: str):
    """Generates a Factur-X invoice then submits it directly to AFNOR."""
    print("\n" + "=" * 60)
    print("7c. GENERATE AND SUBMIT AFNOR (OPTIMIZED WORKFLOW)")
    print("=" * 60)

    # Build invoice data
    invoice_data = build_complete_invoice()

    # 1. Generate Factur-X PDF
    print("📄 Generating Factur-X PDF...")
    pdf_facturx = client.generate_facturx(
        invoice_data=invoice_data,
        pdf_source=pdf_source_path,
        profile="EN16931",
        sync=True,
    )
    print(f"   ✅ PDF generated: {len(pdf_facturx)} bytes")

    # 2. Submit bytes directly to AFNOR (without creating a file)
    print("📤 Direct submission to AFNOR...")
    result = client.submit_invoice_afnor(
        flow_name=f"Invoice {invoice_data['invoiceNumber']}",
        pdf_bytes=pdf_facturx,  # Pass bytes directly
        pdf_filename=f"{invoice_data['invoiceNumber']}.pdf",
        tracking_id=invoice_data["invoiceNumber"],
    )

    print("✅ Invoice generated and submitted in one flow")
    print(f"   Flow ID: {result.get('flowId')}")
    print(f"   Tracking ID: {result.get('trackingId')}")
    print(f"   Status: {result.get('status')}")

    return result


def example_search_flows_afnor(client: FactPulseClient, tracking_id: str = None):
    """Searches AFNOR invoice flows."""
    print("\n" + "=" * 60)
    print("7d. SEARCH AFNOR FLOWS")
    print("=" * 60)

    result = client.search_flows_afnor(
        tracking_id=tracking_id,  # Filter by tracking_id
        status=None,  # Filter by status (submitted, processing, delivered, etc.)
        offset=0,
        limit=25,
    )

    flows = result.get("flows", [])
    print(f"📊 Flows found: {result.get('total', len(flows))}")

    for flow in flows:
        print("\n   Flow:")
        print(f"   - Flow ID: {flow.get('flowId')}")
        print(f"   - Tracking ID: {flow.get('trackingId')}")
        print(f"   - Status: {flow.get('status')}")
        print(f"   - Date: {flow.get('createdAt')}")

    return result


def example_download_flow_afnor(client: FactPulseClient, flow_id: str):
    """Downloads the PDF file of an AFNOR flow."""
    print("\n" + "=" * 60)
    print("7e. DOWNLOAD AFNOR FLOW")
    print("=" * 60)

    pdf_bytes = client.download_flow_afnor(flow_id)

    output_path = f"flow_{flow_id}.pdf"
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)

    print(f"✅ Flow downloaded: {output_path} ({len(pdf_bytes)} bytes)")

    return output_path


def example_search_siret_afnor(client: FactPulseClient, siret: str):
    """Searches for a company by SIRET in the AFNOR Directory Service."""
    print("\n" + "=" * 60)
    print("7f. SEARCH SIRET AFNOR")
    print("=" * 60)

    result = client.search_siret_afnor(siret)

    print(f"🔍 SIRET: {siret}")
    print(f"   Result: {result}")

    return result


def example_search_siren_afnor(client: FactPulseClient, siren: str):
    """Searches for a company by SIREN in the AFNOR Directory Service."""
    print("\n" + "=" * 60)
    print("7g. SEARCH SIREN AFNOR")
    print("=" * 60)

    result = client.search_siren_afnor(siren)

    print(f"🔍 SIREN: {siren}")
    print(f"   Result: {result}")

    return result


def example_list_routing_codes_afnor(client: FactPulseClient, siren: str):
    """Lists routing codes of a company."""
    print("\n" + "=" * 60)
    print("7h. LIST AFNOR ROUTING CODES")
    print("=" * 60)

    codes = client.list_routing_codes_afnor(siren)

    print(f"🔍 SIREN: {siren}")
    print(f"📊 Routing codes: {len(codes)}")

    for code in codes:
        print(f"   - {code.get('routing_code')}: {code.get('description', 'N/A')}")

    return codes


# =============================================================================
# 8. WORKFLOW COMPLET
# =============================================================================


def example_complete_workflow(client: FactPulseClient, pdf_source_path: str):
    """Complete workflow: generation + validation + signature + submission."""
    print("\n" + "=" * 60)
    print("8. COMPLETE WORKFLOW")
    print("=" * 60)

    # Build invoice data
    invoice_data = build_complete_invoice()

    # Use generate_facturx_complete() which does everything at once
    result = client.generate_facturx_complete(
        invoice=invoice_data,
        pdf_source_path=pdf_source_path,
        profile="EN16931",
        validate=True,  # Validate PDF after generation
        sign=True,  # Sign with server certificate
        submit_afnor=True,  # Submit to AFNOR PDP
        afnor_flow_name=f"Invoice {invoice_data['invoiceNumber']}",
        afnor_tracking_id=invoice_data["invoiceNumber"],
        output_path="complete_invoice.pdf",
        timeout=180000,  # 3 minutes
    )

    print("✅ Complete workflow finished:")
    print(f"   PDF generated: {result.get('pdf_bytes') is not None}")
    print(f"   Validation: {result.get('validation', {}).get('is_compliant', 'N/A')}")
    print(f"   Signed: {result.get('signature', {}).get('signed', False)}")
    if result.get("afnor"):
        print(f"   AFNOR Flow ID: {result['afnor'].get('flowId')}")
    if result.get("pdf_path"):
        print(f"   File saved: {result['pdf_path']}")

    return result


# =============================================================================
# 9. GESTION DES ERREURS
# =============================================================================


def example_error_handling():
    """Demonstrates SDK error handling."""
    print("\n" + "=" * 60)
    print("9. ERROR HANDLING")
    print("=" * 60)

    # Exception hierarchy:
    # FactPulseError (base)
    #   ├── FactPulseAuthError (401) - Authentication failed
    #   ├── FactPulseValidationError (400, 422) - Validation error with details
    #   ├── FactPulsePollingTimeout - Polling timeout
    #   ├── FactPulseNotFoundError (404) - Resource not found
    #   └── FactPulseServiceUnavailableError (503) - Service unavailable

    print("\n--- FactPulseAuthError (401) ---")
    print("   Occurs when: invalid email/password, expired token")
    try:
        bad_client = FactPulseClient(
            email="bad@email.com",
            password="bad_password",
        )
        bad_client.ensure_authenticated()
    except FactPulseAuthError as e:
        print(f"   ✅ Error caught: {e.message}")

    print("\n--- FactPulseValidationError (400, 422) ---")
    print("   Occurs when: invalid invoice data, non-compliant PDF")
    print("   Contains a list of detailed errors:")
    print("   - e.errors: List[ValidationErrorDetail]")
    print("   - e.error_code: Error code (e.g.: SCHEMATRON_VALIDATION_FAILED)")
    print("   Each error has: level, item, reason, source, code")

    print("\n--- FactPulsePollingTimeout ---")
    print("   Occurs when: an async task exceeds the timeout")
    print("   Properties: task_id, timeout")
    print("   Default parameter: 120000 ms (2 minutes)")

    print("\n--- FactPulseNotFoundError (404) ---")
    print("   Occurs when: AFNOR flow, Chorus Pro structure not found")
    print("   Properties: resource, identifier")

    print("\n--- FactPulseServiceUnavailableError (503) ---")
    print("   Occurs when: AFNOR PDP, Chorus Pro, API unavailable")
    print("   Properties: service_name, original_error")


# =============================================================================
# MAIN
# =============================================================================


def main():
    """Main entry point."""
    print("=" * 60)
    print("COMPREHENSIVE FACTPULSE PYTHON SDK EXAMPLE")
    print("=" * 60)
    print("SDK Version: 3.0.7")
    print(f"API URL: {API_URL}")

    # Check credentials
    if EMAIL == "votre_email@example.com":
        print("\n⚠️  WARNING: Configure your credentials in environment variables:")
        print("   export FACTPULSE_EMAIL='your_email@example.com'")
        print("   export FACTPULSE_PASSWORD='your_password'")
        print("\nThis script will only demonstrate helpers (no API calls).")

        # Demonstrate helpers
        exemple_helpers_construction_facture()

        # Demonstrate error handling
        example_error_handling()

        print("\n✅ Helpers demonstrated successfully!")
        return

    # Create client
    client = exemple_initialisation_simple()

    # Check if a source PDF is provided
    pdf_source = sys.argv[1] if len(sys.argv) > 1 else None

    if pdf_source and Path(pdf_source).exists():
        # Complete workflow with a real PDF
        example_generate_facturx(client, pdf_source)
    else:
        print("\n💡 To test generation, provide a source PDF:")
        print(f"   python {sys.argv[0]} source_invoice.pdf")

    # Demonstrate helpers (always)
    exemple_helpers_construction_facture()

    print("\n" + "=" * 60)
    print("✅ EXAMPLES COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
