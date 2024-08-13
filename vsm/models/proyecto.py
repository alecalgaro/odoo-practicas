from odoo import models, fields, api

class Proyecto(models.Model):
    _name = 'vsm.proyecto'
    _description = 'Proyecto de construcción de vivienda.'

    cliente_id = fields.Many2one('vsm.cliente', string='Cliente', required=True)
    vivienda_id = fields.Many2one('vsm.vivienda', string='Vivienda', required=True)
    etapa = fields.Selection([
        ('planificacion', 'Planificación'),
        ('construccion', 'Construcción'),
        ('finalizado', 'Finalizado')], string='Etapa', required=True, default='planificacion')