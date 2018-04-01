# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Turkish Parner Customization',
    'summary': 'Parner tax office',
    'author': 'TruncServis',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'website': 'http://trunccervis.com',
    'category': 'Base',
    'depends': ['base','base_vat'],
    'data': [
		'security/ir.model.access.csv',
        'data/res.country.state.csv',
        'data/tax.offices.csv',
        'views/partner_view.xml',
		'views/tax_office_view.xml',
        #
    ],
    'demo': [],
    'test': [],
    'application': False,
    'installable': True,
    'auto_install': False,
}
