from collections import namedtuple
from operator import attrgetter
from mercurial.hgweb.common import continuereader

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


def sort_e(poly):
    return sorted(parse(poly), key=attrgetter('e'), reverse=True)


#alg

def div_leading(num, denum):

    return Term(num[0].q / denum[0].q, num[0].e - denum[0].e)

def mult_poly(poly, term):

    return sorted([Term(t.q * term.q, t.e + term.e) for t in poly],
                  key=lambda t: t.e, reverse=True)

def sub_poly(a, b):

    terms = {t.e: t.q for t in a}
    for t in b:
        terms[t.e] = terms.get(t.e, 0) - t.q
    result = sorted([Term(q, e) for e, q in terms.items() if q != 0],
                    key=lambda t: t.e, reverse=True)
    return result


input_string = "(6x^3 + 11x^2 - 4x^1 - 4x^0)/(3x^1 - 2x^0)"
n, d = input_string.split("/")

num = sort_e(n)
denum = sort_e(d)
result = []

while num and num[0].e >= denum[0].e:
    lead = div_leading(num, denum)
    result.append(lead)
    product = mult_poly(denum, lead)
    num = sub_poly(num, product)

print("Result:", result)
print("Residue:", num)


