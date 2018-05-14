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
- [ ] Syntax und Semantic von LTL Formeln verstehen und Struktur überlegen
- [ ] Logiken Hardcoden

- [ ] Linearfaktoren zerlegung (stefan)
- [ ] + passende ableitungen klarmachen und implementieren
- [ ] gedanken zu 5tens machen
- [ ] syntax von ltlfilt
- [ ] Fehler bei falscher eingabe von ltl formeln abfangen. etwa falsche klammerung
- LF Definition:
  * - [ ] Def U (Julia Angefangen)
  * - [ ] Def R
  * - [ ] Def AND
  * - [ ] Bei Definitionen abchecken ob auch längere funktionieren
  * - [ ] Verbesserung dass keine Strings sondern Objecte wirklich sind
