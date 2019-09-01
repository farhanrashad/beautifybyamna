{
    'name': 'Balance field in Invoice form',
    'images': ['images/main_screenshot.png'],
    'version': '1.0.1',
    'category': 'Partner',
    'summary': 'Add Balance field to main Invoice form',
    'author': 'Dynexcel',
    'website': 'http://www.dynexcel.com',
    'depends': [
	'account',
    ],
    'installable': True,
    'license': 'AGPL-3',
    'data': [
        'views/partner_balance_views.xml',
    ],
}
