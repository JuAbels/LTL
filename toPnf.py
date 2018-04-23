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
prefix = "qwertzuiopüasdfghjklöäyxcvbnm!&~0123456789 "

def appendix(junk):
    """Strip the rest from junk.
    Output: newJunk and appendix
    input: "(p0 & p1) U p2"
    output: (' U p2', '(p0 & p1)')

    """
    #print(junk)
    appe = ""
    last = junk[-1]
    while(last != ")"):
        
        appe = last + appe
        junk = junk[:-1]
        if(len(junk) == 0):
            break
        last = junk[-1]
    #print(appendix)
    #print(junk)
    return appe, junk

def pref(junk):
    first = junk[0]
    junk = junk[1:]
    word = ""
    while (first in prefix):
        word = word + first
        first = junk[0]
        if first in prefix:
            junk = junk[1:]
        else:
            break
    junk = first + junk[1:]
    return word, junk

def chainList(junk):
    """Get a more handy format.
    chained list instead of string"""
    #print(junk)
    junkList = []
    backList = []
    first = junk[0]
    last = junk [-1]
    counter = 0
    while counter < 2:
        first = junk[0]
        last = junk [-1]
        if(first in prefix):
            #print("prefix")
            #print(junk)
            if("(" in junk):
                junkList.append(pref(junk)[0])
            
                junk = pref(junk)[1]
            else:
                backList.append(list(junk))
            
        elif(first == '(' and last == ')'):
            #print("chainList")
            #print(junk)
            junkList.append(chainList(junk[1:-1]))####
        elif(first == '(' and last != ')'):
            #print("appendix")
            #print(junk)
            appe, junk = appendix(junk)
            backList.append(appe)
        else:
            print("Debug!")
        counter += 1
    backList.reverse()
    for i in backList:
         junkList.append(i)

    return junkList





def toPnf(inp):
    """Bring negation in front of atoms.
    Input: Formula in String
    Output: Chained li 
    """
    f = spot.formula(inp)
    junk = f.to_str('spot')
    print(junk)
    print(chainList(junk))
    
   
