from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("ref", operator, name), ("name", operator, name)]
        partners = self.search(domain + args, limit=limit)
        return [(record.id, record.display_name) for record in partners]

    @api.depends("name", "ref")
    def _compute_display_name(self):
        for partner in self:
            name = partner.name or ""
            if partner.ref:
                partner.display_name = f"{name} [{partner.ref}]"
            else:
                partner.display_name = name
