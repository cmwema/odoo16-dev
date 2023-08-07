# -*- coding: utf-8 -*-
{
    'name': "agriculturevc",
    'author': "Caleb Mwema",
    'website': "https://brw-automation.odoo.com/",

    'category': 'Manufacturing',
    'version': '0.1',
    'sequence': -400,
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/venue_view.xml',
        'views/assets_views.xml',
        'views/main.xml',
    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
