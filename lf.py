"""
Authors: Stefan Strang
University of Freiburg - 2018

Operators:
next: 		Xf - ()
eventually 	Ff - <>
always 		Gf - []
strong until 	f U g
weak until	f W g
weak release 	f R g	f V g
strong realase 	f M g

U p1 & p2 G F p3

"""

# doubles: U W R V M

doubles = ['U', 'W', 'R', 'V', 'M']

# singles: X F G
singles = ['X', 'F', 'G']

# standard: xor f^g, and & && /\ * , or | || \/ + ,
# implication -> -->, equivalence <->,
# negation ! ~


def lf(formula, lfset={}):
    """Get the set of Linear factors."""
    print(formula)
