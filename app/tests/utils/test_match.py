import app.utils.match_ptrn as M
from toolz import pipe, curry
from operator import methodcaller


def test_match_ptrn():

    @curry
    def is_len_equal(amount: int, value: str) -> bool:
        return len(value) == amount

    res = pipe(
        M.from_value("enosh"),
        M.when(is_len_equal(3), "short name"),
        M.when(is_len_equal(5), "perfect name"),
        M.when(methodcaller("startswith", "e"), "already found..."),
        M.map(str.upper),
        M.or_else_get(lambda: "nothing here..."),
    )
    assert res == "perfect name".upper()
