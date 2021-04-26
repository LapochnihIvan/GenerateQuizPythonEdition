from typing import List
from os.path import exists
from os import mkdir


class Reader:
    def __init__(self):
        self.__filesNames: List[str] = ['quests.in.txt',
                                        'textsAns.in.txt',
                                        'correctAns.in.txt']

    def catch_errors(self) -> List[str]:
        error_files: List[str] = []
        for fileName in self.__filesNames:
            with open('input/' + fileName) as stream:
                if len(stream.read().split('\n')) < 20:
                    error_files.append(fileName)
        return error_files

    def catch_fatal_errors(self) -> List[str]:
        error_files: List[str] = []
        if not exists('input'):
            try:
                mkdir('input')
            except PermissionError:
                return ['input/']
        for filename in self.__filesNames:
            if not exists('input'):
                try:
                    with open(filename, 'w') as stream:
                        stream.close()
                except PermissionError:
                    error_files.append('input/' + filename)
        return error_files

    @staticmethod
    def read_quests() -> List[str]:
        with open('input/quests.in.txt', encoding='utf-8') as stream:
            return stream.read().split(';')

    @staticmethod
    def read_texts_ans() -> List[List[str]]:
        result: List[List[str]] = []
        with open('input/textsAns.in.txt', encoding='utf-8') as stream:
            for ans in stream.read().split(';'):
                result.append(ans.replace('\n', '').split('/'))
        return result

    @staticmethod
    def read_correct_ans() -> List[int]:
        with open('input/correctAns.in.txt') as stream:
            return list(map(int, stream.read().split('\n')))
