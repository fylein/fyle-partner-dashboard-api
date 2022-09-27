"""
V1 Beta Accountant Orgs
"""

from typing import Dict
from ....internals.list_resources import ListResources
from ....internals.list_all_resources import ListAllResources


class Orgs(ListResources, ListAllResources):
    """Class for Orgs APIs."""

    ORGS = "/orgs"

    def __init__(self, version, role):
        super().__init__(version, role, Orgs.ORGS)

    # Return Dummy Data
    def list(self, query_params=None) -> Dict:
        return {
            "count": 3,
            "data": [
                {
					"name": "Goldman Sachs",
					"id": "orgs124",
					"logo_download_url": "https://xyz.something.something",
					"pending_invitations": 14,
					"active_users_count": 34,
					"total_users_count": 100,
					"incomplete_card_expenses_count": 42,
					"reports_to_approve_count": 3,
					"pending_reimbursement_amount": 1889.2,
					"currency": "USD"
				},
				{
					"org_name": "QuickBooks",
					"org_id": "orgs124",
					"logo_download_url": "https://xyz.something.something",
					"active_users_count": 34,
					"total_users_count": 100,
					"incomplete_card_expenses_count": 42,
					"reports_to_approve_count": 3,
					"pending_reimbursement_amount": 1889.2,
					"currency": "USD"
				},
				{
					"org_name": "NetSuite",
					"org_id": "orgs124",
					"logo_download_url": "https://xyz.something.something",
					"active_users_count": 34,
					"total_users_count": 100,
					"incomplete_card_expenses_count": 42,
					"reports_to_approve_count": 3,
					"pending_reimbursement_amount": 1889.2,
					"currency": "USD"
				}
		]
    }
