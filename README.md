# FactPulse SDK Python

Official Python client for the FactPulse API - French electronic invoicing.

## Features

- **Factur-X**: Generation and validation of electronic invoices (MINIMUM, BASIC, EN16931, EXTENDED profiles)
- **Chorus Pro**: Integration with the French public invoicing platform
- **AFNOR PDP/PA**: Submission of flows compliant with XP Z12-013 standard
- **Electronic signature**: PDF signing (PAdES-B-B, PAdES-B-T, PAdES-B-LT)
- **Simplified client**: JWT authentication and polling integrated

## Installation

```bash
pip install factpulse
```

## Quick Start

```python
from factpulse import (
    FactPulseClient,
    supplier,
    recipient,
    invoice_line,
    invoice_totals,
    vat_line,
)

# Create the client
client = FactPulseClient(
    email="your_email@example.com",
    password="your_password"
)

# Build the invoice
invoice_data = {
    "number": "INV-2025-001",
    "date": "2025-01-15",
    "supplier": supplier(
        name="My Company SAS",
        siret="12345678901234",
        address_line1="123 Example Street",
        postal_code="75001",
        city="Paris",
    ),
    "recipient": recipient(
        name="Client SARL",
        siret="98765432109876",
        address_line1="456 Test Avenue",
        postal_code="69001",
        city="Lyon",
    ),
    "totals": invoice_totals(
        total_excl_tax=1000.00,
        total_vat=200.00,
        total_incl_tax=1200.00,
        amount_due=1200.00,
    ),
    "lines": [
        invoice_line(
            line_number=1,
            description="Consulting services",
            quantity=10,
            unit_price_excl_tax=100.00,
            line_total_excl_tax=1000.00,
        )
    ],
    "vatLines": [
        vat_line(base_amount_excl_tax=1000.00, vat_amount=200.00, rate_value="20.00")
    ],
}

# Generate the Factur-X PDF
with open("source_invoice.pdf", "rb") as f:
    pdf_source = f.read()

pdf_bytes = client.generate_facturx(
    invoice_data=invoice_data,
    pdf_source=pdf_source,
    profile="EN16931",
    sync=True,
)

with open("facturx_invoice.pdf", "wb") as f:
    f.write(pdf_bytes)
```

## Alternative Import (backward compatible)

You can also import from `factpulse_helpers` directly:

```python
from factpulse_helpers import FactPulseClient, supplier, recipient
```

## API Reference

See [FactPulse API Documentation](https://factpulse.fr/docs)

## License

MIT
