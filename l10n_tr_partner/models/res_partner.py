# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _get_default_country(self):
        return self.env['res.country'].search([('name', '=', 'Turkey')], limit=1)

    @api.model
    def _get_default_state(self):
        return self.env['res.country.state'].search([('country_id', '=', 'TR'), ('code', '=', '34')], limit=1)

    # @api.model
    # def force_lang(self, lang='tr_TR'):
    #     for partner in self.env['res.partner'].search([]):
    #         partner.lang = lang

    tax_office_id = fields.Many2one('tax.offices', 'Tax Offices', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', change_default=True, default=_get_default_country)
    state_id = fields.Many2one('res.country.state', string='City', change_default=True, default=_get_default_state)

    @api.model
    def _commercial_fields(self):
        return super(ResPartner, self)._commercial_fields() + ['tax_office_id']

    # def _fields_sync(self, values):
    #     """ Sync commercial fields and address fields from company and to children after create/update,
    #     just as if those were all modeled as fields.related to the parent """
    #     # 1. From UPSTREAM: sync from parent
    #     if values.get('parent_id') or values.get('type', 'contact'):
    #         # 1a. Commercial fields: sync if parent changed
    #         if values.get('parent_id'):
    #             self._commercial_sync_from_company()
    #
    #     # 2. To DOWNSTREAM: sync children
    #     if self.child_ids:
    #         # 2a. Commercial Fields: sync if commercial entity
    #         if self.commercial_partner_id == self:
    #             commercial_fields = self._commercial_fields()
    #             if any(field in values for field in commercial_fields):
    #                 self._commercial_sync_to_children()
    #         for child in self.child_ids.filtered(lambda c: not c.is_company):
    #             if child.commercial_partner_id != self.commercial_partner_id:
    #                 self._commercial_sync_to_children()
    #
    #                 break
