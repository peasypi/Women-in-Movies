import codecs

# script.txt contains the sample text you posted

def klammernloeschen (str):
    klammerauf = str.find('(')
    klammerzu = str.find(')')


    while (klammerauf != -1 and klammerzu != -1):

            if (klammerauf<klammerzu):
                str = str[:klammerauf] + str[klammerzu+1:]

            klammerauf = str.find('(')
            klammerzu = str.find(')')
    return str


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
        if i == 'Revision':
            list.remove('Revision')

    return list


def countingwords(list):
    woerter = 0
    for i in list:
        woerter = woerter + 1
    return woerter;


with codecs.open("/Users/Nils/MEGAsync/Dokumente/Uni/3. Semester/DH/IntroDH17/La_la_land_script.txt", 'r', 'utf8') as f:

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
    if len(line) - len(line.lstrip()) > 8:
      spoken_text += line.strip() + ' '
    spoken_text1 = klammernloeschen(spoken_text)



print(spoken_text1)