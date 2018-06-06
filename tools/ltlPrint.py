"""Author Stefan Strang - Uni Freiburg """
import spot


def ltlPrint(inp):
    """Function print formula.
    Input: Formula
    Output: None - prints formula to terminal
    """
    print("to which form do you want to transform the formula: ")
    print("<latex>, <lbt>, <spin>, <spot>, or <all>")
    form = input()
    form = form.strip(">")
    form = form.strip("<")
    back = ""
    if (form == 'all'):
        f = spot.formula(inp)
        g = spot.formula(inp)
        h = spot.formula(inp)
        i = spot.formula(inp)
        back = f.to_str('latex') + "\n"
        back = back + g.to_str('lbt') + "\n"
        back = back + h.to_str('spin') + "\n"
        back = back + i.to_str('spot')
    else:
        f = spot.formula(inp)
        back = f.to_str(form)
    return back
