# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class JiraIssueType(models.Model):
    _inherit = 'jira.issue.type'

    is_service_desk = fields.Boolean('Is ServiceDesk related')
