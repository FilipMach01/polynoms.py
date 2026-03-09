from collections import namedtuple

Term = namedtuple('Term', ["q", "e"])


def clean_up(poly: str) -> str:
    return (poly
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "")
            .replace("-", "+-")
            )


def split_poly(poly: str) -> list[str]:
    return poly.split("+")


def split_term(term: str) -> list[int]:
    return list(map(int, term.split("x^")))


def read_poly(poly: str) -> list[int]:
    return list(map(split_term, split_poly(clean_up(poly))))


def parse(poly):
    polynomial = []
    for q, e in read_poly(poly):
        polynomial.append(Term(q, e))

    return polynomial


input_string = "(4x^3 - 8x^2)/(2x^2)"

poly_1, poly_2 = input_string.split("/")

# print([split_term(term) for term in split_poly(clean_up(poly_1))])
print(parse(poly_1))
