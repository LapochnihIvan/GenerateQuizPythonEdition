from threading import Thread
from typing import List

from Quiz import Quiz
from GUI import GUI


def process():
    while not quiz.is_empty():
        if gui.get_response() == quiz.get_correct_ans():
            quiz.next_round()
            if quiz.is_empty():
                gui.end_of_quiz()
            else:
                gui.set_quest_frame(quiz.get_quest(), quiz.get_texts_ans())
        else:
            gui.wrong_ans()


if __name__ == '__main__':
    gui: GUI = GUI()
    quiz: Quiz = Quiz()
    errorFiles: List[str] = quiz.get_error_files()
    #
    if not errorFiles:
        gui.generation()
        gui.set_quest_frame(quiz.get_quest(), quiz.get_texts_ans())
        tread = Thread(target=process)
        tread.start()
    else:
        gui.create_error_window(errorFiles, quiz.is_fatal_error())
    gui.exec()
