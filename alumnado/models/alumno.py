from odoo import models, fields, api
from datetime import datetime

class Alumno(models.Model):
    _inherit = 'res.partner'

    is_alumno = fields.Boolean(string="Es Alumno")

    matricula = fields.Char(string="Número de Matrícula")
    nombre_proyecto = fields.Text(string="Nombre de Proyecto")
    email = fields.Char(string="Email")
    anio_cursado = fields.Integer(string="Año de Cursado", default=lambda self: datetime.now().year)
    informes_entregados = fields.One2many('alumnado.informe', 'alumno_id', string="Informes Entregados")