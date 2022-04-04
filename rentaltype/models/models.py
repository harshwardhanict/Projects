# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rentaltype(models.Model):
    _name = 'rentaltype.rentaltype'
    _description = 'rentaltype.rentaltype'

    name = fields.Char()
    Code = fields.Char()
    description = fields.Char()

