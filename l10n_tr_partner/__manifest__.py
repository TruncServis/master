# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Turkish Parner Customization',
    'summary': 'Turkey states/city and partner tax offices',
    'author': 'TruncServis',
    'version': '13.0.1.0',
    'license': 'AGPL-3',
    'website': 'http://trunccervis.com',
    'category': 'Base',
    'depends': ['contacts',
                #'base_vat'
                ],
    'data': [
        'security/ir.model.access.csv',
        'data/tax.offices.csv',
        # 'data/res_country_state.xml',
        'views/company_views.xml',
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
