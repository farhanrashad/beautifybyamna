# -*- coding: utf-8 -*-

from odoo import models, fields


class InvoicePartnerBalance(models.Model):
    _inherit = 'account.invoice'

    balance = fields.Monetary(related="partner_id.total_due", string="Balance", readonly=True)
