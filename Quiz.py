from typing import List

from Reader import Reader


class Quiz:
    def __init__(self):
        self.__quests: List[str] = []
        self.__correctAns: List[int] = []
        self.__textsAns: List[List[str]] = []
        self.__numRound: int = 0
        self.__reader: Reader = Reader()

    def nextRound(self) -> None:
        self.__numRound += 1

    def getQuest(self) -> str:
        return self.__quests[self.__numRound]

    def getCorrectAns(self) -> int:
        return self.__correctAns[self.__numRound]

    def isEmpty(self) -> bool:
        return self.__numRound == 20

    def getTextsAns(self) -> List[str]:
        return self.__textsAns[self.__numRound]

    def isFatalError(self) -> bool:
        return bool(self.__reader.catchFatalErrors())

    def getErrorFiles(self) -> List[str]:
        errorFiles: List[str] = self.__reader.catchFatalErrors()
        if not errorFiles:
            errorFiles = self.__reader.catchErrors()
            if not errorFiles:
                self.__quests = Reader.readQuests()
                self.__textsAns = Reader.readTextsAns()
                self.__correctAns = Reader.readCorrectAns()
        return errorFiles
