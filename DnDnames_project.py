#Program do generowania imion DnD

#Założenia projektu:
#Projekt ma na celu utrwalenie podstaw i używania Data Structures, niektóre rozwiązania mogą nie być najbardziej optymalne tylko po to aby przećwiczyć jakieś zagadnienie, możliwe że po osiągnięciu moich celów będę go optymalizował.

#1 Otwiera liste
#2 Zależnie od inputu podaje x liczbe imion
#3 Mogę zrobić warunki które przyporządkuje do danej grupy imion, potem na podstawie inputy zostaną zrzucone imiona dla konkretnej rasy
#Na jutro stworzyć pustą listę English, Name i dodać warunek pod if który będzie dodawał do niej imiona
#usunąć z imion puste miejsca
#4 regex dla praktyki a może i uproszczenia kodu

import re
import random

name = input("Enter File") #W przyszłości zmiana na automatyczne otwarcie pliku
if len(name) < 1:
    name = 'Names_list.txt'

opener = open(name)
count = 0
limit = 300
race_dict = {}
current_key = None

for line in opener:
    line = line.strip()
    if line.startswith(('Dwarf,','Chondatian,','Illuskan','Chultan','Half-Orc','Tiefling','Halfing','Gnome','Elf','Dragonborn')):
        current_key, value = line.split(', ')
        current_key = line
        race_dict[current_key] = []
    elif current_key:
        race_dict[current_key].append(line)
        print(race_dict)


race = input('Enter D&D(phb) race:')
if race.lower() not in ['human', 'dwarf']: #dopisać reszte ras
    raise ValueError('Please enter correct race name')

if race == 'human':
    nation = input('Enter human nationality, example luskan')
    race = nation.lower()
    if race not in ['luskan', 'calimshan']: #wszystkie narodowości
        raise ValueError('Please enter correct nation name')

gender = input('Select gender M for male F for female:')
if gender.lower() not in ['M', 'm', 'F', 'f']: #czy potrzebuje zaznaczać duże M i F?
    raise ValueError('please enter correct gender')


#Human names
#
# if race.lower() in ['luskan'] and gender.lower() in ['m']:
#     for line in opener:
#         line = line.rstrip()
#         if not line.startswith ('English, Male') : continue
#         stuff = line.split()
#         randomname = random.choice(stuff)
#         print(randomname)
#         count += 1
#         if count == limit:
#             break

# if race.lower() in ['luskan'] and gender.lower() in ['f']:
#     for line in opener:
#         line = line.rstrip()
#         if not line.startswith ('English, Female') : continue
#         stuff = line.split()
#         randomname = random.choice(stuff)
#         print(randomname)
#         count += 1
#         if count == limit:
#             break
#
# #Dwarf names

if race.lower() in ['dwarf'] and gender.lower() in ['m']:
    if 'Dwarf, Male' in race_dict:
        availableopt = race_dict['Dwarf, Male']
        if len(availableopt) >= limit:
            randomname = random.sample(availableopt, limit)
            for name in randomname:
                print(name)
        else:
            print("Limit above of available name options, please find all available names for this race:", availableopt)
    # nameoptions = race_dict['Dwarf, Male']
    
if race.lower() in ['dwarf'] and gender.lower() in ['m']:
    if 'Dwarf, Male' in race_dict:
        availableopt = race_dict['Dwarf, Female']
        if len(availableopt) >= limit:
            randomname = random.sample(availableopt, limit)
            for name in randomname:
                print(name)
            else:
                print("Limit above of available name options, please find all available names for this race:",
                      availableopt)




    # for line in opener:
    #     line = line.rstrip()
    #     if not line.startswith ('Dwarf, Male') : continue
    #     stuff = line.split()
    #     randomname = random.choice(stuff)
    #     print(randomname)
    #     count += 1
    #     if count == limit:
    #         break

# if race.lower() in ['dwarf'] and gender.lower() in ['f']:
#     for line in opener:
#         line = line.rstrip()
#         if not line.startswith ('Dwarf, Female') : continue
#         stuff = line.split()
#         randomname = random.choice(stuff)
#         print(randomname)
#         count += 1
#         if count == limit:
#             break