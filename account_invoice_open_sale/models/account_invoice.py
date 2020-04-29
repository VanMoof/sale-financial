# coding: utf-8
# © 2016 Opener B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import translate, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    has_sale_order = fields.Boolean(compute='_compute_has_sale_order')

    @api.multi
    def _compute_has_sale_order(self):
        """ Determines if the button to show sale order will be shown on the
        invoice """
        for invoice in self:
            invoice.has_sale_order = bool(
                invoice.mapped('invoice_line_ids.sale_line_ids'))


    @api.multi
    def open_sale_order(self):
        self.ensure_one()
        sale_ids = self.mapped('invoice_line_ids.sale_line_ids.order_id').ids
        return {
            'type': 'ir.actions.act_window',
            'name': _('Sales Orders'),
            'res_model': 'sale.order',
            'view_type': 'form',
            'view_mode': 'form' if len(sale_ids) == 1 else 'tree,form',
            'res_id': sale_ids[0] if len(sale_ids) == 1 else False,
            'domain': [('id', 'in', sale_ids)],
        }
