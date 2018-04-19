"""
Authors: Stefan Strang
University of Freiburg - 2018
"""
import spot

def toPnf(inp):
    f = spot.formula(inp)
    junk = f.to_str('spot')
    
