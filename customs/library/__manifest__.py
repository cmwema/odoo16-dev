# -*- coding: utf-8 -*-
{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Caleb Mwema",
    "application": True,
    'version': '0.1',

    'depends': ['base'],

    'data': [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        'views/library_menu.xml',
        'views/book_view.xml',
        "views/book_list_template.xml"
    ],
    "sequence": "-100",
    "category": "Services/Library",
    "license": "LGPL-3"
}
