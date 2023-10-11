"""

def is_anagram(word1, word2):
    wordOneList = list(word1)
    wordTwoList = list(word2)

    for letter in wordOneList:
        if letter not in wordTwoList:
            print ("Letter!")
            return False
    print ("ANAGRAM!")
    return True


is_anagram("hej", "deh")


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
        if bogstav in letter_dict2:
            bogstavsværdiindeks_2[bogstav] += 1
        else:
            bogstavsværdiindeks_2[bogstav] = 1

    #nu har vi to dictionaries, med bogstaverne fra ord1 og ord2, og hvor mange gange hvert ord forekommer
    #med vores sidste trylleord (return) så sammenligner vi de to dictionaries
    # == betyder "er lig med", og hvis de er, er det et anagram, og vi returnerer True, ellers False

    return bogstavsværdiindeks_1 == bogstavsværdiindeks_2

#indsæt ordene her:
print (er_det_et_anagram("blabla", "lablab"))



# Dictionary for Grouping
# Gruppering

def organize_travels(travel_list):
    # Create a dictionary to store the years Grandpa visited each country
    travel_dict = {}

    # Iterate through the list of travels
    for entry in travel_list:
        # Split each entry into country and year
        country, year = entry.split(" ")

        # Update the dictionary
        if country in travel_dict:
            travel_dict[country].append(year)
        else:
            travel_dict[country] = [year]

    # Sort the years for each country and print the results
    for country, years in travel_dict.items():
        sorted_years = sorted(years)
        print(f"{country} {' '.join(sorted_years)}")

# Test the function
grandpa_travels = ['Iceland 2016', 'Sweden 2015', 'Iceland 1982', 'Norway 1999', 'Iceland 2000']
organize_travels(grandpa_travels)



students = {
    'Engineering': [3.5, 3.7, 3.8],
    'Arts': [3.2, 3.9, 3.6]
}
for department, grades in students.items():
    sorted_grades = sorted(grades)
    print(f"{department}: {sorted_grades}")

"""

def er_det_et_anagram(word1, word2):

    værdiindeks_1 = {}
    værdiindeks_2 = {}

    for letter in word1:
        if letter in værdiindeks_1:
            værdiindeks_1[letter] += 1
        else:
            værdiindeks_1[letter] = 1

    for letter in word2:
        if letter in værdiindeks_2:
            værdiindeks_2[letter] += 1
        else:
            værdiindeks_2[letter] = 1 

    return værdiindeks_1 == værdiindeks_2

print (er_det_et_anagram("hej", "jeh"))