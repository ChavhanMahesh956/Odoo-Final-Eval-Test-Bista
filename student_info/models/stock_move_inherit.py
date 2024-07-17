from odoo import api,fields,models

class StockMove(models.Model):
    _inherit = 'stock.move'

    weight = fields.Float(string='Weight')

    def _prepare_procurement_values(self):
        values = super(StockMove, self)._prepare_procurement_values()
        values["sale"] = self.group_id.sale_id
