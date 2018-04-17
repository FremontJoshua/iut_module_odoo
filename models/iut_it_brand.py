# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class IutItBrand(models.Model):
    _name = 'iut.it.brand'

    name = fields.Char(required=True)
    warranty_delay_month = fields.Integer()
    support_phone = fields.Char()
    model_ids = fields.One2many('iut.it.model', 'brand_id', string='Models')

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]

    @api.multi
    def change_date_warranties(self):
        self.ensure_one()
        for oneModel in self.model_ids:
            for oneDevice in oneModel.device_ids:
                oneDevice._change_date_warranty()