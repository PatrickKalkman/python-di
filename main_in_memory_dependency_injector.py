from dependency_injector import providers, containers
from adapters.in_memory_person_repository import InMemoryPersonRepository
from adapters.in_memory_order_repository import InMemoryOrderRepository
from adapters.in_memory_connection import InMemoryConnection
from use_cases.unit_of_work import UnitOfWork
from domain.person import Person
from domain.order import Order
from use_cases.create_person_and_order_use_case import (
    CreatePersonAndOrderUseCase)


class Container(containers.DeclarativeContainer):
    connection = providers.Singleton(
        InMemoryConnection
    )

    person_repository = providers.Singleton(
        InMemoryPersonRepository
    )

    order_repository = providers.Singleton(
        InMemoryOrderRepository
    )

    unit_of_work = providers.Singleton(
        UnitOfWork,
        connection=connection,
        person_repository=person_repository,
        order_repository=order_repository
    )

    create_use_case = providers.Factory(
        CreatePersonAndOrderUseCase,
        unit_of_work=unit_of_work
    )


if __name__ == '__main__':
    container = Container()
    create_use_case = container.create_use_case()

    new_person = Person(id=1, name="John Doe", age=30)
    new_order = Order(id=1, order_date="2023-04-03", total_amount=100.0)

    person, order = create_use_case.execute(new_person, new_order)
    print(person, order)
