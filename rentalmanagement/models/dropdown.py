from odoo import models, fields, api


class name_ref(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        res = []
        if self._context.get('name_phone'):
            for rec in self:
                if rec.phone:
                    res.append((rec.id, f"{rec.name} - {rec.phone}"))
                else:
                    res.append((rec.id, f"{rec.name}"))
            return res
        return super(name_ref, self).name_get()







