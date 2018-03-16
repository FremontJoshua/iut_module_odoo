# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutItModel(models.Model):
    _name = 'iut.it.model'

    name = fields.Char(required=True)
    ref = fields.Char()
    device_ids = fields.One2many('iut.it.device', 'model_id', string='Devices')
    brand_id = fields.Many2one('iut.it.brand', string='Brand')
    type_ids = fields.Many2many('iut.model.type', string='Types')

    _sql_constraints = [
        ('ref_unique',
         'unique(ref)',
         'Choose another value - it has to be unique!')
    ]