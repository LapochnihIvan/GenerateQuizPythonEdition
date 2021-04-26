from typing import List

from Reader import Reader


class Quiz:
    def __init__(self):
        self.__quests: List[str] = []
        self.__correctAns: List[int] = []
        self.__textsAns: List[List[str]] = []
        self.__numRound: int = 0
        self.__reader: Reader = Reader()

    def next_round(self) -> None:
        self.__numRound += 1

    def get_quest(self) -> str:
        return self.__quests[self.__numRound]

    def get_correct_ans(self) -> int:
        return self.__correctAns[self.__numRound]

    def is_empty(self) -> bool:
        return self.__numRound == 20

    def get_texts_ans(self) -> List[str]:
        return self.__textsAns[self.__numRound]

    def is_fatal_error(self) -> bool:
        return bool(self.__reader.catch_fatal_errors())

    def get_error_files(self) -> List[str]:
        error_files: List[str] = self.__reader.catch_fatal_errors()
        if not error_files:
            error_files = self.__reader.catch_errors()
            if not error_files:
                self.__quests = Reader.read_quests()
                self.__textsAns = Reader.read_texts_ans()
                self.__correctAns = Reader.read_correct_ans()
        return error_files
