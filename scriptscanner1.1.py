from nltk.tokenize import word_tokenize
import docx


f = open("C:/Users/Piasu/Desktop/dhprojekt/djangounchained.txt", "r")
s = open("C:/Users/Piasu/Desktop/dhprojekt/djangounchained2.txt", 'w')

script = f.read()

def klammernloeschen (str):
    klammerauf = str.find('(')
    klammerzu = str.find(')')


    while (klammerauf != -1 and klammerzu != -1):

            if (klammerauf<klammerzu):
                str = str[:klammerauf] + str[klammerzu+1:]

            klammerauf = str.find('(')
            klammerzu = str.find(')')
    s.write(str)

    return;

klammernloeschen(script)

s.close()

s = open("C:/Users/Piasu/Desktop/dhprojekt/djangounchained2.txt", 'r')

script = s.read()


def sprechanteil(script, name):

    a = 0
    e = 0
    all = 0
    while(a != -1 and e != -1):

        a = script.find(name+'\n           ') + len(name)
        temp = script[a:]
        e = temp.find(' \n')
        texttom = temp[:e]
        #print(texttom)
        texttomlist = word_tokenize(texttom)
        #print(texttomlist)

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
            return list;

        removing(texttomlist)

        #print(texttomlist)

        def countingwords(list):
            woerter = 0
            for i in list:
                woerter = woerter+1
            return woerter;


        mehr = countingwords(texttomlist)
        #print(mehr)

        all = all + mehr

        script = script[a+e:]
        a = script.find(name +'\n           ')
        temp = script[a:]
        e = temp.find(' \n')

    print(name + " sagt " + str(all) + " Wörter.")

f.close()

name = input("Gib einen Namen ein:")
sprechanteil(script, name)
name1 = input("Gib einen weiteren Namen ein:")
sprechanteil(script, name1)
if input("Weiterer Name?") == 'y':
    name2 = input("Gib einen weiteren Namen ein:")
    sprechanteil(script, name2)
