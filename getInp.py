"""Author Stefan Strang - Uni Freiburg."""
import sys
from ltlPrint import ltlPrint
import spot
import doctest

def usage():
    """Tell how to use."""
    print("usage: python3 main.py <input>")

    print("input can be textfile(.txt) or string")
    print("set flag if you want to reprint the formula")
    print("To print: python3 main.py <input> <flag>")
    print("possible Flags: -pp [menu]; -spot; -spin; -latex") 
    sys.exit(1)


def getInp(inp = sys.argv[1]):
    """Get the input via source or terminal.

    Input: Nothing, read out of file or command line.
    Output: The general input or instructions
    
    >>> import os

    >>> from getInp import getInp
    >>> f = open('testfile.txt', 'w')
    >>> getInp(inp = 'testfile.txt')
    ('', '')
    >>> f.write('G F p\n')
    6
    >>> f.write('{"p", "p2", "q1", "q2"}')
    23
    >>> f.close()
    >>> getInp(inp = 'testfile.txt')
    ('G F p', '{"p", "p2", "q1", "q2"}')
    >>> os.remove('testfile.txt')

    """
    #print(inp)
    try:
        if(len(sys.argv) == 2):
            #inp = sys.argv[1]
            if(len(inp.split(".")) > 1):
                data = open(inp, "r")
                back = (data.readline().strip().strip("\""))
                #print(back)
                secBack = data.readline().strip()
                #print(secBack)
                return(back, secBack)
            else:
                return inp
        elif(len(sys.argv) == 3):
            if(sys.argv[2] == "-pp"):
                #inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                print(ltlPrint(back))
                #print(back)
                secBack = data.readline().strip()
                return(back,secBack)
            elif(sys.argv[2] == "-spot"):
                
                #inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spot'))
                secBack = data.readline().strip()
                return(back, secBack)
            elif(sys.argv[2] == "-spin"):
                
                #inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spin'))
                secBack = data.readline().strip()
                return(back, secBack)
            elif(sys.argv[2] == "-latex"):
                
                #inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('latex'))
                secBack = data.readline().strip()
                return(back, secBack)
        else:
            exit()
    except:
        usage()
