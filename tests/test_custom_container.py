import pytest
from custom_di.container import Container


class A:
    pass


class B:
    def __init__(self, a: A):
        self.a = a


class C:
    def __init__(self, b: B):
        self.b = b


def test_register_and_resolve():
    container = Container()

    container.register(A)
    container.register(B)
    container.register(C)

    instance_a = container.resolve(A)
    instance_b = container.resolve(B)
    instance_c = container.resolve(C)

    assert isinstance(instance_a, A)
    assert isinstance(instance_b, B)
    assert isinstance(instance_c, C)
    assert isinstance(instance_b.a, A)
    assert isinstance(instance_c.b, B)


def test_dependency_not_registered():
    container = Container()

    container.register(A)
    container.register(B)

    container.resolve(A)
    container.resolve(B)

    match = "Dependency <class 'tests.test_custom_container.C'> not registered"
    with pytest.raises(ValueError, match=match):
        container.resolve(C)
