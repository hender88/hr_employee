# -*- coding:utf-8 -*-
#
#
#  2022 Henderson Zambrano <zambranohender@gmail.com>.
#    
{
   'name': 'Empleado',

    'description': """
        Modulo que registra traslados entre departmentos del empledo,
        tambien agrega nuevos campos a la vista formulario
    """,
    'author': 'Henderson Zambrano <zambranohender@gmail.com>',
    'website': 'https://www.odoo.com',

    # Categories can be used to filter modules in modules listing

    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee.xml',
    ],
    'installable': True,
   
}
