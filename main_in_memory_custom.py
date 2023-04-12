from adapters.in_memory_person_repository import InMemoryPersonRepository
from adapters.base_repository import BaseRepository
from adapters.in_memory_order_repository import InMemoryOrderRepository
from adapters.in_memory_connection import InMemoryConnection
from adapters.base_connection import BaseConnection
from use_cases.unit_of_work import UnitOfWork
from domain.person import Person
from domain.order import Order
from use_cases.create_person_and_order_use_case import (
    CreatePersonAndOrderUseCase)

from custom_di.container import Container

container = Container()
container.register(BaseConnection, InMemoryConnection)
container.register(BaseRepository[Person], InMemoryPersonRepository)
container.register(BaseRepository[Order], InMemoryOrderRepository)
container.register(UnitOfWork)
container.register(CreatePersonAndOrderUseCase)

create_use_case = container.resolve(CreatePersonAndOrderUseCase)

new_person = Person(id=1, name="John Doe", age=30)
new_order = Order(id=1, order_date="2023-04-03", total_amount=100.0)

person, order = create_use_case.execute(new_person, new_order)
print(person, order)
