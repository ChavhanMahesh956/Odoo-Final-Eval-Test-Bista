from odoo import models, fields,api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    weight = fields.Float(string='Weight')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.weight = self.product_id.weight
        else:
            self.weight = 0.0

    def _prepare_procurement_values(self, group_id=False):
        '''The _prepare_procurement_values method allows customization of the data that will be used to create procurement orders from sales order lines '''
        
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        self.ensure_one()

        if self.weight:
            
            values.update({
                 'weight': self.weight,
                })

        return values
    def _prepare_invoice_line(self, **optional_values):
        '''Passing new field value from sale.order.line to account.move.line ,when Invoice is created from SO'''

        self.ensure_one()
        values = super()._prepare_invoice_line(**optional_values)
        values.update({
            'weight': self.weight or '',
        })

        return values
