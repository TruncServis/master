# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import datetime
from datetime import datetime

from odoo import SUPERUSER_ID

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    reconciliation_letter = fields.Boolean('Reconciliation Letter', default=False)

    # @api.model
    def get_date(self):
        today = datetime.now().date().strftime('%d-%m-%Y')

        return today

    # @api.multi
    # def button_send_letter(self):
    #     email_template = "reconciliation_letter.email_account_reconciliation_letter2"
    #     return super(
    #         ResPartner, self.with_context(
    #             email_account_reconciliation_letter2=email_template)).button_send_letter()

    @api.model
    def cron_reconciliation_letter_create(self):
        # print "print"

        for letter in self.env['res.partner'].search([]):
            if letter.reconciliation_letter == True:
                if letter:
                    template_id = self.env['ir.model.data'].get_object_reference(
                        'reconciliation_letter', 'email_account_reconciliation_letter')[1]
                email_template_obj = self.env['mail.template'].browse(template_id)
                if template_id:
                    values = email_template_obj.generate_email(letter.id, fields=None)
                    values['email_from'] = letter.email
                    values['email_to'] = letter.email
                    values['res_id'] = self.id
                    mail_mail_obj = self.env['mail.mail']
                    msg_id = mail_mail_obj.create(values)
                    if msg_id:
                        msg_id.send()

        return True

    @api.multi
    def action_letter_send(self):
        self.ensure_one()
        template = self.env.ref('reconciliation_letter.email_account_reconciliation_letter', False, )
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        ctx = dict(
            default_model='res.partner',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_composition_mode='comment',
        )
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }
