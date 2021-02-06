# -*- coding: utf-8 -*-

from odoo.exceptions import AccessError
from odoo import api, fields, models, _
from odoo import SUPERUSER_ID

import logging

_logger = logging.getLogger(__name__)


class AccountTaxTemplate(models.Model):
    _name = 'account.tax.template'
    _description = 'Templates for Taxes'

    @api.multi
    def _generate_tax(self, company):
        """ This method generate taxes from templates.

            :param company: the company for which the taxes should be created from templates in self
            :returns: {
                'tax_template_to_tax': mapping between tax template and the newly generated taxes corresponding,
                'account_dict': dictionary containing a to-do list with all the accounts to assign on new taxes
            }
        """
        todo_dict = {}
        tax_template_to_tax = {}
        for tax in self:
            # Compute children tax ids
            children_ids = []
            for child_tax in tax.children_tax_ids:
                if tax_template_to_tax.get(child_tax.id):
                    children_ids.append(tax_template_to_tax[child_tax.id])
            vals_tax = tax._get_tax_vals(company)
            vals_tax['children_tax_ids'] = children_ids and [(6, 0, children_ids)] or []
            new_tax = self.env['account.chart.template'].create_record_with_xmlid(company, tax, 'account.tax', vals_tax)
            tax_template_to_tax[tax.id] = new_tax
            # Since the accounts have not been created yet, we have to wait before filling these fields
            todo_dict[new_tax] = {
                'account_id': tax.account_id.id,
                'refund_account_id': tax.refund_account_id.id,
            }

        return {
            'tax_template_to_tax': tax_template_to_tax,
            'account_dict': todo_dict
        }
