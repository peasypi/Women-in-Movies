# Import of the required packages
import json
import urllib
from urllib.request import urlopen

# This function returns URLs (for the "theMovieDB"-API) for all movie of an user given time span
def linksYearCreater():
	# "s" is the complete URL to get the 20 most succesful movies of a certan year, without the year
    s = "https://api.themoviedb.org/3/discover/movie?api_key=0ae744d3523ac83c17788b462e1af745&sort_by=revenue.desc&include_adult=false&include_video=false&page=1&primary_release_year="
    linksWithYears =[]
    startYear = "a"

    print("We will always collect the 20 most succesful movies of each year.\n")

	# This while loop gets the start year from the user. The variable startYear is initially set to "a". With a try block, we catch ValueError's (because of the "int"-function, every input which is not an int will generate a Value Error).
    while startYear == "a":
        try:
            startYear = int(input("Please enter the start year:"))
        except ValueError:
            print("Please enter an integer")

    endYear = "a"

	# It's the same routine, like with the start year. Only that we catch (with an if-clause) the case, that the end year is lower than the start year.
    while endYear == "a":
        try:
            endYear = int(input("Please enter the end year:"))
            if endYear < startYear:
                print("The end year has to be lower than the start year. Please try again :)")
                endYear = "a"
        except ValueError:
            print("Please enter an integer")

	# Now we append all the links (we put together the basic link from "s" and all the years from start to end year) to the list "linksWithYears", which gets returned afterwards
    while startYear < endYear+1:
        number = str(startYear)
        linksWithYears.append(s + number)
        startYear += 1

    return linksWithYears

# This function creates the links, for the most succesful movies. It works pretty similar to the linksYearCreater-function. The only main difference is, that the links get put together with the page number
	# TheMovieDB-API can return always 20 movies on one page. So if we want to get the 20 most succesful movies, we get only page 1. If we want to get the 80 most succesful movies, we get pages 1,2,3 and 4.
	# Out of simplicity, we decided to don't do anything about the situation, that you can only choose a number dividible by 20. For a project/programm, which is supposed to go public, we would have considered our decision, but this progamm is for research-purposes only.
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

# This function gets the "TheMovieDB"-ids for movies on API pages.
# As parameters you can put in lists, which include links for API pages which, on the other hand, include movie-lists in the JSON-format
# The output is a list with all movie ids.
def getJSON(links):

    ids = []

    for x in links:
        with urlopen(x) as url:
            response = urlopen(x)
            values = json.load(response)

        for i in range(0, len(values['results'])):
            ids.append(values['results'][i]['id'])

    return ids

# This function creates a txt-file, based on a list with API movie ids, with a list of all names with their link to the movieDB
def getMovies(ids):

	# temp is to check, if there are duplicates
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
            print("")

        except urllib.error.URLError:
            print("")

        name = values['title']

        names.write("{0} --> https://www.themoviedb.org/movie/{1}\n".format(values['title'], idLink))

    print("We createt a text file called \"movieNames.txt\" with your chosen movies.")

# This function creates 5 csv files (director, screenplay, editor, producer, directirOfPhotography), which include (for each profession) a table with a proportion of gender, divided by release-year
# As parameter, the function works only with list which include movie ids, which are sorted uprising by year, and with always 20 movies per year, without one year missing
# That's because of the way the MovieDB works. Here again it would be possible to change that, but we decided against it, because it would need way more system-recources and at that point, the only people who are using the programm, can look in the comments.
# If we would think about releasing the programm, we definitely would do some changes in this part.
def getCrew(ids):
	# We create all the needed files and allready write the first line of the csv-table
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


	# We get the API link for the first index of the entered link to get the release year, of the first movie.
    linkFirstYear = "https://api.themoviedb.org/3/movie/" + str(ids[0]) + "?api_key=0ae744d3523ac83c17788b462e1af745"

    try:
        with urlopen(linkFirstYear) as url:
            response = urlopen(linkFirstYear)

        valuesFirstYear = json.load(response)

    except urllib.error.HTTPError:
            print("")

    except urllib.error.URLError:
            print("")

	# We get the JSON-value which includes the release date, but because it's in the "YYYY-MM-DD"-format, we split the returned string and parse it afterwards to an integer.
    year = valuesFirstYear["release_date"]
    year = int(year[0:4])

    x = 0
	# All these variable are counters for the gender ratio and get added 1, if a crew member, with the specific job and gender gets found.
    directorW = editorW = producerW = screenplayW = directorOfPhotographyW = 0
    directorM = editorM = producerM = screenplayM = directorOfPhotographyM = 0
    directorN = editorN = producerN = screenplayN = directorOfPhotographyN = 0

	# This for loop goes through all the entered links. Another for loop, goes through the results of every movie.
    for j in ids:
		# x is to count. Every time it's dividible by 20, we now we can change the year-variable
        x += 1
        idLink = str(j)
		# This link is the basic construct for a link, which includes al the credits of a movie
        link = "https://api.themoviedb.org/3/movie/" + idLink + "/credits?api_key=0ae744d3523ac83c17788b462e1af745"

        try:
            with urlopen(link) as url:
                response = urlopen(link)

            values = json.load(response)

        except urllib.error.HTTPError:
            print("")

        except urllib.error.URLError:
            print("")

		# This for loop goes through the whole crew part of the credits.
		# It basicaly goes through every job. Every time one of our determined jobs gets found, the int for the found gender gets added 1.
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

		# when x reaches a number dividible by 20, the results get writen in to the csv-files and the different job-gender-counter get set back to zero.
		# the year-variable gets added 1 and the for loop goes again.
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