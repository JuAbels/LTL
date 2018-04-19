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

!(p1 U (p2 & GFp3))

"""

import spot

def toPnf(inp):
    """Bring negation in front of atoms."""
    f = spot.formula(inp)
    junk = f.to_str('spot')
    print(inp)
    print(junk)
    paraOpen = 0
    paraClosed = 0
    depth = 0 		# hier irgendwe die tiefe bestimmen
    for i in junk:
        if(i == '('):
            paraOpen = paraOpen +1
        if(i == ')'):
            paraClosed = paraOpen +1
    if(paraOpen != paraClosed):
        print("invalid formula - parenthese error")
    

