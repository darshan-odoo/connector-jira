# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import jira
from jira.utils import CaseInsensitiveDict

from odoo.addons.component.core import Component


class Organization(jira.resources.Resource):
    """A Service Desk Organization."""

    def __init__(self, options, session, raw=None):
        super().__init__(
            'organization/{0}',
            options,
            session,
            '{server}/rest/servicedeskapi/{path}'
        )
        if raw:
            self._parse_raw(raw)


class OrganizationAdapter(Component):
    _name = 'jira.organization.adapter'
    _inherit = ['jira.webservice.adapter']
    _apply_on = ['jira.organization']

    _desk_headers = CaseInsensitiveDict({'X-ExperimentalApi': 'opt-in'})

    def __init__(self, work_context):
        super().__init__(work_context)
        self.client._session.headers.update(self._desk_headers)

    def read(self, id_):
        organization = Organization(
            self.client._options,
            self.client._session
        )
        organization.find(id_)
        return organization.raw

    def search(self):
        base = (self.client._options['server'] +
                '/rest/servicedeskapi/organization')
        orgs = self.client._fetch_pages(
            Organization,
            'values',
            'organization',
            # limit to False will get them in batch
            maxResults=False,
            base=base
        )
        return [org.id for org in orgs]
