# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Turkish Invoice Customization',
    'summary': 'View the amount in word in the invoice.',
    'author': 'TruncServis',
    'version': '10.0.1.0',
    'license': 'AGPL-3',
    'website': 'http://truncservis.com',
    'category': 'Localization',
    'depends': ['account'],
    'data': [
        'views/amount_word_view.xml',
    ],

    'application': False,
    'auto_install': False,
    'installable': True,
}
