# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutItDevice(models.Model):
    _name = 'iut.it.device'

    name = fields.Char(required=True)
    date_allocation = fields.Date()
    serial_number = fields.Char(required=True)
    date_purchase = fields.Date()
    date_warranty_ = fields.Date()
    model_id = fields.Many2one('iut.it.model', string='Model')
    partner_id = fields.Many2one('res.partner', string='Partner')
