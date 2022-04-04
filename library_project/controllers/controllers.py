# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryProject(http.Controller):
#     @http.route('/library_project/library_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_project/library_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_project.listing', {
#             'root': '/library_project/library_project',
#             'objects': http.request.env['library_project.library_project'].search([]),
#         })

#     @http.route('/library_project/library_project/objects/<model("library_project.library_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_project.object', {
#             'object': obj
#         })
