from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

def klammernloeschen (str):
    klammerauf = str.find('(')
    klammerzu = str.find(')')

    while (klammerauf != -1 and klammerzu != -1):

        if(klammerauf<klammerzu):
            str = str[:klammerauf] + str[klammerzu+1:]


        klammerauf = str.find('(')
        klammerzu = str.find(')')
    print(str)
    return


def get_script(str):
    my_url = str
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
            #find_all_b = page_soup.find_all(re.compile("b"))

    text = page_soup.get_text()



    #print(text)
    return text


'''klammernloeschen(script)

i = 0
for t in script:
    if '/n' in script:
        i += 1
'''


script = get_script(input("Gib die URL des zu bearbeitenden Films ein:"))
text=''
for lines in script.splitlines(True):
    if lines.startswith("           "):
        text=text+lines
        print(text)


print(klammernloeschen(text))        