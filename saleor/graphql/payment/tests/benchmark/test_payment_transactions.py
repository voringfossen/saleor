import pytest

from ....tests.utils import get_graphql_content

PAYMENT_TRANSACTIONS_QUERY = """
query {
  orders(first:100) {
    edges {
      node {
        payments {
          id
          transactions {
            id
            isSuccess
            token
          }
        }
      }
    }
  }
}
"""


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_payment_transactions(
    staff_api_client, orders_for_benchmarks, permission_manage_orders, count_queries
):
    content = get_graphql_content(
        staff_api_client.post_graphql(
            PAYMENT_TRANSACTIONS_QUERY,
            permissions=[permission_manage_orders],
            check_no_permissions=False,
        )
    )
    assert len(content["data"]["orders"]["edges"]) == 11
