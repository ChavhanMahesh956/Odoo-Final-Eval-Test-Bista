from odoo import models,fields,api

class College(models.Model):
    _name='college.college'
    _description = 'The College Data'

    name = fields.Char(string="College Name",required=True )