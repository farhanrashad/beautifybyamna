# -*- coding: utf-8 -*-
{
    'name': "Link Ecommerce Categories",

    'summary': """
        Ecommerce Category and Products Integration""",

    'description': """
        This module will link ecommerce category to products and also adds auto car fields. 
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website', 'website_sale_delivery'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/product_template_ext.xml',
        'views/product_public_category_ext.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}