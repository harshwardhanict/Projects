# -*- coding: utf-8 -*-

from odoo import models, fields, api


class department_wizard(models.Model):
    _name = 'department_wiz'
    _description = 'department_wiz'

    name = fields.Char(string='Name')
    fee_id = fields.Char(string='Fee')
    user_id = fields.Many2many('res.partner.category', string='Users')

    @api.model
    def Create_H(self, vals):
        res = self.env['department_department'].create(vals)
        return res

