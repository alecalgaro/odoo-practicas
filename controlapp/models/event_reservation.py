from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class EventReservation(models.Model):
    _name = 'controlapp.event.reservation'
    _description = 'Reserva para un evento'

    name = fields.Char(string='Nombre cliente', required=True)
    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    start_datetime = fields.Datetime(string='Fecha y hora de inicio', required=True)
    end_datetime = fields.Datetime(string='Fecha y hora de finalización', required=True)
    description = fields.Text(string='Descripción')

    #* Validaciones
    # Con @api.contrains se definen restricciones sobre los campos indicados. 
    # La funcion decorada se ejecuta cada vez que se crea o actualiza un registro que contenga esos campos.

    # Validar que las fechas elegidas no sean anteriores a la fecha actual.
    @api.constrains('start_datetime', 'end_datetime')
    def _check_dates(self):
        for record in self:
            if record.start_datetime < datetime.now():
                raise ValidationError("La fecha y hora de inicio no puede ser anterior a la fecha y hora actual.")
            if record.end_datetime < record.start_datetime:
                raise ValidationError("La fecha y hora de finalización no puede ser anterior a la fecha y hora de inicio.")

    # Validar que no existan eventos registrados en el mismo dia y horario (solapamiento de reservas).
    # Asegura que no se puedan guardar o actualizar reservas que se solapen con otras reservas ya existentes. 
    @api.constrains('start_datetime', 'end_datetime')
    def _check_overlap(self):
        # Recorrer cada reservar y verificar si existe alguna reserva que se solape
        for record in self:
            # self.env[...] se accede al modelo y con search se busca en la BD los registros
            # que cumplan con las condiciones especificadas en la lista:
            # - que el id no sea el mismo que el del registro actual
            # - que la fechay hora  de inicio de otro evento sea anterior a la feche y hora de finalizacion del evento actual
            # - que la fecha y hora de finalizacion de otro evento sea posterior a la fecha y hora de inicio del evento actual.
            # Si todas se cumplen, significa que ya hay un evento registrado dentro del rango en el que se quiere
            # registrar un nuevo evento (hay un solapamiento), por lo cual se lanza una excepcion con un mensaje de error. 
            overlapping_reservations = self.env['controlapp.event.reservation'].search([
                ('id', '!=', record.id),    
                ('start_datetime', '<', record.end_datetime),   
                ('end_datetime', '>', record.start_datetime)
            ])
            if overlapping_reservations:    # si overlapping_reservations contiene algun registro (hay solapamiento)
                raise ValidationError("Ya existe un evento registrado en el día y horario elegido.")
    
    # Para generar un reporte en PDF con la información de la reserva
    def action_print_report(self):
        return self.env.ref('controlapp.action_report_event_reservation').report_action(self)