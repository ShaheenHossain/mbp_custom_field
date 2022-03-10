# -*- coding: utf-8 -*-
{
    'name': "MBP field in invoice",

    'summary': """
for invoice extra field""",

    'description': """
        invoice extra field invoice module's purpose
    """,

    'author': "Md. Shaheen Hossain",
    'website': "http://www.eagle-erp.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'report/mbp_part_no_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
