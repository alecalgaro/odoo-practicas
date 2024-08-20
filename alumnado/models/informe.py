from odoo import models, fields, api

class Informe(models.Model):
    _name = 'alumnado.informe'
    _description = 'Informe del alumno'

    nombre = fields.Char(string="Nombre del Informe", required=True)
    fecha_entrega = fields.Date(string="Fecha de Entrega", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('requiere_correccion', 'Requiere Corrección')
    ], string="Estado", default='pendiente')
    comentarios = fields.Text(string="Comentarios")
    alumno_id = fields.Many2one('res.partner', string="Alumno", ondelete='cascade', required=True)