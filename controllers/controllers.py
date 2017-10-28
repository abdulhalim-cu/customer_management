# -*- coding: utf-8 -*-
from odoo import http

# class CustomerManagement(http.Controller):
#     @http.route('/customer_management/customer_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_management/customer_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_management.listing', {
#             'root': '/customer_management/customer_management',
#             'objects': http.request.env['customer_management.customer_management'].search([]),
#         })

#     @http.route('/customer_management/customer_management/objects/<model("customer_management.customer_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_management.object', {
#             'object': obj
#         })