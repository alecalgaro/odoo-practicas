from odoo import models, fields, api

class Photo(models.Model):
    _name = 'photo.photo'
    _description = 'Photo'

    image = fields.Binary(string='Foto', required=True)
    status = fields.Selection([('in_review', 'En revisión'), ('approved', 'Aprobada'), ('rejected', 'Rechazada')], default='in_review', string='Estado')
    event_id = fields.Many2one('event.photo', string='Evento', required=True)

    def action_approve(self):
        for record in self:
            record.status = 'approved'

    def action_reject(self):
        for record in self:
            record.status = 'rejected'