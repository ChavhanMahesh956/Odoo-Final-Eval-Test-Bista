from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    weight = fields.Text(string='Weight')
