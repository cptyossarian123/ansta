from decimal import *
from typing import List, Generator


# task 0


def post_code_to_int(code: str) -> int:
    return int(code.replace('-', ''))


def int_to_post_code(code: int) -> str:
    return f'{code // 1000}-{code % 1000:03}'


def generate_post_codes(first: str, last: str) -> List[str]:
    first_num, last_num = map(
        post_code_to_int,
        (first, last)
    )
    return list(
        map(int_to_post_code,
            range(first_num, last_num))
    )


print(generate_post_codes('79-900', '80-155'))


# task 1


def find_missing_numbers(seq: List[int], upper_limit: int) -> List[int]:
    set_seq = set(seq)
    res = []
    for n in range(1, upper_limit + 1):
        if n not in set_seq:
            res.append(n)
    return res


print(find_missing_numbers([2, 3, 7, 4, 9], 10))


# task 2


def decimal_range(start: Decimal,
                  stop: Decimal,
                  step: Decimal) -> Generator[Decimal, None, None]:
    cur = start
    while cur != stop:
        yield cur
        cur += step


*res, = decimal_range(Decimal(2), Decimal('5.5'), Decimal('0.5'))
print(res)
