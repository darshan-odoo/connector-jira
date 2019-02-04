# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.connector.components.mapper import mapping, only_create
from odoo.addons.component.core import Component


class IssueTypeMapper(Component):
    _inherit = ['jira.issue.type.mapper']

    @only_create
    @mapping
    def service_desk(self, record):
        if 'Created by Jira Service Desk' in record['description']:
            return {'is_service_desk': True}
