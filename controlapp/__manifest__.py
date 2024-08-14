{
    'name': "ControlApp",
    'description': "Gestión de ingresos, gastos y reserva de fechas en salón de eventos.",
    'author': "Alejandro Calgaro",
    'website': "https://www.alecalgaro.com.ar",
    'version': '1.0',
    'depends': ['base'],
    "data": [
        "security/ir.model.access.csv",
        "views/budget_views.xml",
        "views/move_views.xml",
        "views/event_reservation_views.xml",
        "views/event_reservation_template.xml",
        "views/event_reservation_report.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'controlapp/static/css/custom_styles.css',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'icon': '/controlapp/static/icon_app.png',
}