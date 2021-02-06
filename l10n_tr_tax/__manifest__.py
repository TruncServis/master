# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Turkish Tax Customization',
    'summary': 'Tevkifatlı KDV',
    'author': 'TruncServis',
    'version': '13.0.1.0',
    'license': 'AGPL-3',
    'website': 'http://truncservis.com',
    'category': 'Localization',
    'depends': ['account',
                # 'base_vat',
                'l10n_tr',
                # 'account_tax_python'
                ],
    'data': [
        # 'data/account_tax_tevkifat.xml',
        'data/account_tax_tevkifat_satis.xml',
        'data/account_tax_tevkifat_satinalma.xml',
        # 'data/satinalama.xml',
        'views/account_tax.xml',
    ],

    'application': False,
    'auto_install': False,
    'installable': True,
}
