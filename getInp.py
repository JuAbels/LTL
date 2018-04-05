"""Author Stefan Strang - Uni Freiburg"""
import sys


def usage():
    """Tell how to use."""
    print("usage: python3 main.py <input>")
    print("input can be textfile(.txt) or string")


def getInp():
    """Get the input via source or terminal
    Input: Nothing
    Output: The general input or instructions
    """
    try:
        if(len(sys.argv)==2):
            inp = sys.argv[1]
            if(len(inp.split("."))>1):
                
                data = open(inp, "r")
                return(data.readline().strip().strip("\""))
            else:
                return inp
                
        else:
            usage()
    except:
        usage()
    
    
