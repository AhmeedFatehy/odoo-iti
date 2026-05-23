from odoo import models, fields, api
from datetime import date


class HMSDepartment(models.Model):
    _name = 'hms.department'
    _description = 'HMS Department'

    name = fields.Char(string='Name', required=True)
    capacity = fields.Integer(string='Capacity')
    is_opened = fields.Boolean(string='Is Opened')
    patient_ids = fields.One2many('hms.patient', 'department_id', string='Patients')