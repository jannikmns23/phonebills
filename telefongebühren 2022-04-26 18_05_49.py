#Willkommen
grundgebühr = 7
kosten_gesprächseinheit = 0.23
kostenlose_gesprächseinheiten = 20
print("Willkommen bei der deutschen Telekom. Schön dass Sie sich für unserern Service entschieden haben, denn der von 1und1 ist scheiße. Unsere monatliche Grundgebühr beträgt", grundgebühr, " Euro und Sie erhalten damit", kostenlose_gesprächseinheiten, "Gesprächseinheiten kostenlos. Jede weitere Gesprächseinheit kostet Sie", kosten_gesprächseinheit, " Euro. Bitte geben die Anzahl der von Ihnen in diesem Monat getätigten Gesprächseinheiten an:")

gesprächseinheiten = input()
gesprächseinheiten = int(gesprächseinheiten)

if (gesprächseinheiten <=20):
    print("Für Sie fallen diesen Monat nur", grundgebühr, "Euro Telefongebühren an.")

if (gesprächseinheiten >20):
    gesamtgebühren = grundgebühr+(gesprächseinheiten-20)*kosten_gesprächseinheit
    print("Für Sie fallen diesen Monat", gesamtgebühren, "Euro Telefongebühren an.")




