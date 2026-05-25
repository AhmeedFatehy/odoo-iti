from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(
        'hms.patient',
        string='Related Patient'
    )
    #vat = fields.Char(required=True)


    @api.constrains('email')
    def _check_patient_email(self):
        for rec in self:
            if rec.email:
                patient = self.env['hms.patient'].search([
                    ('email', '=', rec.email)
                ], limit=1)

                if patient and patient != rec.related_patient_id:
                    raise ValidationError(
                        "This email already exists in Patients."
                    )
                
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError(
                    "You cannot delete a contact linked to a patient."
                )
            else:
                return super(ResPartner, self).unlink()