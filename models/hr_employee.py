# -*- coding:utf-8 -*-
#
#
#   2022 Henderson Zambrano  <zambranohender@gmail.com>.
#    
#

from odoo import tools
from odoo import api, fields, models
from odoo.tools.translate import _
from datetime import datetime, date
import math
import time


class Hrempleado(models.Model):
    _inherit = "hr.employee" #clase heredada de rrhh
	
#campos que se declaran dentro de la clase para ser llamadas desde el archivo hr_employee.xml para crear la vista heredada en rrhh


    apellido = fields.Char('Apellidos')
    birthday = fields.Date('Fecha Nacimiento')
    sangre = fields.Char('Tipo de Sangre')
    x_fech_ing = fields.Date('Fecha de Ingreso')
    x_fec_tras = fields.Date('Fecha de Traslado')
    ano_antigue = fields.Integer('Años de Antiguedad')
    edad = fields.Integer('Edad')
    department_id = fields.Many2one('hr.department', 'Ubicación Administrativa')
    job_id = fields.Many2one('hr.job', 'Cargo')
    parent_id = fields.Many2one('hr.employee', string='Jefe Inmediato')
    coach_id = fields.Many2one('hr.employee', 'Jefe Inmediato')
    enfermedad = fields.Text('Padece Alguna Enfermedad.?', size=240)
    department_asig = fields.Many2one('hr.department', 'Unidad Asignada')
    mopersonal = fields.One2many('hr.mopersonal', 'employee_id', 'Movimiento de Personal')
    direccion = fields.Text('Direccion de Habitación', size=240)
    phone = fields.Char('Telefono Celular')
    casa = fields.Char('Nº Casa/Apartamento')
  
  	
# funcion que calcula la edad en años del empleado en base
# a la fecha de nacimiento
    @api.onchange('birthday', 'edad')
    def on_change_birthday(self):
        today = date.today()
        if self.birthday:
           self.edad = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day)) 
           
# funcion que calcula la antiguedad en años del empleado en base
# a la fecha del ingreso
    @api.onchange('x_fech_ing', 'ano_antigue')
    def on_change_fech_ing(self):
        today = date.today()
        if self.x_fech_ing:
           self.ano_antigue = today.year - self.x_fech_ing.year - ((today.month, today.day) < (self.x_fech_ing.month, self.x_fech_ing.day)) 
         

 
# clase para registrar los cambios de departamento del empleado
class hr_Mopersonal(models.Model):
    _name = "hr.mopersonal"
    _description = 'Movimiento de Personal'


# funcion para obtener la fecha actual por defecto en el campo -> fech_tras

    def _default_fecha(self):
        return datetime.now()	
	
    name = fields.Char('Descripción', required=True)
    employee_id = fields.Many2one('hr.employee', string="Empleado", readonly=True)
    fech_tras = fields.Date('Fecha de Traslado', default=_default_fecha)
    department = fields.Many2one('hr.department', 'Unidad Asignada')
    cargo = fields.Many2one('hr.job', 'Nuevo Cargo')

    

