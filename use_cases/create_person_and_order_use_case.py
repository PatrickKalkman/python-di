from typing import Tuple

from domain.person import Person
from domain.order import Order
from use_cases.unit_of_work import UnitOfWork


class CreatePersonAndOrderUseCase:
    def __init__(self, unit_of_work: UnitOfWork):
        self.unit_of_work = unit_of_work

    def execute(self, person: Person, order: Order) -> Tuple[Person, Order]:
        with self.unit_of_work as uow:
            uow.persons.add(person)

            if person.id is not None:
                order.person_id = int(person.id)
            else:
                raise ValueError("Person id cannot be None")

            uow.orders.add(order)

        return person, order
