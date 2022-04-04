# -*- coding: utf-8 -*-
# from odoo import http


# class Rentalmanagement(http.Controller):
#     @http.route('/rentalmanagement/rentalmanagement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentalmanagement/rentalmanagement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentalmanagement.listing', {
#             'root': '/rentalmanagement/rentalmanagement',
#             'objects': http.request.env['rentalmanagement.rentalmanagement'].search([]),
#         })

#     @http.route('/rentalmanagement/rentalmanagement/objects/<model("rentalmanagement.rentalmanagement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentalmanagement.object', {
#             'object': obj
#         })
