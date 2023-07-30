# -*- coding: utf-8 -*-
{
    "name": "Library Members",
    "license": "AGPL-3",
    "description": "Manage members borrowing books.",
    "application": False,
    "author": "Caleb Mwema",
    "sequence": "-300",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['library', 'mail'],

    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/member_view.xml',
        'views/library_menu.xml',
        "views/book_list_template.xml",

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    #     "demo/library.book.csv",
    #     "demo/library.member.csv"
    # ],
}
