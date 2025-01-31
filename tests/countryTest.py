from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def test_country(test):
    """class `Country` werkt correct"""
    canada = getModule().Country('Canada', 34482779, 9984670)
    if canada.name != 'Canada':
        raise AssertionError("de attribute `name` van een nieuw Country-object bevat niet de gegeven naam")
    if canada.population != 34482779:
        raise AssertionError("de attribute `population` van een nieuw Country-object bevat niet het gegeven aantal mensen")
    if canada.area != 9984670:
        raise AssertionError("de attribute `area` van een nieuw Country-object bevat niet de gegeven oppervlake")
    usa = getModule().Country('United States of America', 313914040, 9826675)
    if not canada.is_larger(usa):
        raise AssertionError("is_larger werkt niet als we een kleiner land als parameter meegeven")
    if canada.population_density() != 3.4535722262227995:
        raise AssertionError("population_density geeft niet de juiste uitkomst")
    if usa.__str__() != 'United States of America has a population of 313914040 and is 9826675 square km.':
        raise AssertionError("het format van Country.__str__ is niet correct")
    if has_call('isinstance'):
        raise AssertionError("let op dat je geen isinstance() gebruikt")
