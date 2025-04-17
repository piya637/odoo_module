{
    "name": "priya Test",
    "version": "18.0.1.0.0",
    "category": "Hidden",
    "summary": "priya Test",
    "depends": [
        "sale_management",
        "stock",
        "sale",
        "mrp",
        "base_automation",
        "purchase",
    ],
    "data": [
        "data/mail_template_data.xml",
        "data/automated_action_data.xml",
        "views/stock_picking_views.xml",
        "views/sale_order_views.xml",
        "views/mrp_production_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "priya_test/static/src/components/**/*",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
