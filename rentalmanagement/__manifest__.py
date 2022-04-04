# -*- coding: utf-8 -*-
{
    'name': "rentalmanagement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'rentaltype', 'mail', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/task_views.xml',
        'views/sales_id.xml',
        'views/setting.xml',
        'rental_type/rentaltype.xml',
        'views/dropdown.xml',
        'views/product.xml',
        'views/templates.xml',
        'data/category_data.xml',
        'report/paperform.xml',
        'report/card.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "license": "LGPL-3",
    "application": True
}
