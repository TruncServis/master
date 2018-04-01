# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    _description = "Account invoice"

    @api.one
    @api.depends('amount_untaxed', 'amount_tax')
    def _amount_tefkifat(self):
        a = 847
        if self.amount_untaxed > a:
            self.tefkifat_otuz = (self.amount_tax * 30) / 100
            self.tefkifat_yetmis = (self.amount_tax * 70) / 100
            self.tefkifat_amount = (self.amount_untaxed + self.tefkifat_otuz)

    tefkifat_otuz = fields.Float(compute='_amount_tefkifat', string=u'Tefkifat 30', default=0)
    tefkifat_yetmis = fields.Float(compute='_amount_tefkifat', string=u'Tefkifat 70', default=0)
    tefkifat_amount = fields.Float(compute='_amount_tefkifat', string=u'Tefkifat Toplam', default=0)
