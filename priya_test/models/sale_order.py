from odoo import Command, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    copy_clipboard = fields.Char(string="Copy Clipboard")

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            for picking in order.picking_ids:
                picking.delivery_tag_ids = [Command.set(self.tag_ids.ids)]
        return res
