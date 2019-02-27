import matplotlib.pyplot as plt
import re
import nltk


def words_spoken_total(script):
    spoken_text = ''

  # split the file into a list of strings, with each line a member in the list
    for line in script.split('\n'):

        # split the line into a list of words in the line
        words = line.split()

        # if there are no words, do nothing
        if not words:
            continue

        # if this line is a person identifier, do nothing
        if len(words[0]) > 1 and all([i.isupper() for i in words[0]]):
            continue

        # if there's a good amount of whitespace to the left, this is a spoken line
        if len(line) - len(line.lstrip()) > 10:
            spoken_text += line.strip() + ' '


    list1 = []
    spoken = nltk.word_tokenize(spoken_text)
    for i in spoken:
        if i.isalpha():
            list1.append(i)


    print(spoken)
    print(list1)
    return len(spoken)

script = """               
                         
                          JOHN
           Ted!
                         
                          TED
                          (RETARDED-SOUNDING VOICE)
           I'm alive, Johnny!
                         
                          JOHN
           Oh my god!
                         
                          (CONTINUED)
                          125
                         CONTINUED:
                         
                          TED
                          (RETARDED-SOUNDING VOICE)
           I'm alive! Your magical wish worked!
                         
                          JOHN
           You're back!
           """
print(words_spoken_total(script))

'''
dialog = words_spoken_total(script)

spoken_text = ""

words_spoken = defaultdict(Counter)
currently_speaking = 'Narrator'
speaking_people = []

for line in script.split('\n'):
    name = line.replace('(CONT\'D)', '').strip()
    if re.match('^[A-Z]+$', name):
        currently_speaking = name
        speaking_people.append(currently_speaking)
    else:
        words_spoken[currently_speaking].update(line.split())


character1 = input("Enter name of character:")
character2 = input("Enter name of another character:")
character3 = input("Character:")
character4 = input("Character:")

sumchar1 = sum(words_spoken[character1].values())
sumchar2 = sum(words_spoken[character2].values())
sumchar3 = sum(words_spoken[character3].values())
sumchar4 = sum(words_spoken[character4].values())
print(sumchar1)
print(sumchar2)
print(sumchar3)
print(sumchar4)
 

#Diagramme

labels = [character1,character2]
values = [sumchar1,sumchar2]
sonstige = dialog - sumchar1 - sumchar2 - sumchar3

word_counts = [sumchar1, sumchar2, sumchar3 , sonstige]
names = [character1, character2, character3, "Sonstige"]
colors = ['#b284be', '#e52b50', '#abcdef', '#848484']
plt.pie(word_counts, labels=names, colors=colors, startangle=90, autopct='%.1f%%')
plt.title('Research on words spoken')
plt.show()
pprint(set(speaking_people))
'''