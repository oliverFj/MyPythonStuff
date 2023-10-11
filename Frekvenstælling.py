
# Dictionaries for Frequency Count
# Frekvenstælling

#funktion der modtager to ord - strenge - og returnerer True hvis de er anagrammer, False ellers
def er_det_et_anagram(ord1, ord2):

    #hvis længden af ordene er forskellige, er de ikke anagrammer
    #så vi kan bruge 2 dictonaries(værdiindekseer) til at tælle bogstaverne i hvert ord
    #og hvis de er ens, så ved vi at det et anagram. 

    #Vi kaldere dem:
    bogstavsværdiindeks_1 = {}
    bogstavsværdiindeks_2 = {}

    
    #Nu tager vi alle bogstaverene i ord1, og ligger dem ind i vores første dictionary(værdiindeks)

    #Hvis(if) bogstavet allerede findes i dictionarien(værdiindekset), så hopper vi videre til (else)
    #Inde hos else, så laver vi en ny "key" med bogstavet, og sætter "value" til 1
    #Dictonary[Key] = Value

    #På den måde, når programmet ser et bogstav der er der i forvejen, så kommer den ind i if, og
    #så plusser den værdien der er der i forvejen, med 1


    for bogstav in ord1:
        if bogstav in bogstavsværdiindeks_1:
            bogstavsværdiindeks_1[bogstav] += 1
        else:
            bogstavsværdiindeks_1[bogstav] = 1

    #så copy paster vi overstående, og ændrer ord1 til ord2, og bogstavsværdiindeks_1 til bogstavsværdiindeks_2        

    for bogstav in ord2:
        if bogstav in bogstavsværdiindeks_2:
            bogstavsværdiindeks_2[bogstav] += 1
        else:
            bogstavsværdiindeks_2[bogstav] = 1

    #nu har vi to dictionaries, med bogstaverne fra ord1 og ord2, og hvor mange gange hvert ord forekommer
    #med vores sidste trylleord (return) så sammenligner vi de to dictionaries
    # == betyder "er lig med", og hvis de er, er det et anagram, og vi returnerer True, ellers False

    return bogstavsværdiindeks_1 == bogstavsværdiindeks_2

#indsæt ordene her:
print (er_det_et_anagram("blabla", "lablab"))


# Frekvenstælling

def er_det_et_anagram(ord1, ord2):

    bogstavsværdiindeks_1 = {}
    bogstavsværdiindeks_2 = {}

    for bogstav in ord1:
        if bogstav in bogstavsværdiindeks_1:
            bogstavsværdiindeks_1[bogstav] += 1
        else:
            bogstavsværdiindeks_1[bogstav] = 1

    for bogstav in ord2:
        if bogstav in bogstavsværdiindeks_2:
            bogstavsværdiindeks_2[bogstav] += 1
        else:
            bogstavsværdiindeks_2[bogstav] = 1

    return bogstavsværdiindeks_1 == bogstavsværdiindeks_2

print (er_det_et_anagram("blabla", "lablab"))
