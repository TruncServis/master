# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResBank(models.Model):
    _inherit = 'res.bank'

    teleks = fields.Char(string='Telex')
    eft_code = fields.Char(string='EFT Code')
    website = fields.Char(string="Website of Bank")
    branch_code = fields.Char(string="Branch Code")
    branch_name = fields.Char(string="Branch Name")


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    branch_code = fields.Char(string="Branch Code")
    branch_name = fields.Char(string="Branch Name")
