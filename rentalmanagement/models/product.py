from odoo import models, fields, api


class product_product(models.Model):
    _inherit = 'product.template'


    is_rental = fields.Boolean(string="Is Rental")
    Type = fields.Many2one('rentaltype.rentaltype', string="Rental Type")
