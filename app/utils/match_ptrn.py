from dataclasses import dataclass
from typing import TypeVar, Generic, Callable, Union
from toolz import curry
from returns.result import Failure, Success, Result

T = TypeVar("T")
R = TypeVar("R")
S = TypeVar("S")
E = TypeVar("E")

Predicate = Callable[[T], bool]


@dataclass(frozen=True)
class Found(Generic[T, R]):
    value: T
    result: R


@dataclass(frozen=True)
class NotFound(Generic[T]):
    value: T


Match = Union[Found[T, R], NotFound[T]]


def is_found(container: Match) -> bool:
    return isinstance(container, Found)


def from_value(value: T) -> Match:
    return NotFound(value=value)


@curry
def map(transformer: Callable[[R], S], container: Match) -> Match:
    if isinstance(container, Found):
        return Found(value=container.value, result=transformer(container.result))
    return container


@curry
def when(predicate: Predicate[T], result: R, container: Match) -> Match:
    if isinstance(container, NotFound) and predicate(container.value):
        return Found(value=container.value, result=result)
    return container


@curry
def to_result(error: E, container: Match) -> Result[R, E]:
    if is_found(container):
        return Success(container.result)
    return Failure(error)


@curry
def or_else(other: R, container: Match) -> R:
    return container.result if is_found(container) else other


@curry
def or_else_get(supplier: Callable[[], R], container: Match) -> R:
    return container.result if is_found(container) else supplier()
