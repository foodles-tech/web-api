# Copyright 2022 Foodles (http://www.foodles.co).
# @author Pierre Verkest <pierreverkest84@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

from odoo.addons.http_routing.models.ir_http import slugify


class WebserviceConsumerMixin(models.AbstractModel):

    _name = "webservice.consumer.mixin"
    _description = "Add fields to save web service responses"

    ws_response_status_code = fields.Integer(
        "Status code",
        help="Web service response HTTP code",
    )
    ws_response_content = fields.Binary(
        "Response",
        attachment=True,
        copy=False,
        help="Web service response content",
    )
    ws_response_date = fields.Datetime(
        "Response date",
        help="Date when the web service response has been saved",
    )
    ws_response_content_filename = fields.Char(
        compute="_compute_ws_response_content_filename"
    )

    def _compute_ws_response_content_filename(self):
        for rec in self:
            if rec.ws_response_date and rec.ws_response_status_code:
                formatted_response_date = slugify(
                    rec.ws_response_date.strftime(DATETIME_FORMAT)
                )
                rec.ws_response_content_filename = "response_%s_%s.json" % (
                    formatted_response_date,
                    str(rec.ws_response_status_code),
                )
            else:
                rec.ws_response_content_filename = ""
