from odoo import models, fields

class HMSLog(models.Model):
    _name = 'hms.log'
    _description = 'HMS Log'

    created_by = fields.Many2one('res.users', string='Created By')
    date = fields.Datetime(string='Date')
    description = fields.Text(string='Description')
    patient_id = fields.Many2one('hms.patient', string='Patient')

    def create(self, vals):
        return super(HMSLog, self).create({
            'created_by': self.env.user.id,
            'date': fields.Datetime.now(),
            'description': vals.get('description'),
            'patient_id': vals.get('patient_id'),
        })