from odoo import models, fields

class Property(models.Model):
    _name = 'property.property'
    _description = 'Property'

    name = fields.Char(string='Property Name', required=True)
    price = fields.Float(string='Price')
    broker_id = fields.Many2one('broker.broker', string='Broker')
    sold = fields.Boolean(string='Sold', default=False)
