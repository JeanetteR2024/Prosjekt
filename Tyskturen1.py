
# Regnskap tyskturen
import numpy as np
import matplotlib.pyplot as plt

#d = float(input("Hvor mange deltakere skal reise? ")) # deltakere/elever via input
#v = float(input("Hvor mange voksne skal reise? ")) # voksne via input

# deltakerliste med navn blir lest fra fil. Her hadde jeg litt hjelp av ki
with open("deltakerlisten.txt", "r", encoding="utf-8", errors="replace") as file:
    r = (file.readlines())
    with open("deltakerlisten.txt", "a", encoding="utf-8") as file:
        file.write("\n")
        print(f"Beregningen baserer seg paa {len(r)} deltakere.", file=file)
        print(f"Beregningen baserer seg på {len(r)} deltakere.")
r = len(r) #antall deltakere
    
budsjett = float(input("Hva er budsjettet ditt? (Alle priser angis i Euro.)"))  # budsjett input

#Reise/flybilletter
pris = 2500 # basert på gjennomsnittet
Flybilletter = pris * r

with open("deltakerlisten.txt", "a", encoding="utf-8") as file:
    file.write("\n")
    print("Flybillettene koster:", Flybilletter)  
    print("Flybillettene koster:", Flybilletter, file=file)  # skrives i fil deltakerlisten

#Transfer og transport
transferenkel = 4 #per person
transfer = 4 * r
transport = 35 * r
Transportkostnadene = transfer + transport

with open("deltakerlisten.txt", "a", encoding="utf-8") as file:
    print ("Transportkostnadene er:", Transportkostnadene)
    print ("Transportkostnadene er:", Transportkostnadene, file=file) # skrives i fil deltakerlisten

#Forpleining
lunsjenkel = 50 #per person
middagenkel = 100 #per person
lunsj = 50 * r
middag = 100 * r
forpleining = lunsj + middag

with open("deltakerlisten.txt", "a", encoding="utf-8") as file:
    print ("Forpleiningskostnadene er:", forpleining)
    print ("Forpleiningskostnadene er:", forpleining, file=file) # skrives i fil deltakerlisten

# Utregning av totalsummen 
Total = Flybilletter + Transportkostnadene + forpleining

with open("deltakerlisten.txt", "a", encoding="utf-8") as file:
    print("Totalsummen er:", Total)
    print("Totalsummen er:", Total, file=file) # skrives i fil deltakerlisten

# Utregning av forholdet mellom kostnadene og budsjett
if budsjett > Total:
    rest = budsjett - Total
    print("Du har", rest, "igjen.")
elif budsjett == Total:
    print("Budsjettet dekker akkurat utgiftene.")
else:
    rest = Total - budsjett
    print("Du ligger over budsjettet med", rest, "Euro.")
    
# Omregning til Euro etter aktuelt kurs (hjelp av en venn) https://pypi.org/project/CurrencyConverter/
from currency_converter import CurrencyConverter
c = CurrencyConverter()
rundet = round(c.convert(Total, 'EUR', 'NOK'), 2)

with open("deltakerlisten.txt", "a", encoding="utf-8") as file:
    print("Dette er ", rundet, "Kroner.")
    print("Dette er ", rundet, "Kroner.", file=file)
    
# Utregning av totalsummen med en funksjon, basert på en reisetid på 5 dager
def totalsum(x):
    f = 2500  # pris flybilletter per person
    t = 39   # pris transport per person per dag
    m = 150   # pris forpleining per person per dag
    d = 5     # antall dager
    return x * d * (t + m) + (x * f) 
        
deltakere = [5, 10, 15, 20, 25] #liste
     
for x in deltakere: #for løke
   resultat = totalsum(x)
   print(f"Antall deltakere: {x}, Totalkostnad: {resultat}")
    
#Plotting, visuell fremstilling for 1 - 25 deltakere
xdeltakere = np.arange(1, 25)
ytotal = xdeltakere * (pris + lunsjenkel + middagenkel + transferenkel)
ypoints = budsjett #fast sum

breakpoint = None #beregning av max antall deltakere i forhold til budsjettet
for i, total in enumerate(ytotal):
    if total >= budsjett:
        breakpoint = xdeltakere[i]
        break
    
if breakpoint:
    plt.plot(breakpoint, ytotal[breakpoint - 1], 'ro', markersize=8, label=f"Budget erreicht bei {breakpoint} TN")
    print(breakpoint - 1, "deltakere kan være med på turen.")
    print("Prisen for turen med", breakpoint - 1, "deltakere blir deretter", (breakpoint - 1) * (pris + lunsjenkel + middagenkel + transferenkel))

plt.plot(xdeltakere, ytotal)
plt.plot(xdeltakere, [budsjett] * len(xdeltakere), linestyle="--", color="r", label="Budget")

  

    
