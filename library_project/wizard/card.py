from odoo import models, fields, api


class card_membership(models.Model):
    _name = 'card.membership'
    _description ='This a membership details'

    p_name = fields.Char(string="Name")
    p_id = fields.Integer(string="Membership Id")
    p_period = fields.Char(string="Membership Period")
