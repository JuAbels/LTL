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
- [ ] Docstrings überall auf ein level bringen
- [ ] Testfälle
- [ ] wie möchten wir die speicherung des outputs haben?
- [ ] mögliche testfälle für tableaudecissiongrafik herausarbeiten
- [ ] doctest testfälle tuple/obs to name
- [ ] klarmachen ob bei decission tableau richtig verstanden und implementiert
wurde das die junktion von endbedingungen angeht
- [ ] idealerweise globale variblen ersetzen 
- [ ] testfälle für omega automaten ausdenken
- [ ] wenn alles fertig clean code konventionen durchsetzen. 

## Testfälle

lf
| U q p | a b
X R q p & a b

derivatives 
R | q1 p2 p3  	zu true und false
| U q p | a b 	zu true und false
X R q p & a b 	zu true und false
