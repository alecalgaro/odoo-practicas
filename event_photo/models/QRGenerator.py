from odoo import models, fields, api
import qrcode
import base64
from io import BytesIO

class QRGenerator(models.Model):
    _name = 'qr.generator'
    _description = 'QR Generator'

    qr_code = fields.Binary(string='QR', readonly=True)
    url = fields.Char(string='URL', required=True, default='/subir-foto')

    def generate_qr_code(self):
        """
        Metodo para generar un codigo QR a partir de la URL almacenada en el campo 'url'.
        Se recorre cada registro (qr.generator), se genera el codigo QR y se guarda
        la imagen en el campo 'qr_code'.
        """
        for record in self:
            qr = qrcode.QRCode( 
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(record.url)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_code_image = base64.b64encode(buffer.getvalue())
            record.qr_code = qr_code_image