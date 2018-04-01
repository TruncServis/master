# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Turkish Account Customization',
    'summary': 'Reconciliation letter, partners credit debit sum, tax',
    'author': 'TruncServis',
    'version': '10.0.1.0',
    'license': 'AGPL-3',
    'website': 'http://truncservis.com',
    'category': 'Localization',
    'depends': ['account', 'base_vat', 'l10n_tr', 'account_tax_python'],
    'data': [
        'views/reconciliation_letter_views.xml',
        'views/account_tax_tevkifat.xml',
        'views/partners_credit_debit_sum.xml',
        'data/reconciliation_letter_data.xml',
        'data/reconciliation_letter_cron.xml',
    ],

    'application': False,
    'auto_install': False,
    'installable': True,
}
