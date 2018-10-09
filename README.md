# LTL

## Struktur

1. Definition einer Datenstruktur für die LTL Formeln
2. Parser für LTL Formeln, also Einlesen von Datei (Syntax dafür gebe ich vor, da gibt es einen Standard)
3. Ausdrucken von LTL Formeln
4. Implementierung von LF (def 8)
5. Implementierung von partial derivatives (def 10)
6. Implementierung des AFA (Def 16), also Datenstruktur dafür, Ausdrucken, cool wäre eine graphische Ausgabe: dafür muss eine Datei im DOT Format (siehe https://www.graphviz.org/) erzeugt werden
7. Implementierung der Konstruktion in Def 17, das ist eine etwas andere Graphstruktur, die dann nach bestimmten Regeln bearbeitet werden muss. Auch dafür ist eine graphische Ausgabe sinnvoll.

## ToDo's

- [ ] möglichen input für den code zusammen bekommen.
- [ ] randfälle abdecken

- [ ] Fehler bei falscher eingabe von ltl formeln abfangen. etwa falsche klammerung
- [ ] bei input mittels konsolzeile ohne input.txt. das x noch implementieren???

neu:
- [ ] Testfälle
- [ ] wie möchten wir die speicherung des outputs haben?
- [ ] mögliche testfälle für tableaudecissiongrafik herausarbeiten (Julia)
- [ ] doctest testfälle tuple/obs to name (Stefan)
- [ ] klarmachen ob bei decission tableau richtig verstanden und implementiert
wurde das die junktion von endbedingungen angeht
- [ ] ebenso was bei einer junktion bei derivatives gemacht wurde und ob es richtig implementiert wurde.
- [ ] testfälle für omega automaten ausdenken (Julia)
- [ ] def 6 negativ testen
- [ ] an der readme arbeiten.
	=> hardqare requirements?!
- [ ] Docstrings überall auf ein level bringen
	=> lf case literal?! check nicht was passiert
        => ist iterated derivatives und flat.py überhaupt noch aktuell? wenn ja auch hier nochmal docstrings überarbeiten. ansonsten fertig


- [ ] wenn alles fertig clean code konventionen durchsetzen. 
- [ ] idealerweise globale variblen ersetzen 

## Testfälle

lf
- müsste fertig sein
- vllt noch ein paar länge zufällige formeln. oder mit F und G

derivatives (stefan)
R | q1 p2 p3  	zu true und false
| U q p | a b 	zu true und false
X R q p & a b 	zu true und false
'& p2 | p3 U p4 p2' zu true und false
