{
    'name': 'Health Management System',
    'version': '1.0',
    'author': 'Ahmed fathi',
    'depends': ['base', 'contacts'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/patient_report.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/department_views.xml',
        'views/log_views.xml',
        'views/related_patient.xml',
    ],
    'installable': True,
    'application': True,
}