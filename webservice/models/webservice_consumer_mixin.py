# Copyright 2022 Foodles (http://www.foodles.co).
# @author Pierre Verkest <pierreverkest84@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class WebserviceConsumerMixin(models.AbstractModel):

    _name = "webservice.consumer.mixin"
    _description = "Add fields to save web service responses"

    ws_response_status_code = fields.Integer(
        "Status code", help="Web service response HTTP code"
    )
    ws_response_content = fields.Binary(
        "Response", attachment=True, copy=False, help="Web service response content"
    )
    ws_response_content_filename = fields.Char(
        compute="_compute_ws_response_content_filename"
    )

    def _compute_ws_response_content_filename(self):
        for rec in self:
            rec.ws_response_content_filename = "response_%s_%s.json" % (
                str(rec.ws_response_status_code),
                self.name_get()[1],
            )
