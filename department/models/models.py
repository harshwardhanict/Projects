# -*- coding: utf-8 -*-

from odoo import models, fields, api


class department(models.Model):
    _name = 'department_department'
    _description = 'department_department'

    name = fields.Char(string='NAME')
    marks = fields.Integer()
    fee_id = fields.Char()
    user_id = fields.Many2many('res.partner.category', string='Users')
    description = fields.Text()
    value = fields.Integer(string="Value")
    print_value = fields.Integer(string="Print Value")

    @api.onchange('value')
    def _vue_pc(self):
        for record in self:
            if record.value:
                record.print_value = record.value



    def website(self):
        # print("button is click")
        return {
            'name': 'smart button',
            'domain': [],
            'view_type': 'form',
            'res_model': 'station.station',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }

    def Add(self):
        return self.env['ir.actions.act_window']._for_xml_id("department.department_wiz_action_window")



    # def write(self, vals):
    #     vals.update({
    #         'name': 'Harsh'
    #     })
    #     res = super().write(vals)
    #     return res
    #
    # def unlink(self):
    #     print("unlin", self)
    #     res = super().unlink()
    #     print("kkkk---res", res)
    #     return res


