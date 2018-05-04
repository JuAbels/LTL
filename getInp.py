"""Author Stefan Strang - Uni Freiburg."""
import sys
from ltlPrint import ltlPrint
import spot

def usage():
    """Tell how to use."""
    print("usage: python3 main.py <input>")

    print("input can be textfile(.txt) or string")
    print("set flag if you want to reprint the formula")
    print("To print: python3 main.py <input> <flag>")
    print("possible Flags: -pp [menu]; -spot; -spin; -latex") 
    sys.exit(1)


def getInp():
    """Get the input via source or terminal.

    Input: Nothing
    Output: The general input or instructions
    """
    # print(len(sys.argv))
    try:
        if(len(sys.argv) == 2):
            inp = sys.argv[1]
            if(len(inp.split(".")) > 1):
                data = open(inp, "r")
                return(data.readline().strip().strip("\""))
            else:
                return inp
        elif(len(sys.argv) == 3):
            if(sys.argv[2] == "-pp"):
                inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                print(ltlPrint(back))
                return(back)
            elif(sys.argv[2] == "-spot"):
                
                inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spot'))
                return(back)
            elif(sys.argv[2] == "-spin"):
                
                inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('spin'))
                return(back)
            elif(sys.argv[2] == "-latex"):
                
                inp = sys.argv[1]
                data = open(inp, "r")
                back = data.readline().strip().strip("\"")
                f = spot.formula(back)
                print(f.to_str('latex'))
                return(back)
        else:
            exit()
    except:
        usage()
