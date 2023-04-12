from injector import Injector, inject, Module, provider, singleton
from adapters.in_memory_person_repository import InMemoryPersonRepository
from adapters.in_memory_order_repository import InMemoryOrderRepository
from adapters.in_memory_connection import InMemoryConnection
from use_cases.unit_of_work import UnitOfWork
from domain.person import Person
from domain.order import Order
from use_cases.create_person_and_order_use_case import (
    CreatePersonAndOrderUseCase)


class AppModule(Module):
    @singleton
    @provider
    def provide_connection(self) -> InMemoryConnection:
        return InMemoryConnection()

    @singleton
    @provider
    def provide_person_repository(self) -> InMemoryPersonRepository:
        return InMemoryPersonRepository()

    @singleton
    @provider
    def provide_order_repository(self) -> InMemoryOrderRepository:
        return InMemoryOrderRepository()

    @inject
    @singleton
    @provider
    def provide_unit_of_work(self,
                             connection: InMemoryConnection,
                             person_repository: InMemoryPersonRepository,
                             order_repository: InMemoryOrderRepository) -> UnitOfWork:
        return UnitOfWork(connection, person_repository, order_repository)

    @inject
    @singleton
    @provider
    def provide_create_use_case(self, unit_of_work: UnitOfWork) -> CreatePersonAndOrderUseCase:
        return CreatePersonAndOrderUseCase(unit_of_work)


injector = Injector(AppModule())
create_use_case = injector.get(CreatePersonAndOrderUseCase)

new_person = Person(id=1, name="John Doe", age=30)
new_order = Order(id=1, order_date="2023-04-03", total_amount=100.0)

person, order = create_use_case.execute(new_person, new_order)
print(person, order)
