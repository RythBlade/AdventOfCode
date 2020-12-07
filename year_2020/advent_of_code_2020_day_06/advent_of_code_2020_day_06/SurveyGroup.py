
class SurveyGroup:
    def __init__(self, groupString):
        listOfPeoplesResponses = groupString.strip().split("\n")

        # dictionary of 
        self.foundUniqueQuestions = []

        for response in listOfPeoplesResponses:
            for answer in response:
                if (answer in self.foundUniqueQuestions) == False:
                    self.foundUniqueQuestions.append(answer)

        self.__numberOfUniqueAnswers = len(self.foundUniqueQuestions)

