# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutModelType(models.Model):
    _name = 'iut.model.type'

    name = fields.Char(required=True)
    model_ids = fields.Many2many('iut.it.model', string='Models')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]