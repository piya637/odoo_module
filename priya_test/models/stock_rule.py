import random

from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _run_buy(self, procurements):
        for procurement, _rule in procurements:
            procurement.values["grouping"] = (
                procurement.product_id.categ_id.procured_purchase_grouping
            )
        return super()._run_buy(procurements)

    def _make_po_get_domain(self, company_id, values, partner):
        domain = super()._make_po_get_domain(company_id, values, partner)
        if values.get("grouping") == "product_category":
            if values.get("supplier"):
                suppinfo = values["supplier"]
                product = suppinfo.product_id or suppinfo.product_tmpl_id
                domain += (
                    ("order_line.product_id.categ_id", "=", product.categ_id.id),
                )
        elif values.get("grouping") == "order":
            if values.get("move_dest_ids"):
                domain += (("id", "=", -values["move_dest_ids"][:1].id),)
            domain += (("id", "=", random.randint(-2147483648, 0)),)
        return domain
