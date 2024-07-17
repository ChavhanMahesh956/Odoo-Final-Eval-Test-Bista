from odoo import models, fields

class Enrollment(models.Model):
    _name = 'enrollment.form'
    _description = 'Enrollment Form'

    name = fields.Char(string='Full Name', required=True)
    dob = fields.Date(string='Date of Birth', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True)
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email', required=True)

    college_name = fields.Char(string='College Name', required=True)
    course_name = fields.Char(string='Course Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    additional_comment = fields.Text(string='Comment')

    supervisor_group = fields.Many2many(
        comodel_name='res.groups',
        string='Supervisor Groups',
        help='Select groups whose members can view all enrollment records.')



    def create_partner_and_portal_user(self):
        Partner = self.env['res.partner']
        User = self.env['res.users']

        partner_vals = {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'street': self.address,
        }
        partner = Partner.create(partner_vals)

        user_vals = {
            'name': self.name,
            'login': self.email,
            'partner_id': partner.id,
            'email': self.email,
            'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],
        }
        user = User.create(user_vals)

        return partner, user
