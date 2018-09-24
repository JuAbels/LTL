- LTL.main -
============ 
fosaccs2018 demonstration python module
Version 1.0 - 24.September 2018

Contact Informations:
---------------------
Albert-Ludwigs-Universität Freiburg
juli.abels@web.de
stefan.strang@web.de

Software Description:
---------------------
This module demonstrates the content of the "LTL Semantic Tableaux and
Alternating omega-automata via Linear Factors" Paper by Martin Sulzmann
(Karlsruhe University of Applied Science) and Peter Thiemann(Faculty of
Engineering, University of Freiburg). 

General Usage:
--------------
How to Use:
	python3 main.py <input> <automatPrint> [<flag>}")
The input can be a textfile(.txt) or a string.
Content in the textfile or the string should be e.g.
	('G F p'; '{'p', 'p2', 'q1', 'q2'}') 			// unsure
AutomatPrint should be the location where the output is print to. 
It is possible to set a Flag to reprint the formula and to go to the 
menu if you want to be guided through this process.
Possible Flags are: 
	-pp [for the menu] 
	-spot 
	-spin 
	-latex
    	-test [for the testing and debugging]
        -demo[for the demonstraiton mode]

Requirements:
-------------
Developed under ubuntu 16.04 & kubuntu[Version], Python Version 3.5.2.
Further dependencies are:
	ltlfilt version 2.6.1(spot.lrde.epita.fr/ltlfilt.html)
	C++-compliant-compiler. g++ 5.0 or later
	clang++ 3.5
        graphviz version 2.38.0

License Information:
