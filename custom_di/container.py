import inspect


class Container:
    def __init__(self):
        self._registry = {}

    def register(self, dependency_type, implementation=None):
        if not implementation:
            implementation = dependency_type

        for base in inspect.getmro(implementation):
            if base not in (object, dependency_type):
                self._registry[base] = implementation

        self._registry[dependency_type] = implementation

    def resolve(self, dependency_type):
        if dependency_type not in self._registry:
            raise ValueError(f"Dependency {dependency_type} not registered")
        implementation = self._registry[dependency_type]
        constructor_signature = inspect.signature(implementation.__init__)
        constructor_params = constructor_signature.parameters.values()

        dependencies = [
            self.resolve(param.annotation)
            for param in constructor_params
            if param.annotation is not inspect.Parameter.empty
        ]

        return implementation(*dependencies)
