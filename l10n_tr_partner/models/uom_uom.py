from odoo import api, fields, models, _


class UoM(models.Model):
    _inherit = 'uom.uom'

    uom_code = fields.Char(string='Birim Kodu')