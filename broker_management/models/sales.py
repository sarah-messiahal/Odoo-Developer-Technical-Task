from odoo import models, fields, api

class Sale(models.Model):
    _name = 'sale.sale'
    _description = 'Property Sale'

    property_id = fields.Many2one('property.property', string='Property', required=True)
    broker_id = fields.Many2one('broker.broker', string='Broker', required=True)
    sale_price = fields.Float(string='Sale Price')
    commission = fields.Float(string='Commission', compute='_compute_commission', store=True)

    @api.depends('sale_price', 'broker_id.commission_rate')
    def _compute_commission(self):
        for record in self:
            record.commission = record.sale_price * (record.broker_id.commission_rate / 100)
