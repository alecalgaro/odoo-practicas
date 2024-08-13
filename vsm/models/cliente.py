from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'vsm.cliente'
    _description = 'Cliente'

    name = fields.Char(string='Nombre', required=True)
    dni = fields.Char(string='DNI', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Teléfono')
    address = fields.Char(string='Dirección')