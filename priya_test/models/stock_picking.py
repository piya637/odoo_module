from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    delivery_tag_ids = fields.Many2many(
        comodel_name="crm.tag",
        string="Tags",
    )
