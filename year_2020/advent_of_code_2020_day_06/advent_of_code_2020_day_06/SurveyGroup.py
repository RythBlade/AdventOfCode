
class SurveyGroupUnqiueQuestions:
    def __init__(self, groupString):
        listOfPeoplesResponses = groupString.strip().split("\n")

        # dictionary of 
        self.foundUniqueQuestions = []

        for response in listOfPeoplesResponses:
            for answer in response:
                if (answer in self.foundUniqueQuestions) == False:
                    self.foundUniqueQuestions.append(answer)

        self.__numberOfUniqueAnswers = len(self.foundUniqueQuestions)


class SurveyGroupAllAnsweredSameQuestion:
    def __init__(self, groupString):
        listOfPeoplesResponses = groupString.strip().split("\n")

        # dictionary of 
        self.foundUniqueQuestions = []

        mainList = []

        if len(listOfPeoplesResponses) > 0:
            mainList = listOfPeoplesResponses.pop(0)

        for character in mainList:
            characterIsInAllResponses = True

            for response in listOfPeoplesResponses:
                if character in response:
                    response.replace(character, '')
                else:
                    characterIsInAllResponses = False

            if characterIsInAllResponses:
                self.foundUniqueQuestions.append(character)

        self.__numberOfUniqueAnswers = len(self.foundUniqueQuestions)

