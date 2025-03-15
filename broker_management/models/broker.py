from odoo import models, fields

class Broker(models.Model):
    _name = 'broker.broker'
    _description = 'Real Estate Broker'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    commission_rate = fields.Float(string='Commission Rate (%)', default=5.0)
    property_ids = fields.One2many('property.property', 'broker_id', string='Properties')
    sale_ids = fields.One2many('sale.sale', 'broker_id', string='Sales')
