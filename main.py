from threading import Thread
from typing import List

from Quiz import Quiz
from GUI import GUI
#
#
def process():
    while not quiz.isEmpty():
        if gui.getResponse() == quiz.getCorrectAns():
            quiz.nextRound()
            if quiz.isEmpty():
                gui.endOfQuiz()
            else:
                gui.setQuestFrame(quiz.getQuest(), quiz.getTextsAns())
        else:
            gui.wrongAns()


if __name__ == '__main__':
    gui: GUI = GUI()
    quiz: Quiz = Quiz()
    errorFiles: List[str] = quiz.getErrorFiles()
    #
    if not errorFiles:
        gui.generation()
        gui.setQuestFrame(quiz.getQuest(), quiz.getTextsAns())
        tread = Thread(target=process)
        tread.start()
    else:
        gui.createErrorWindow(errorFiles, quiz.isFatalError())
    gui.exec()
