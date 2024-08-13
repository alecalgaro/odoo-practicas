# -*- coding: utf-8 -*-
{
    'name': "VSM",
    'description': "Gestión de clientes y viviendas sociales en madera",
    'author': "Alejandro Calgaro",
    'website': "https://www.alecalgaro.com.ar",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cliente_view.xml',
        'views/vivienda_view.xml',
        'views/modulo_view.xml',
        'views/vivienda_report_template.xml',
        'views/report_vivienda.xml',
        'views/proyecto_view.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'icon': '/vsm/static/icon_vsm.png',
}

