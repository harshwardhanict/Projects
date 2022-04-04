from odoo import models, fields, api


class station_wizard(models.TransientModel):
    _name = 'station_wiz'
    _description = 'station_wiz'

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    ticket_no = fields.Char(string="Ticket No")



