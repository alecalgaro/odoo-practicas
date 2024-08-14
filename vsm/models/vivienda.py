from odoo import models, fields, api
import base64

class Vivienda(models.Model):
    _name = 'vsm.vivienda'
    _description = 'Vivienda'

    id_cliente = fields.Many2one('vsm.cliente', string='Cliente', required=True)
    orientacion = fields.Selection([
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
        ('noreste', 'Noreste'),
        ('noroeste', 'Noroeste'),
        ('sureste', 'Sureste'),
        ('suroeste', 'Suroeste')], string='Orientación', required=True, default='norte')
    largo_terreno = fields.Float(string='Largo del terreno', required=True) 
    ancho_terreno = fields.Float(string='Ancho del terreno', required=True)
    cubierta = fields.Selection([
        ('un_agua', 'Un agua'),
        ('dos_aguas', 'Dos aguas'),
        ('plana', 'Plana')], string='Cubierta', required=True, default='un_agua')
    piso = fields.Selection([
        ('platea', 'Sobre platea'),
        ('pilotes', 'Sobre pilotes')], string='Piso', required=True, default='platea')
    terminacion = fields.Selection([
        ('placa', 'Placa cementicia'),
        ('madera', 'Tablas madera')], string='Terminación', required=True, default='madera')  
    modulos_vivienda_ids = fields.One2many('vsm.modulo_vivienda', 'vivienda_id', string='Módulos en Vivienda')
    costo_total_vivienda = fields.Float(string='Costo Total', compute='_compute_costo_total_vivienda', store=True)

    @api.depends('modulos_vivienda_ids.costo_total')
    def _compute_costo_total_vivienda(self):
        for record in self:
            record.costo_total_vivienda = sum(modulo.costo_total for modulo in record.modulos_vivienda_ids)

    def export_to_txt(self):
        """
        Metodo para exportar la informacion de la vivienda a un archivo TXT.
        """
        for record in self:
            content = f"{record.orientacion}\n"
            content += f"{record.largo_terreno}\n"
            content += f"{record.ancho_terreno}\n"
            content += f"{record.cubierta}\n"
            content += f"{record.piso}\n"
            content += f"{record.terminacion}\n"
            for modulo in record.modulos_vivienda_ids:
                content += f"{modulo.modulo_id.id_bloque}\n"
                content += f"{modulo.cantidad}\n"

            # Crear el archivo TXT
            file_name = f"vivienda_{record.id}.txt"
            attachment = self.env['ir.attachment'].create({
                'name': file_name,
                'type': 'binary',
                'datas': base64.b64encode(content.encode('utf-8')),
                'res_model': self._name,
                'res_id': record.id,
                'mimetype': 'text/plain'
            })

            return {
                'type': 'ir.actions.act_url',
                'url': f'/web/content/{attachment.id}?download=true',
                'target': 'self',
            }
    
    def action_print_report(self):
        """
        Metodo para generar un reporte en PDF con la informacion de la vivienda.
        """
        return self.env.ref('vsm.action_report_vivienda').report_action(self)