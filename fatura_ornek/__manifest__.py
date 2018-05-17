# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Turkish Invoice Customization',
    'summary': 'Fatura Sample',
    'author': 'TruncServis',
    'version': '10.0.1.0',
    'license': 'AGPL-3',
    'website': 'http://truncservis.com',
    'category': 'account',
    'depends': ['account'],
    'data': [
        'data/paperformat.xml',
        'views/report_menu.xml',
        'template/fatura_a5.xml',
        # 'views/invoice_test.xml',
    ],

    'application': False,
    'auto_install': False,
    'installable': True,
}
