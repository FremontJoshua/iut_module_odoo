# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    employee_ref = fields.Char()
    device_ids = fields.One2many('iut.it.device', 'partner_id', string='Devices')
    room_id = fields.Many2one('iut.room', string='Room')