"""Author Stefan Strang - Uni Freiburg."""
import sys
from ltlPrint import ltlPrint


def usage():
    """Tell how to use."""
    print("usage: python3 main.py <input>")

    print("input can be textfile(.txt) or string")
    print("set flag if you want to reprint the formula")
    print("to print: python3 main.py <input> -pp")
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
            
            inp = sys.argv[1]
            
            data = open(inp, "r")
            back = data.readline().strip().strip("\"")
            ltlPrint(back)
            return(back)
            
        else:
            exit()
    except:
        usage()
