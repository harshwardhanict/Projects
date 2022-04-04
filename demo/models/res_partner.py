from odoo import models, fields, api


class ResPartnerserver(models.Model):
    _inherit = 'res.partner'

    def comp(self):
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

    def record_cree(self):
        context = self._context
        self.env[context["active_model"]].create({"name": "hax"})

    def over_wirte(self):
        self.update({
            'name': 'HaxCreation',
            'email': 'jjackmony@gmail.com',
            'mobile': '56446564'
        })

    # @api.onchange('name', 'mobile', 'email')
    # def _on_partner_id(self):
    #     for rec in self:
    #         rec.name = 'Harshwardhan Waghela'
    #         rec.email = 'hvwaghela51@gmail.com'
    #         rec.mobile = '746686774'
