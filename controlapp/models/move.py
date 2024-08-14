from odoo import models, fields, api

class BudgetMove(models.Model):
    _name = 'controlapp.move'
    _description = 'Gestión ingresos y gastos para el control de presupuesto'

    amount = fields.Float(string='Cantidad', required=True)
    date = fields.Date(string='Fecha', required=True)
    description = fields.Text(string='Descripción')
    type = fields.Selection([('income', 'Ingreso'), ('expense', 'Gasto')], string='Tipo', required=True)
    budget_id = fields.Many2one('controlapp.budget', string='Presupuesto', required=True)
    # Tipo de moneda o divisa (definida por defecto en ARS para pesos argentinos)
    currency_id = fields.Many2one('res.currency', string='Tipo de moneda', default=lambda self: self.env.ref('base.ARS').id)