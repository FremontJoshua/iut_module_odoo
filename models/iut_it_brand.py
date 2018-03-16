# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutItBrand(models.Model):
    _name = 'iut.it.brand'

    name = fields.Char(required=True)
    warranty_delay_month = fields.Integer()
    support_phone = fields.Integer()
    model_ids = fields.One2many('iut.it.model', 'brand_id', string='Models')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]