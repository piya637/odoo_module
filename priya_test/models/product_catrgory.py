from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    _inherit = "product.category"

    procured_purchase_grouping = fields.Selection(
        [
            ("product_category", "Product category grouping"),
        ],
        default="product_category",
    )

    @api.constrains("name", "parent_id")
    def _check_unique_name(self):
        for category in self:
            if category.name:
                normalized_name = category.name.strip().lower()
                similar_categories = self.search([("id", "!=", category.id)])
                for similar_category in similar_categories:
                    if (
                        similar_category.name
                        and similar_category.name.strip().lower() == normalized_name
                    ):
                        raise ValidationError(
                            _("Category with this name already exists: %s")
                            % category.name
                        )
