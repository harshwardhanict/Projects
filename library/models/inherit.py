from odoo import models, fields, api
from odoo.exceptions import UserError


class product_product(models.Model):
    _inherit = 'account.move'

    email_1 = fields.Many2one("account.move",string="Email")
    # mobile = fields.Char(string="Phone No")

    def name_get(self):
      result = []
      for rec in self:
        result.append((rec.id, f"{rec.partner_id.email} - {rec.partner_id.phone}"))
      return result


    # def action_confirm(self):
    #     for rec in self:
    #         if len(rec.invoice_line_ids) > 2:
    #             raise UserError("Create again")

    # @api.onchange('partner_id')
    # def _onchange_partner_id(self):
    #     for rec in self:
    #         rec.mobile = rec.partner_id.phone