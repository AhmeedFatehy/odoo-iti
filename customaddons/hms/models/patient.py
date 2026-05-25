import re

from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError
class HMSPatient(models.Model):
    _name = 'hms.patient'
    _description = 'HMS Patient'
    _rec_name = 'first_name'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)

    birth_date = fields.Date(string='Birth Date')

    history = fields.Html(string='History')

    cr_ratio = fields.Float(string='CR Ratio')

    blood_type = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string='Blood Type')

    pcr = fields.Boolean(string='PCR')

    image = fields.Image(string='Patient Image')

    address = fields.Text(string='Address')

    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True
    )

    department_id = fields.Many2one('hms.department', string='Department', domain="[('is_opened', '=', True)]")
    department_capacity = fields.Integer(string='Department Capacity', related='department_id.capacity')
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors')

    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string='State', default='undetermined')

    logs = fields.One2many('hms.log', 'patient_id', string='Logs')

    email = fields.Char(string='Email')

    _email_unique = models.Constraint(
        'UNIQUE(email)', 
        'The email must be unique.'
    )
    
    @api.constrains('email')
    def _check_email(self):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        for rec in self:
            if rec.email:
                if not re.match(email_pattern, rec.email):
                    raise ValidationError("Please enter a valid email address.")

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = date.today().year - record.birth_date.year
            else:
                record.age = 0

    def write(self, vals):
        res = super(HMSPatient, self).write(vals)
        if 'state' in vals:
            self.env['hms.log'].create({
                'description': f"State changed to {vals['state']} for patient {self.first_name} {self.last_name}",
                'patient_id': self.id,
            })
        return res
    
    @api.onchange('age')
    def _onchange_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'PCR has been automatically checked because age is lower than 30.'
                }
            }