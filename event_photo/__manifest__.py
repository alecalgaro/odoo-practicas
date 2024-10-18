{
    'name': 'Event Photo',
    'version': '1.0',
    'summary': 'Modulo para compartir fotos en eventos.',
    'description': 'Modulo que permite compartir fotos en pantalla gigante de un evento escaneando un código QR.',
    'author': 'Alejandro Calgaro',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/upload_photo_template.xml',
        'views/event_views.xml',
        'views/photo_views.xml',
        'views/photo_moderation_views.xml',
        'views/show_photos_template.xml',
        'views/qr_generator_views.xml',
    ],
    'application': True,
}