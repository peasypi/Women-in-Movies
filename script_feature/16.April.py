import re
from collections import Counter, defaultdict
#from sys import stdin
from pprint import pprint
import matplotlib.pyplot as plt

#Liest Script ein
f = open("/Users/Nils/MEGAsync/Dokumente/Uni/3. Semester/DH/IntroDH17/La_la_land_script.txt", "r")
script = f.read()

#bestimmt den gesprochenen Anteil
words_spoken = defaultdict(Counter)
currently_speaking = 'Narrator'

for line in script.split('\n'):
    name = line.replace('(CONT\'D)', '').strip()
    if re.match('^[A-Z]+$', name):
        currently_speaking = name
    else:
        words_spoken[currently_speaking].update(line.split())


pprint(words_spoken)

character1 = input("Enter name of character:")
character2 = input("Enter name of another character:")

sumchar1 = sum(words_spoken[character1].values())
sumchar2 = sum(words_spoken[character2].values())
#print(sum(words_spoken[character].values()))


#Diagramme

labels = [character1,character2]
values = [sumchar1,sumchar2]


word_counts = [sumchar1, sumchar2]
names = [character1, character2]
colors = ['r', 'y']
plt.pie(word_counts, labels=names, colors=colors, startangle=90, autopct='%.1f%%')
plt.title('Research on words spoken')
plt.show()

f.close()