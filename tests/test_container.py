import pytest
from custom_di.container import Container


# Sample classes for testing
class Engine:
    pass


class DieselEngine(Engine):
    pass


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine


# Test functions
def test_resolve_simple_dependency():
    container = Container()
    container.register(Engine, DieselEngine)
    container.register(Car)

    car_instance = container.resolve(Car)
    assert isinstance(car_instance, Car)
    assert isinstance(car_instance.engine, DieselEngine)


def test_resolve_unregistered_dependency():
    container = Container()

    with pytest.raises(ValueError):
        container.resolve(Engine)


def test_resolve_base_class_dependency():
    container = Container()
    container.register(Engine, DieselEngine)
    container.register(Car)

    engine_instance = container.resolve(Engine)
    assert isinstance(engine_instance, DieselEngine)
