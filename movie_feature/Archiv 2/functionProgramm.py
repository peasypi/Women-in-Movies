import json
import urllib
from urllib.request import urlopen

def linksYearCreater():
    s = "https://api.themoviedb.org/3/discover/movie?api_key=0ae744d3523ac83c17788b462e1af745&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year="
    linksWithYears =[]
    startYear = "a"

    print("We will always collect the 20 most succesful movies of each year.\n")

    while startYear == "a":
        try:
            startYear = int(input("Please enter the start year:"))
        except ValueError:
            print("Please enter an integer")

    endYear = "a"

    while endYear == "a":
        try:
            endYear = int(input("Please enter the end year:"))
            if endYear < startYear:
                print("The end year has to be lower than the start year. Please try again :)")
                endYear = "a"
        except ValueError:
            print("Please enter an integer")

    while startYear < endYear+1:
        number = str(startYear)
        linksWithYears.append(s + number)
        startYear += 1

    return linksWithYears

def linksPopularityCreater():

    s = "https://api.themoviedb.org/3/discover/movie?api_key=0ae744d3523ac83c17788b462e1af745&language=en-US&sort_by=revenue.desc&include_adult=false&include_video=false&page="
    i = 1
    notCorrect = True
    a = 0
    out = []


    while notCorrect:
        a = int(input("Please enter a number divisble by 20, which is at least 20:"))
        notCorrect = False
        if a < 20 or not(a % 20 == 0):
            notCorrect = True

    a /= 20

    while i <= a:
        number = str(i)
        out.append(s + number)
        i += 1

    return out

def getJSON(links):

    ids = []

    for x in links:
        with urlopen(x) as url:
            response = urlopen(x)
            values = json.load(response)

        for i in range(0, len(values['results'])):
            ids.append(values['results'][i]['id'])

    return ids

def getMovies(ids):

    temp = ""
    names = open("movieNames.txt", "w")


    for i in ids:
        if i == temp:
            continue

        temp = i

        idLink = str(i)
        link = "https://api.themoviedb.org/3/movie/" + idLink + "?api_key=0ae744d3523ac83c17788b462e1af745"

        try:
            with urlopen(link) as url:
                response = urlopen(link)

            values = json.load(response)

        except urllib.error.HTTPError:
            print("A")

        except urllib.error.URLError:
            print("B")

        name = values['title']

        names.write("{0} --> https://www.themoviedb.org/movie/{1}\n".format(values['title'], idLink))

    print("We createt a text file called \"movieNames.txt\" with your chosen movies.")

def getCrew(ids):
    director = open("director.csv", "w")
    director.write("Year, female, male, null")
    screenplay = open("screenplay.csv", "w")
    screenplay.write("Year, female, male, null")
    editor = open("editor.csv", "w")
    editor.write("Year, female, male, null")
    producer = open("producer.csv", "w")
    producer.write("Year, female, male, null")
    directorOfPhotography = open("directorOfPhotography.csv", "w")
    directorOfPhotography.write("Year, female, male, null")



    linkFirstYear = "https://api.themoviedb.org/3/movie/" + str(ids[0]) + "?api_key=0ae744d3523ac83c17788b462e1af745"

    try:
        with urlopen(linkFirstYear) as url:
            response = urlopen(linkFirstYear)

        valuesFirstYear = json.load(response)

    except urllib.error.HTTPError:
            print("")

    except urllib.error.URLError:
            print("")

    year = valuesFirstYear["release_date"]
    year = int(year[0:4])

    x = 0
    directorW = editorW = producerW = screenplayW = directorOfPhotographyW = 0
    directorM = editorM = producerM = screenplayM = directorOfPhotographyM = 0
    directorN = editorN = producerN = screenplayN = directorOfPhotographyN = 0

    for j in ids:
        x += 1
        idLink = str(j)
        link = "https://api.themoviedb.org/3/movie/" + idLink + "/credits?api_key=0ae744d3523ac83c17788b462e1af745"

        try:
            with urlopen(link) as url:
                response = urlopen(link)

            values = json.load(response)

        except urllib.error.HTTPError:
            print("")

        except urllib.error.URLError:
            print("")

        for i in range(0, len(values['crew'])):

            if (values['crew'][i]['job'] == "Director"):
                if (values['crew'][i]['gender'] == 1):
                    directorW += 1
                if (values['crew'][i]['gender'] == 2):
                    directorM += 1
                else:
                    directorN += 1

            if (values['crew'][i]['job'] == "Writer"):
                if (values['crew'][i]['gender'] == 1):
                    screenplayW += 1
                if (values['crew'][i]['gender'] == 2):
                    screenplayM += 1
                else:
                    screenplayN += 1

            if (values['crew'][i]['job'] == "Screenplay"):
                if (values['crew'][i]['gender'] == 1):
                    screenplayW += 1
                if (values['crew'][i]['gender'] == 2):
                    screenplayM += 1
                else:
                    screenplayN += 1

            if (values['crew'][i]['job'] == "Producer"):
                if (values['crew'][i]['gender'] == 1):
                    producerW += 1
                if (values['crew'][i]['gender'] == 2):
                    producerM += 1
                else:
                    producerN += 1

            if (values['crew'][i]['job'] == "Editor"):
                if (values['crew'][i]['gender'] == 1):
                    editorW += 1
                if (values['crew'][i]['gender'] == 2):
                    editorM += 1
                else:
                    editorN += 1

            if (values['crew'][i]['job'] == "Director of Photography"):
                if (values['crew'][i]['gender'] == 1):
                    directorOfPhotographyW += 1
                if (values['crew'][i]['gender'] == 2):
                    directorOfPhotographyM += 1
                else:
                    directorOfPhotographyN += 1

        if x % 20 == 0:
            director.write("\n")
            director.write("{0}, {1}, {2}, {3}".format(year, directorW, directorM, directorN))
            editor.write("\n")
            editor.write("{0}, {1}, {2}, {3}".format(year, editorW, editorM, editorN))
            producer.write("\n")
            producer.write("{0}, {1}, {2}, {3}".format(year, producerW, producerM, producerN))
            screenplay.write("\n")
            screenplay.write("{0}, {1}, {2}, {3}".format(year, screenplayW, screenplayM, screenplayN))
            directorOfPhotography.write("\n")
            directorOfPhotography.write("{0}, {1}, {2}, {3}".format(year, directorOfPhotographyW, directorOfPhotographyM, directorOfPhotographyN))
            directorW = editorW = producerW = screenplayW = directorOfPhotographyW = 0
            directorM = editorM = producerM = screenplayM = directorOfPhotographyM = 0
            directorN = editorN = producerN = screenplayN = directorOfPhotographyN = 0
            year += 1

    director.close()
    editor.close()
    producer.close()
    screenplay.close()
    directorOfPhotography.close()

    print("The CSV-files were created succesfully.")