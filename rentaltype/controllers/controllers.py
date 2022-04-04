# -*- coding: utf-8 -*-
# from odoo import http


# class Rentaltype(http.Controller):
#     @http.route('/rentaltype/rentaltype', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentaltype/rentaltype/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentaltype.listing', {
#             'root': '/rentaltype/rentaltype',
#             'objects': http.request.env['rentaltype.rentaltype'].search([]),
#         })

#     @http.route('/rentaltype/rentaltype/objects/<model("rentaltype.rentaltype"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentaltype.object', {
#             'object': obj
#         })
