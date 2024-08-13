from odoo import models, fields, api

class ModuloVivienda(models.Model):
    _name = 'vsm.modulo_vivienda'
    _description = 'Modulo en Vivienda'

    vivienda_id = fields.Many2one('vsm.vivienda', string='Vivienda', required=True)
    modulo_id = fields.Many2one('vsm.modulo', string='Modulo', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)
    costo_total = fields.Float(string='Costo', compute="_compute_costo_total", required=True)

    @api.depends('modulo_id.costo_total', 'cantidad')
    def _compute_costo_total(self):
        for record in self:
            record.costo_total = record.modulo_id.costo_total * record.cantidad