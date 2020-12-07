
from Timer import Timer
from SurveyGroup import SurveyGroup

def loadSurveyAnswers(filename):
    concatenatedFile = ""
    with open(filename) as file:
        for line in file:
            concatenatedFile += line

    return concatenatedFile


applicationTimer = Timer()
print("Application started")

surveyFilename = "survey_answers.txt"

surveyFile = loadSurveyAnswers(surveyFilename)

surveyGroups = surveyFile.split("\n\n")

sumOfUniqueAnswers = 0

for group in surveyGroups:
    surveyGroup = SurveyGroup(group)
    sumOfUniqueAnswers += surveyGroup._SurveyGroup__numberOfUniqueAnswers

print("Total unique answers, {0}".format(sumOfUniqueAnswers))
print("Application finished. Time taken (s), {0}".format(applicationTimer.elapsedTime()))