# -*- coding: utf-8 -*-
# from odoo import http


# class Agriculturevc(http.Controller):
#     @http.route('/agriculturevc/agriculturevc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agriculturevc/agriculturevc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agriculturevc.listing', {
#             'root': '/agriculturevc/agriculturevc',
#             'objects': http.request.env['agriculturevc.agriculturevc'].search([]),
#         })

#     @http.route('/agriculturevc/agriculturevc/objects/<model("agriculturevc.agriculturevc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agriculturevc.object', {
#             'object': obj
#         })
