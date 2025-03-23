from typing import Generic, TypeVar, Callable
from abc import abstractmethod

T = TypeVar("T")
R = TypeVar("R")


class Match(Generic[T]):

    @staticmethod
    def of(value: T) -> "Match[T]":
        return NotFound(value)

    @abstractmethod
    def when(self, predicate: Callable[[T], bool], alt: R) -> "Match[T]":
        pass

    @abstractmethod
    def or_else(self, default: R) -> R:
        pass

    @abstractmethod
    def or_else_get(self, supplier: Callable[[], R]) -> R:
        pass


class NotFound(Generic[T], Match[T]):

    def __init__(self, value: T):
        self.value = value

    def when(self, predicate: Callable[[T], bool], alt: R) -> "Match[T]":
        return Found(self.value, alt) if predicate(self.value) else self

    def or_else(self, default: R) -> R:
        return default

    def or_else_get(self, supplier: Callable[[], R]) -> R:
        return supplier()


class Found(Generic[T], Match[T]):

    def __init__(self, value: T, result: R):
        self.value = value
        self.result = result

    def when(self, predicate: Callable[[T], bool], alt: R) -> "Match[T]":
        return self

    def or_else(self, default: R) -> R:
        return self.result

    def or_else_get(self, supplier: Callable[[], R]) -> R:
        return self.result
