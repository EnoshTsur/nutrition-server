from functools import partial
from operator import add, eq

if __name__ == "__main__":
    is_valid_age = partial(eq, 18)
    add_year = partial(add, 1)
    print(is_valid_age(add_year(17)))

    upper_list = partial(map, str.upper)
    print(list(upper_list(["enosh", "loves", "partial", "application"])))
