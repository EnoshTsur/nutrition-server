from typing import TypeVar, Callable
from toolz import curry
from .match_case import Match

T = TypeVar("T")
R = TypeVar("R")


def from_value(v: T) -> Match[T]:
    return Match.of(v)


@curry
def when(predicate: Callable[[T], bool], result: R, container: Match[T]) -> Match[T]:
    return container.when(predicate, result)


@curry
def or_else(default: R, container: Match[T]) -> R:
    return container.or_else(default)
