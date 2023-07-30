# -*- coding: utf-8 -*-
{
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    "application": True,
    'installable': True,
    'application': True,
    'auto_install': False,

    'author': "Caleb Mwema",
    'sequence': -100,
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',

        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
    'demo': [],

}
