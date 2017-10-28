# -*- coding: utf-8 -*-
{
    'name': "Customer Management",

    'summary': """Customer Management, Tasks, Assign Task""",

    'description': """Customer, Management, Tasks, Assign Task """,

    'author': "Abdul Halim",
    'website': "http://aristobd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cm_menu.xml',
        'views/cm_task_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
