"""
Authors: Julia Abels, Stefan Strang
University of Freiburg - 2018

"""

import sys
from LTL.tests.testMain import testMain
from LTL.tools.demo import demo1
import spot


def usage():
    """Tell how to use."""
    print("call it from the folder above.")
    print("usage: python3 -m LTL.main <input> <automatPrint> [<flag>}")

    print("input can be textfile(.txt) or string")
    print("string-example: \"('G F p'; '{'p', 'p2', 'q1', 'q2'}')\"")
    print("set flag if you want to reprint the formula")
    print("To print: python3 main.py <input> <output> <flag>")

    print("possible Flags: -pp [menu]; -spot; -spin; -latex")
    print("Flags for testing: -test")
    print("Flags for demo-mode: -demo")
    sys.exit(1)


def empty(back, secBack):
    if back == "" or secBack == "":
        sys.exit(1)


def getInp():
    """Get the input via source or terminal.

    Input: Nothing, read out of file or command line.
    Output: The general input or instructions


    """

    try:
        if '.' in sys.argv[1]:
            inp = sys.argv[1]
        else:
            inp = sys.argv[1]
        if(len(sys.argv) == 3):
            if(len(inp.split(".")) > 1):
                print(inp)
                data = open(inp, "r")
                back = (data.readline().strip().strip("\""))
                secBack = data.readline().strip()
                file_write = sys.argv[2]
                empty(back, secBack)
                return(back, secBack, file_write)
            else:
                inp = inp.strip("(")
                inp = inp.strip(")")
                inp = inp.split(";")
                retour = []
                for i in inp:
                    i = i.strip()
                    i = i.strip("'")
                    retour.append(i)
                file_write = sys.argv[2]
                empty(retour[0], retour[1])
                return retour[0], retour[1], file_write
        elif(len(sys.argv) == 4 and 1 < len(sys.argv[1].split("."))):
            print(len(sys.argv[1].split(".")))
            if(sys.argv[3] == "-pp"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                print(ltlPrint(back))
                secBack = data.readline().strip()
                file_write = sys.argv[2]
                empty(back, secBack)
                return(back, secBack, file_write)
            elif(sys.argv[3] == "-spot"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spot'))
                secBack = data.readline().strip()
                file_write = sys.argv[2]
                empty(back, secBack)
                return(back, secBack, file_write)
            elif(sys.argv[3] == "-spin"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spin'))
                secBack = data.readline().strip()
                file_write = sys.argv[2]
                empty(back, secBack)
                return(back, secBack, file_write)
            elif(sys.argv[3] == "-latex"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('latex'))
                secBack = data.readline().strip()
                file_write = sys.argv[2]
                empty(back, secBack)
                return(back, secBack, file_write)
            elif(sys.argv[3] == "-test"):
                testMain()

            elif(sys.argv[3] == "-demo"):
                demo1()
                return 'demo', 'demo'
        elif(len(sys.argv) == 4):
            inp = inp.strip("(")
            inp = inp.strip(")")
            inp = inp.split(";")
            retour = []
            for i in inp:
                i = i.strip()
                i = i.strip("'")
                retour.append(i)
            if(sys.argv[3] != "-pp"):
                f = spot.formula(retour[0])
                print(f.to_str(sys.argv[3][1:]))

            else:
                print(ltlPrint(retour[0]))
            file_write = sys.argv[2]
            empty(retour[0], retour[1])
            return retour[0], retour[1], file_write
        else:
            exit()
    except:
        usage()
