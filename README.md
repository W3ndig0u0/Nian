# Nian

Uppgiften
Uppgiften går ut på att skriva ett Python-program som löser Nian. Som ordbok ska användas en egen förteckning av ord som finns på samma ställe som denna text på filen svenskaOrd.txt. Obs att denna fil är mycket mindre omfattande än SAOL så en del ord kommer ditt program inte att hitta.
Programmet ska läsa in pusslet som en sträng på nio bokstäver, där den mittersta bokstaven är den speciella som ska finnas med i varje lösning. Inmatningen ska kontrolleras, om den är kortare än 4 bokstäver eller längre än 9 bokstäver ska ett felmeddelande skrivas ut:
Fel: för få bokstäver, försök igen!
resp.
Fel: för många bokstäver, försök igen!
Inmatningen ska upprepas tills godkänd inmatning har givits.
Sedan ska programmet skriva ut alla lösningar det hittar, lösningarna ska presenteras med ett ord per rad i alfabetisk ordning.
Därefter ska det komma en utskrift om hur många lösningar som använder alla nio bokstäver och så en lista på dessa ord.
Exempel på programdialogen (användarens inmatning i svart):
Nian: anitsksem
anemisk
anis
anse
ansikte
... (många andra ord borttagna från utskriften av utrymmesskäl) stam
stank
stek
steka
sten
stena
stim
stinka
2 ord använder alla bokstäver:
misstanke
semantisk
Om det inte hittas några ord som uppfyller kriterierna ska programmet skriva ut:
Hittade inga ord alls.
I så fall ska ingen utskrift om ord som använder alla nio bokstäver komma.
Om det finns ord som uppfyller kriterierna, men inga som använder alla nio bokstäver, ska utskriften om ord som använder alla nio bokstäver vara:
Det finns inga ord som använder alla bokstäver.
