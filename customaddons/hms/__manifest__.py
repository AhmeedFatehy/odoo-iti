{
    'name': 'Health Management System',
    'version': '1.0',
    'author': 'Ahmed fathi',
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/department_views.xml',
        'views/log_views.xml',
        'views/related_patient.xml',
    ],
    'installable': True,
    'application': True,
    'depends': ['base', 'contacts'],
    'license': 'LGPL-3',
    'sequence': 1,
}