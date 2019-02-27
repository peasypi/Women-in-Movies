import nltk


f = open("/Users/pia/Desktop/Uni/IntroToDH/Women_in_movies/LaLaLand.txt", "r")
s = open("/Users/pia/Desktop/Uni/IntroToDH/Women_in_movies/women-in-movies/scripts/LaLaLand-versuch.txt", 'w')

script = f.read()

def klammernloeschen (str):
    klammerauf = str.find('(')
    klammerzu = str.find(')')


    while (klammerauf != -1 and klammerzu != -1):

            if (klammerauf<klammerzu):
                str = str[:klammerauf] + str[klammerzu+1:]

            klammerauf = str.find('(')
            klammerzu = str.find(')')

    return str;

#Sprechanteil 
def sprechanteil(script, name):

    a = 0
    e = 0
    all = 0
    #while-Schleife .. weiter machen bis Name nicht mehr gefunden
    while(a != -1 and e != -1):

        a = script.find(name+'\n           ') + len(name)
        temp = script[a:]
        e = temp.find(' \n')
        text = temp[:e]
        #print(text)
        
        #Text in Liste von Woertern spliten
        textlist = nltk.word_tokenize(text)
        #print(textlist)
        
        #Satzzeichen aus List entfernen
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

        removing(textlist)

        def countingwords(list):
            woerter = 0
            for i in list:
                woerter = woerter+1
            return woerter;


        mehr = countingwords(textlist)
        #print(mehr)

        all = all + mehr

        script = script[a+e:]
        a = script.find(name +'\n           ')
        temp = script[a:]
        e = temp.find(' \n')

    print(name + " sagt " + str(all) + " Woerter.")


klammernloeschen(script)

name = input("Gib einen Namen ein:")
sprechanteil(script, name)
name1 = input("Gib einen weiteren Namen ein:")
sprechanteil(script, name1)
if input("Weiterer Name?") == 'y':
    name2 = input("Gib einen weiteren Namen ein:")
    sprechanteil(script, name2)
