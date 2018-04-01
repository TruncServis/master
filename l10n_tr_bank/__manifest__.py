# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Turkey Banking',
    'summary': 'Bank',
    'author': 'TruncServis',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'website': 'http://truncservis.com',
    'category': 'Base',
    'depends': ['base'],
    'data': [
        'data/res.bank.csv',
        'views/res_bank_view.xml',
        # 'security/',
    ],
    'demo': [],
    'test': [],
    'application': False,
    'auto_install': False,
    'installable': True
}
