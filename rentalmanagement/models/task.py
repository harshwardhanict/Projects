from unittest import result

from odoo import models, fields, api


class task_wizard(models.TransientModel):
    _name = 'task_wiz'
    _description = 'task_wiz'

    customer = fields.Many2one('res.partner', string="Customer")
    customer_email = fields.Char(string="Email")
    sales_person = fields.Char(string="Sales Person")
    sales_person_contact = fields.Char(string="Sales Person Contact")
    payment_terms = fields.Char(string="Payment Terms")


    @api.model
    def default_get(self, fields):
        res = super(task_wizard, self).default_get(fields)
        cust = self.env['sale.order'].browse([self.env.context.get('active_id')])
        res['customer'] = cust.partner_id.id
        res['customer_email'] = cust.partner_id.email
        res['sales_person'] = cust.user_id.name
        res['sales_person_contact'] = cust.user_id.phone
        res['payment_terms'] = cust.payment_term_id.name
        return res
