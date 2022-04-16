from odoo import api, fields, models


class SaleOder(models.Model):
    _inherit = "sale.order"

    last_update_amount = fields.Datetime(
        compute="_compute_last_update_amount",
        store=True,
    )
    prev_amount = fields.Float(
        default=lambda self: self and self.amount_total or 0.0,
    )

    @api.depends("amount_total")
    def _compute_last_update_amount(self):
        for sale in self:
            if self.prev_amount != sale.amount_total:
                sale.last_update_amount = fields.Datetime.now()
                sale.prev_amount = sale.amount_total
