# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ['tax_offices']
        return res

    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'TR')], limit=1)
        return country

    @api.model
    def _get_default_state(self):
        state = self.env['res.country.state'].search([('code', '=', '344')], limit=1)
        return state

    # notify_email = fields.Selection(default='none')
    vat_department = fields.Char(string='Vat Deparmen')
    tax_offices = fields.Many2one('tax.offices', 'Tax Offices')
    country_id = fields.Many2one('res.country', string='Country', change_default=True, default=_get_default_country)
    state_id = fields.Many2one('res.country.state', string='City', change_default=True, default=_get_default_state)
