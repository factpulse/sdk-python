"""Test that all SDK modules can be imported correctly."""

import pytest


class TestImports:
    """Test module imports."""

    def test_import_factpulse(self):
        """Test main package import."""
        import factpulse
        assert factpulse is not None

    def test_import_models(self):
        """Test models import."""
        from factpulse import models
        assert models is not None

    def test_import_api_client(self):
        """Test API client import."""
        from factpulse import ApiClient
        assert ApiClient is not None

    def test_import_configuration(self):
        """Test configuration import."""
        from factpulse import Configuration
        assert Configuration is not None

    def test_import_helpers(self):
        """Test helpers import."""
        from factpulse.helpers import FactPulseClient
        assert FactPulseClient is not None


class TestHelperFunctions:
    """Test helper factory functions."""

    def test_supplier_helper(self):
        """Test supplier helper function."""
        from factpulse.helpers import supplier
        result = supplier(
            name="Test Company",
            siret="12345678901234",
            address_line1="123 Test St",
            postal_code="75001",
            city="Paris"
        )
        assert result is not None
        assert result["name"] == "Test Company"

    def test_recipient_helper(self):
        """Test recipient helper function."""
        from factpulse.helpers import recipient
        result = recipient(
            name="Client Company",
            siret="98765432109876",
            address_line1="456 Client Ave",
            postal_code="69001",
            city="Lyon"
        )
        assert result is not None
        assert result["name"] == "Client Company"

    def test_invoice_line_helper(self):
        """Test invoice_line helper function."""
        from factpulse.helpers import invoice_line
        result = invoice_line(
            number=1,
            description="Test service",
            quantity=1,
            unit_price=100.00,
            line_total=100.00
        )
        assert result is not None
        assert result["description"] == "Test service"

    def test_vat_line_helper(self):
        """Test vat_line helper function."""
        from factpulse.helpers import vat_line
        result = vat_line(
            base_amount=100.00,
            vat_amount=20.00,
            rate="20.00"
        )
        assert result is not None
        assert result["baseAmount"] == 100.00
