"""Author Stefan Strang - Uni Freiburg."""
import sys
from LTL.tools.ltlPrint import ltlPrint
from LTL.tests.testMain import testMain
# from LTL.tools.demo import demo1
import spot


def usage():
    """Tell how to use."""
    print("usage: python3 main.py <input>")

    print("input can be textfile(.txt) or string")
    print("string-example: '& p1 p2 {'p1','q'}'")
    print("set flag if you want to reprint the formula")
    print("To print: python3 main.py <input> <flag>")

    print("possible Flags: -pp [menu]; -spot; -spin; -latex")
    print("Flags for testing: -test")
    print("Flags for demo-mode: -demo")
    sys.exit(1)


def getInp():
    """Get the input via source or terminal.

    Input: Nothing, read out of file or command line.
    Output: The general input or instructions


    """

    try:
        if '.' in sys.argv[1]:
            inp = "LTL/" + sys.argv[1]
        else:
            inp = sys.argv[1]
        # print(len(sys.argv))
        if(len(sys.argv) == 2):
            if(len(inp.split(".")) > 1):
                data = open(inp, "r")
                back = (data.readline().strip().strip("\""))
                secBack = data.readline().strip()
                return(back, secBack)
            else:
                print(inp)
                inp = inp.split('{')
                print(inp)
                return inp[0], '{' + inp[1]
        elif(len(sys.argv) == 3):
            if(sys.argv[2] == "-pp"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                print(ltlPrint(back))
                secBack = data.readline().strip()
                return(back, secBack)
            elif(sys.argv[2] == "-spot"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spot'))
                secBack = data.readline().strip()
                return(back, secBack)
            elif(sys.argv[2] == "-spin"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spin'))
                secBack = data.readline().strip()
                return(back, secBack)
            elif(sys.argv[2] == "-latex"):
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('latex'))
                secBack = data.readline().strip()
                return(back, secBack)
            elif(sys.argv[2] == "-test"):
                testMain()

            elif(sys.argv[2] == "-demo"):
                return 'demo', 'demo'

        else:
            exit()
    except:
        usage()
