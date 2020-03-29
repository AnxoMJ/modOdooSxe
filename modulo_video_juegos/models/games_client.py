# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class GameClients(models.Model):
    _name = 'game.client'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete = 'cascade')
    date_start = fields.Date('Cliente Desde',default = lambda *a:datetime.now().strftime('%Y-%m-%d'))
    date_of_birth = fields.Date('Fecha de nacimiento', required = True)
    remaining_orders = fields.Integer('Pedidos Pendientes', compute = 'check_remain_orders', default = 0)
    total_price = fields.Float('Precio Total', compute = 'check_remain_orders', default = 0)

#constrain que verifica que no sea más joven que el día en el que se registra
    @api.constrains('date_of_birth', 'date_start')
    def _check_dates(self):
        for client in self:
            if client.date_of_birth >= client.date_start:
                raise models.ValidationError('No puede ser mas joven que cuando se hizo miembro!!!')

#se encarga de actualizar el campo remaining_orders
    @api.multi
    def check_remain_orders(self):
        orders = self.env['game.reserve']
        for cliente in orders.search([]):
            cont = 0
            totalPrice = 0
            for order in orders.search([]):
                if (order.isCompleted == False and order.client_id == cliente.client_id):
                    totalPrice+=order.game_id.price
                    cont+=1
                cliente.client_id.remaining_orders = cont
                cliente.client_id.total_price = totalPrice
