
from Timer import Timer
from SurveyGroup import SurveyGroupUnqiueQuestions
from SurveyGroup import SurveyGroupAllAnsweredSameQuestion

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

sumOfUniqueAnswersPart1 = 0
sumOfUniqueAnswersPart2 = 0

for group in surveyGroups:
    surveyGroupPart1 = SurveyGroupUnqiueQuestions(group)
    sumOfUniqueAnswersPart1 += surveyGroupPart1._SurveyGroupUnqiueQuestions__numberOfUniqueAnswers

for group in surveyGroups:
    surveyGroupPart2 = SurveyGroupAllAnsweredSameQuestion(group)
    sumOfUniqueAnswersPart2 += surveyGroupPart2._SurveyGroupAllAnsweredSameQuestion__numberOfUniqueAnswers

print("Total unique answers, part 1, {0}".format(sumOfUniqueAnswersPart1))
print("Total unique answers, part 2, {0}".format(sumOfUniqueAnswersPart2))
print("Application finished. Time taken (s), {0}".format(applicationTimer.elapsedTime()))