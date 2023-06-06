from sys import maxsize
from typing import TypeVar

from .model_proto import Model

Tensor = TypeVar("Tensor") # TODO use jaxtyping

def greedy_search(model: Model, input_ids: Tensor,*, eos_token_id: int, max_length: int = maxsize):
    raise NotImplemenentedError()
