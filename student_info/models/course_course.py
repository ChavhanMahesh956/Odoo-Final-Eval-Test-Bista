from odoo import models,fields,api

class Course(models.Model):
    _name='course.course'
    _description = 'The Course Data'

    name = fields.Char(string="Course Name",required=True )