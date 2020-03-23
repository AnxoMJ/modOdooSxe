# -*- coding: utf-8 -*-
from odoo import http

# class ModuloVideoJuegos(http.Controller):
#     @http.route('/modulo_video_juegos/modulo_video_juegos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_video_juegos/modulo_video_juegos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_video_juegos.listing', {
#             'root': '/modulo_video_juegos/modulo_video_juegos',
#             'objects': http.request.env['modulo_video_juegos.modulo_video_juegos'].search([]),
#         })

#     @http.route('/modulo_video_juegos/modulo_video_juegos/objects/<model("modulo_video_juegos.modulo_video_juegos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_video_juegos.object', {
#             'object': obj
#         })