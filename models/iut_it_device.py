# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class IutItDevice(models.Model):
    _name = 'iut.it.device'

    name = fields.Char(required=True)
    date_allocation = fields.Date()
    serial_number = fields.Char(required=True)
    date_purchase = fields.Date(default=datetime.datetime.today())
    date_warranty_end = fields.Date()
    model_id = fields.Many2one('iut.it.model', string='Model')
    partner_id = fields.Many2one('res.partner', string='Partner')
    room_id = fields.Integer(related='partner_id.room_id.id', store=True, string='Room')
    office_id = fields.Integer(related='partner_id.room_id.office_id.id', store=True, string='Office')
    is_free = fields.Boolean(string="Libre", default=True)

    _sql_constraints = [
        ('serial_number_unique',
         'unique(serial_number)',
         'Choose another value - it has to be unique!')
    ]


    @api.onchange('date_purchase', 'model_id', 'model_id.brand_id.warranty_delay_month')
    def _change_date_warranty(self):
        self.date_warranty_end = (datetime.datetime.strptime(self.date_purchase, '%Y-%m-%d') +
                                  datetime.timedelta(self.model_id.brand_id.warranty_delay_month * 365/12)).strftime('%Y-%m-%d')

    @api.multi
    def change_state_free(self):
        self.ensure_one()
        self.is_free = not(self.is_free)
        if self.is_free:
            self.date_allocation = ''