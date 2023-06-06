from typing import Protocol, runtime_checkable

@runtime_checkable
class Model(Protocol):
    def __call__(inputs, *args, **kwargs):
        ...
