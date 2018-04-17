# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IutOffice(models.Model):
    _name = 'iut.office'
    _inherit = 'res.partner'

    room_ids = fields.One2many('iut.room', 'office_id', string='Rooms')
    employee_nb = fields.Integer(compute='_compute_employee_nb')
    count_devices = fields.Integer(compute="_count_devices")

    @api.depends()
    def _compute_employee_nb(self):
        return True

    @api.depends('is_company','parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        pass

    def _count_devices(self):
        self.ensure_one()
        for oneRoom in self.room_ids:
            for onePartner in oneRoom.partner_ids:
                self.count_devices = self.count_devices + len(onePartner.device_ids)

