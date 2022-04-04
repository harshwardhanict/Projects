# -*- coding: utf-8 -*-

from odoo import models, fields, api


class library(models.Model):
    _name = 'library.library'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'library.library'

    name = fields.Char(string='Name', tracking=True)
    value = fields.Integer(string='Value', tracking=True)
    image = fields.Binary(string='Image')
    date = fields.Datetime('Date', default=lambda x: fields.datetime.now())

    books = fields.One2many('library.book', 'library_books', string='Books')
    address = fields.One2many('library.address', 'library_address', string='Address')
    payment = fields.One2many('library.payment', 'library_payment', string='Payment')
    stat = fields.Selection([('application', 'Application'), ('confirm', 'Confirm')], string='Status', index=True)
    star = fields.Selection(
        [('0', 'Bad'), ('1', 'Average'), ('2', 'Good'), ('3', 'Excellent'), ('4', 'Insane'), ('5', 'Master')])
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], string='Gender')


class librarybooks(models.Model):
    _name = 'library.book'
    _description = 'library.book'
    library_books = fields.Many2one('library.library')
    books_name = fields.Char(string="Books Name")
    quantity = fields.Char(string="Quantity")
    Mrp = fields.Float(string="Mrp")
    add = fields.Many2one('library.library', string="Adding")


class librarybooks_address(models.Model):
    _name = 'library.address'
    _description = 'library.address'
    library_address = fields.Many2one('library.library')
    Address = fields.Char(string="Address")
    locality = fields.Char(string="Locality")
    street = fields.Char(string="Street")
    pin_code = fields.Integer(string="Pin Code")


class librarybooks_payment(models.Model):
    _name = 'library.payment'
    _description = 'library.payment'
    library_payment = fields.Many2one('library.library')
    card = fields.Integer(string="Card")
    name_of_card_holder = fields.Char(string="Name")
    cvv = fields.Integer(string="CVV")
