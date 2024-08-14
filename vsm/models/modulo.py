from odoo import models, fields, api

class Modulo(models.Model):
    _name = 'vsm.modulo'
    _description = 'Modulo'

    id_bloque = fields.Char(string='Bloque', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    costo_materiales = fields.Float(string='Costo de materiales', required=True)
    costos_extras = fields.Float(string='Costos extras', required=True)
    costo_total = fields.Float(string='Costo total', compute="_compute_costo_total", required=True)
    informacion_adicional = fields.Text(string='Información adicional')
    imagen = fields.Binary(string='Imagen')
    modulos_vivienda_ids = fields.One2many('vsm.modulo_vivienda', 'modulo_id', string='Viviendas con Módulo')

    @api.depends('costo_materiales', 'costos_extras')
    def _compute_costo_total(self):
        for modulo in self:
            modulo.costo_total = modulo.costo_materiales + modulo.costos_extras

    def _compute_display_name(self):
        """
        Metodo para calcular el nombre a mostrar del modulo.
        Odoo ejecuta automaticamente el metodo _compute_display_name.
        """
        for modulo in self:
            modulo.display_name = modulo.nombre