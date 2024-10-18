from odoo import http
from odoo.http import request 
import base64
import json

class EventPhotoController(http.Controller):

    # Ruta para mostrar el formulario de subida de fotos
    @http.route('/subir-foto', type='http', auth='public', website=True)
    def upload_photo(self, **kwargs):
        # Renderiza la plantilla del formulario de subida de fotos
        return request.render('event_photo.upload_photo_template')

    # Ruta para enviar la foto a la base de datos
    @http.route('/submit_photo', type='http', auth='public', methods=['POST'], website=True)
    def submit_photo(self, **kwargs):
        # Obtener de los parametros de la URL los datos del formulario (codigo de evento y foto)
        event_code = kwargs.get('event_code')
        photo = kwargs.get('photo')
        # Buscar el evento en la base de datos usando el codigo del evento
        event = request.env['event.photo'].sudo().search([('event_code', '=', event_code)], limit=1)
        # Validar que el evento exista y este activo
        if not event:
            return json.dumps({'status': 'error', 'message': 'Código de evento inválido'})
        if not event.is_active:
            return json.dumps({'status': 'error', 'message': 'El evento no está activo'})

        # Convertir el archivo (foto) a base64
        photo_base64 = base64.b64encode(photo.read()).decode('utf-8')
        
        # Crea un nuevo registro de foto en la base de datos
        request.env['photo.photo'].sudo().create({
            'image': photo_base64,
            'status': 'in_review',
            'event_id': event.id,
        })

        # Devuelver una respuesta JSON indicando si el envio fue exitoso
        return json.dumps({'status': 'success', 'message': 'Foto enviada correctamente'})

    # Ruta para mostrar las fotos de un evento en la pagina web de la pantalla gigante
    @http.route('/show_photos', type='http', auth='public', website=True)
    def show_photos(self, **kwargs):
        # Obtener el ID del evento
        event_id = kwargs.get('event_id')
        # Buscar el evento en la base de datos usando el codigo del evento
        event = request.env['event.photo'].sudo().search([('event_code', '=', event_id)], limit=1)
        # Validar que el evento exista y este activo
        if not event:
            return "Código de evento inválido"
        if not event.is_active:
            return "El evento no está activo"

        # Buscar en la base de datos las fotos aprobadas del evento
        photos = request.env['photo.photo'].sudo().search([('event_id', '=', event.id), ('status', '=', 'approved')])
        # Decodificar la imagen antes de pasarla a la plantilla
        photos_data = [{'image': photo.image.decode('utf-8')} for photo in photos]
        # Renderizar la plantilla de la pantalla gigante con las fotos del evento
        return request.render('event_photo.show_photos_template', {'photos': photos_data, 'event_id': event_id})

    # Ruta para obtener las fotos aprobadas de un evento
    @http.route('/get_approved_photos', type='http', auth='public', website=True)
    def get_approved_photos(self, **kwargs):
        # Obtener el ID del evento
        event_id = kwargs.get('event_id')
        # Buscar en la base de datos las fotos aprobadas del evento
        event = request.env['event.photo'].sudo().search([('event_code', '=', event_id)], limit=1)
        # Validar que el evento exista. Si no existe, devolver una lista vacia
        if not event:
            return json.dumps([])

        # Buscar en la base de datos las fotos aprobadas del evento
        photos = request.env['photo.photo'].sudo().search([('event_id', '=', event.id), ('status', '=', 'approved')])
        # Decodificar las imagenes antes de devolverlas como JSON
        photos_data = [{'image': photo.image.decode('utf-8')} for photo in photos]
        # Devolver las fotos aprobadas del evento en formato JSON
        return json.dumps(photos_data)