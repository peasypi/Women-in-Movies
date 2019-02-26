from functionProgramm import *

firstInput = 0
secondInput = 0
notCorrect = True
links = []

print("Welcome to this little programm :)")

while notCorrect:
    firstInput = int(input("Do you want to gather information about the most popular movies of a certain time span [1] or from a certain number of movies, orderd by succes [2]"))
    notCorrect = False
    if not(firstInput == 1 or 2):
        print("Please enter 1 or 2!")
        notCorrect = True

if firstInput == 2:
    getMovies(getJSON(linksPopularityCreater()))

elif firstInput == 1:
    links = linksYearCreater()

    notCorrect = True

    while notCorrect:
        secondInput = int(input("Do you want to get CSV files, which include the gender ratio for important crew-jobs [1] or a text file, which includes all collected movies [2] or both [3]"))
        notCorrect = False
        if not(secondInput == 1 or 2 or 3):
            print("Please enter 1,2 or 3!")
            notCorrect = True

    ids = getJSON(links)

    if secondInput == 1:
        getCrew(ids)

    elif secondInput == 2:
        getMovies(ids)

    elif secondInput == 3:
        getCrew(ids)
        getMovies(ids)










