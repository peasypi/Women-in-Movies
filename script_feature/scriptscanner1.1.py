from nltk.tokenize import word_tokenize
#from re import match
import codecs

#f = open("/Users/Nils/MEGAsync/Dokumente/Uni/3. Semester/DH/IntroDH17/La_la_land_script.txt", "r")
#script = f.read()

def klammernloeschen (str):
    klammerauf = str.find('(')
    klammerzu = str.find(')')


    while (klammerauf != -1 and klammerzu != -1):

            if (klammerauf<klammerzu):
                str = str[:klammerauf] + str[klammerzu+1:]

            klammerauf = str.find('(')
            klammerzu = str.find(')')
    return str



# script.txt contains the sample text you posted
with codecs.open('/Users/Nils/MEGAsync/Dokumente/Uni/3. Semester/DH/IntroDH17/La_la_land_script.txt', 'r', 'utf8') as f:

  # read the file content
  f = f.read()

  # store all the clean text that's accumulated
  spoken_text = ''

  # split the file into a list of strings, with each line a member in the list
  for line in f.split('\n'):

    # split the line into a list of words in the line
    words = line.split()

    # if there are no words, do nothing
    if not words:
      continue

    # if this line is a person identifier, do nothing
    if len(words[0]) > 1 and all([i.isupper() for i in words[0]]):
      continue

    # if there's a good amount of whitespace to the left, this is a spoken line
    if len(line) - len(line.lstrip()) > 4:
      spoken_text += line.strip() + ' '

print(spoken_text)
def removing(list):
    for i in list:
        if i == '?':
            list.remove('?')
        if i == '!':
            list.remove('!')
        if i == '.':
            list.remove('.')
        if i == ',':
            list.remove(',')
        if i == '...':
            list.remove('...')
        if i == '--':
            list.remove('--')
    return list


def countingwords(list):
    woerter = 0
    for i in list:
        woerter = woerter + 1
    return woerter;

#script = klammernloeschen(script)
#print(script)

#result = match(r"\w[A-Z]+\n\s).+?(?=\n",script)
#print (result)
'''
def sprechanteil(script, name):

    a = 0
    e = 0
    all = -len(name)-1

    if script.find(name)==-1:
        print("Dieser Charakter sagt in diesem Script nichts")
    else:
        while(a != -1 and e != -1):

            a = script.find(name+'\n            ') + len(name)
            print(a)
            temp = script[a:]
            t = temp.split("\n")
            #e = temp.find(' \n')
            text = t[1]
            #temp[:e]
            print(text)
            textlist = word_tokenize(text)
            #print (textlist)

            removing(textlist)

            #print(textlist)

            mehr = countingwords(textlist)
            #print(mehr)

            all = all + mehr

            script = script[a+e:]
            a = script.find(name +'\n           ')
            temp = script[a:]
            e = temp.find(' \n')

    print(name + " sagt " + str(all) + " Wörter.")
'''


#print(script.find("Pia"))
name = input("Gib einen Namen ein:")
sprechanteil(script, name)
name1 = input("Gib einen weiteren Namen ein:")
sprechanteil(script, name1)
if input("Weiterer Name?") == 'y':
    name2 = input("Gib einen weiteren Namen ein:")
    sprechanteil(script, name2)
