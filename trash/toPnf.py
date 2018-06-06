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
    appe = ""
    last = junk[-1]
    while(last != ")"):
        appe = last + appe
        junk = junk[:-1]
        if(len(junk) == 0):
            break
        last = junk[-1]
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
    junkList = []
    backList = []
    first = junk[0]
    last = junk[-1]
    counter = 0
    if("("not in junk and")"not in junk):
        junkList.append(junk)
        junk = ""
    while (len(junk) > 5):
        first = junk[0]
        last = junk[-1]
        if(first in prefix):
            word, junk = pref(junk)
            junkList.append(word)
        elif(first == '(' and last == ')'):
            junkList.append((chainList(junk[1:-1]))[0])
            junk = (chainList(junk[1:-1]))[1]
        elif(first == '(' and last != ')'):
            appe, junk = appendix(junk)
            backList.append(appe)
        else:
            print("Debug!")
        counter += 1
    backList.reverse()
    for i in backList:
        junkList.append(i)
    return junkList, junk


def listed(junkList):
    """This may be redundant"""
    for i in range(len(junkList)):
        if(type(junkList[i]) == list):
            junkList[i] = listed(junkList[i])
        else:
            junkList[i] = junkList[i].split()
    return junkList


def pushIn(listed, junk):
    print(junk)
    print(listed)
    for i in listed:
        print(i)


def toPnf(inp):
    """Bring negation in front of atoms.
    Input: Formula in String
    Output: Chained list
    """
    f = spot.formula(inp)
    junk = f.to_str('spot')
    if("!" not in junk):
        print("allready in pnf")
        return junk 			# hier vllt besser die junklist
    else:
        # print("need to bring in pnf")
        junkList = (chainList(junk)[0])
        # print(junkList)
        pushIn(listed(junkList), junk)
