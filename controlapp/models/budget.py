from odoo import models, fields, api

class Budget(models.Model):
    _name = 'controlapp.budget'
    _description = 'Presupuesto'

    name = fields.Char(string='Nombre del presupuesto', required=True)
    initial_amount = fields.Float(string='Presupuesto inicial', required=True)
    current_amount = fields.Float(string='Presupuesto actual', compute='_compute_current_amount', store=True)
    move_ids = fields.One2many('controlapp.move', 'budget_id', string='Movimientos')
    # Tipo de moneda o divisa (definida por defecto en ARS para pesos argentinos)
    currency_id = fields.Many2one('res.currency', string='Tipo de moneda', default=lambda self: self.env.ref('base.ARS').id)

    @api.depends('move_ids.amount', 'move_ids.type')
    def _compute_current_amount(self):
        """
        Metodo para calcular el presupuesto actual.
        """
        for budget in self:
            total = budget.initial_amount
            for move in budget.move_ids:
                if move.type == 'income':
                    total += move.amount
                else:
                    total -= move.amount
            budget.current_amount = total