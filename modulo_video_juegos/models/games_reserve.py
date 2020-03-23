# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class GameReserve(models.Model):
    _name = 'game.reserve'
    _description = 'Reserva Videojuegos'
    _rec_name = 'game_id'
    _order = 'date_start desc'

    client_id = fields.Many2one('game.client', required = True)
    isCompleted = fields.Boolean('Completado', default = False)
    game_id =  fields.Many2one('games', required = True)
    date_start = fields.Date('Fecha del pedido', default = lambda *a:datetime.now().strftime('%Y-%m-%d'))
    date_complete = fields.Date('Fecha de finalización')

    client_image = fields.Binary('Imagen Cliente', related = 'client_id.partner_id.image')

#actualiza los pedidos
    @api.multi
    def completed(self):
        if self.isCompleted:
            raise models.ValidationError('Ya estaba completado!!!')
            return False
        self.ensure_one()
        self.date_complete = datetime.now().strftime('%Y-%m-%d')
        self.isCompleted = True
        return True

#muestra la cantidad de pedidos pendientes(que no estan completados) del cliente actual
    @api.multi
    def contOrders(self):
        orders = self.env['game.reserve']
        cont = 0
        for order in orders.search([]):
            if (order.isCompleted == False and order.client_id == self.client_id):
                cont+=1
        raise models.ValidationError('Encargos pendientes: '+str(cont))

#constrain que verifica que no se reserve un videojuego no disponible
    @api.constrains('game_id')
    def _check_dates(self):
        for client in self:
        #    if client.date_of_birth >= client.date_start:
            if client.game_id.state=="unavailable":
                    raise models.ValidationError('No se puede reservar un videojuego que no esta disponible!!!')
