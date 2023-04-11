from domain.order import Order
from adapters.in_memory_order_repository import InMemoryOrderRepository


def test_in_memory_order_repository():
    repo = InMemoryOrderRepository()
    order1 = Order(id=1, person_id=1, order_date="2022-01-01",
                   total_amount=10.0)
    order2 = Order(id=2, person_id=2, order_date="2022-01-02",
                   total_amount=20.0)

    # Add orders
    repo.add(order1)
    repo.add(order2)

    # Get order by id
    assert repo.get_by_id(order1.id) == order1
    assert repo.get_by_id(order2.id) == order2

    # Update order
    order1.total_amount = 15.0
    repo.update(order1)
    assert repo.get_by_id(order1.id).total_amount == 15.0

    # Delete order
    repo.delete(order2.id)
    assert repo.get_by_id(order2.id) is None
