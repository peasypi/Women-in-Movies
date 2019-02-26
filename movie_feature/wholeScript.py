# Import of the other Python Script, which includes all the relevant functions
from functionProgramm import *

# Different essential variables, which are gonna be explained in the process
firstInput = 0
secondInput = 0
notCorrect = True
links = []

print("Welcome to this little programm :)")

# This while-loop goes on and on, until the user enters the correct input (1 or 2).
# the "notCorrect"-variable was earlier declared as boolean "True", that's what keeps the while-loop running
# after the user puts in a value, the "notCorrect"-variable gets set on False, but if the input is not what we want, we put it on False again.
while notCorrect:
    firstInput = int(input("Do you want to gather information about the most popular movies of a certain time span [1] or from a certain number of movies, orderd by succes [2]"))
    notCorrect = False
    if not(firstInput == 1 or 2):
        print("Please enter 1 or 2!")
        notCorrect = True

# if the User choces Option 2, we start a bunch of functions, which work together as parameter in a classical way of functional-programming.
# the different functions are explained in the "functionProgramm.py"-file.
if firstInput == 2:
    getMovies(getJSON(linksPopularityCreater()))

elif firstInput == 1:
    links = linksYearCreater()

    notCorrect = True

# This while-loop goes on and on, until the user enters the correct input (1, 2 or 3).
# the "notCorrect"-variable was earlier declared as boolean "True", that's what keeps the while-loop running
# after the user puts in a value, the "notCorrect"-variable gets set on False, but if the input is not what we want, we put it on False again.
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










