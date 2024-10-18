from odoo import models, fields, api

class Event(models.Model):
    _name = 'event.photo'
    _description = 'Evento'

    name = fields.Char(string='Nombre del evento', required=True)
    start_datetime = fields.Datetime(string='Fecha y hora de inicio', required=True)
    end_datetime = fields.Datetime(string='Fecha y hora de finalización', required=True)
    description = fields.Text(string='Descripción')
    event_code = fields.Char(string='Código', required=True)
    is_active = fields.Boolean(string='Esta activo', default=True)
    show_photos_url = fields.Char(string='Pantalla gigante', compute='_compute_show_photos_url')

    @api.depends('event_code')
    def _compute_show_photos_url(self):
        """
        Metodo para calcular la URL de la pantalla gigante. 
        Se obtiene la URL base del sistema y se concatena con el codigo del evento, luego de 
        recorrer cada registro (evento).
        """
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.show_photos_url = f"{base_url}/show_photos?event_id={record.event_code}"

    def open_show_photos(self):
        """
        Metodo para abrir la pantalla gigante en una nueva pestaña del navegador
        al hacer click en un boton en la vista de lista de eventos.
        """
        self.ensure_one()   # para asegurarse que se este trabajando con un solo registro (evento)
        # Devuelver una accion de tipo URL que redirige a la URL de la pantalla gigante (show_photos_url) en una nueva pestaña (new)
        return {
            'type': 'ir.actions.act_url',
            'url': self.show_photos_url,
            'target': 'new',
        }