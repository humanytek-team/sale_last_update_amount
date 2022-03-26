from odoo import api, fields, models


class SaleOder(models.Model):
    _inherit = "sale.order"

    last_update_amount = fields.Datetime(
        compute="_compute_last_update_amount",
        store=True,
    )

    @api.depends("amount_total")
    def _compute_last_update_amount(self):
        for sale in self:
            sale.last_update_amount = fields.Datetime.now()
