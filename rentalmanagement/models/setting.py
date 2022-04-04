from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    click = fields.Boolean(string="Click")
    html = fields.Html(string="Html")
    track = fields.Many2one("res.company", string="Track", required=False)

    @api.model
    @api.onchange('click')
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['click'] = self.env['ir.config_parameter'].get_param(
            'rental_management.click')
        if res['click']:
            res['html'] = self.env['ir.config_parameter'].get_param('rental_management.html')
            track = self.env['ir.config_parameter'].get_param(
                'rental_management.track'
            )
            res.update(
                track=int(track)
            )
        else:
            self.html = None
            self.track = False
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            'rental_management.click', self.click)
        self.env['ir.config_parameter'].set_param(
            'rental_management.track', self.track.id)
        super(ResConfigSettings, self).set_values()


