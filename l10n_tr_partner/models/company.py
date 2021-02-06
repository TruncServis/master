# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, tools, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    tax_office_id = fields.Many2one('tax.offices', related='partner_id.tax_office_id', string='Tax Offices', )
