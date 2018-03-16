# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutRoom(models.Model):
    _name = 'iut.room'

    floor = fields.Char()
    name = fields.Char(required=True)
    partner_ids = fields.One2many('res.partner', 'room_id', string='Partners')
    office_id = fields.Many2one('iut.office', string='Office')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]