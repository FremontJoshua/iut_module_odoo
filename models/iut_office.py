# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutOffice(models.Model):
    _name = 'iut.office'
    _inherit = 'res.partner'

    partner_ids = fields.One2many('iut.room', 'office_id', string='Rooms')

    # employee_nb = fields.Integer(compute='_compute_employee_nb')
    #
    # @api.depends('value', 'tax')
    # def _compute_employee_nb(self):
    #     for record in self:
    #         record.total = record.value + record.value * record.tax