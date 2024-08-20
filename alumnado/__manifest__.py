{
    'name': "Gestión de alumnos",
    'description': "Gestión de alumnos y sus entregas de informes.",
    'author': "Alejandro Calgaro",
    'website': "https://www.alecalgaro.com.ar",
    'version': '1.0',
    'depends': ['base'],
    "data": [
        "security/ir.model.access.csv",
        "views/alumno.xml",
        "views/informe.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}