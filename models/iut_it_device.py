# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutItDevice(models.Model):
    _name = 'iut.it.device'

    name = fields.Char(required=True)
    date_allocation = fields.Date()
    serial_number = fields.Char(required=True)
    date_purchase = fields.Date()
    date_warranty_end = fields.Date()
    model_id = fields.Many2one('iut.it.model', string='Model')
    partner_id = fields.Many2one('res.partner', string='Partner')
    room_id = fields.Integer(related='partner_id.room_id.id', store=True)
    office_id = fields.Integer(related='partner_id.room_id.office_id.id', store=True)
    #date_warranty_end = fields.Date()


    # @api.onchange('date_purchase', 'model_id.brand_id.warranty_delay_month')
    # def _change_date_warranty(self):
    #     self.date_warranty_end = self.date_purchase + self.model_id.brand_id.warranty_delay_month
