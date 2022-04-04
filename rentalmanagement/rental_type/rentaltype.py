from odoo import models, fields, api


class Rental_Type(models.Model):
    _name = 'rental_type'
    _description = 'rental_type'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")