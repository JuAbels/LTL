"""Author: Stefan Strang - Uni Freiburg."""
import spot


def translate(inp):
    """Translate input to polish pred Logic.

    input: ltl no matter what form.
    output: ltl in polish notation

    >>> from LTL.tools.ltlToPred import translate
    >>> translate('[]<>p0')
    'G F p0'
    >>> translate('p1 U (p2 & GFp3)')
    'U p1 & p2 G F p3'

    """
    f = spot.formula(inp)
    lbt = f.to_str('lbt')

    return lbt
