# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class TaxOffices(models.Model):
    _name = 'tax.offices'
    _description = 'Turkey tax offices'

    name = fields.Char(required=True, string='Name')
    code = fields.Char(string='Code')
    city = fields.Char(required=True, string='City')
    active = fields.Boolean(string='Active')
