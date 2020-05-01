# © 2016 Opener B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import tests
from odoo.tests.common import TransactionCase


@tests.tagged('standard', 'at_install')
class TestInvoice(TransactionCase):
    def test01_compute_has_sale_order(self):
        sale = self.env.ref('sale.sale_order_8')
        sale.action_invoice_create()
        invoice = sale.invoice_ids[0]
        self.assertTrue(invoice.has_sale_order)

        invoice_no_so = self.env.ref('l10n_generic_coa.demo_invoice_extract')
        self.assertFalse(invoice_no_so.has_sale_order)
