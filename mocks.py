"""Timed mocks for LexStudy Ghana v0.3.

One timed mock per subject that already has a quiz, built on the
same questions as the quiz. A mock is a study aid: the countdown
runs in the browser and submits the form when time runs out.
The server does not enforce the time limit.

Mock slugs match quiz slugs, so a mock and its quiz cover the
same subject and the same questions.
"""

from quizzes import QUIZZES

TIME_LIMIT_MINUTES = 10


def get_mock(slug):
    quiz = QUIZZES.get(slug)
    if quiz is None:
        return None
    return {
        "slug": slug,
        "title": quiz["subject"] + " timed mock",
        "subject": quiz["subject"],
        "time_limit_minutes": TIME_LIMIT_MINUTES,
        "questions": quiz["questions"],
    }


def all_mocks():
    return [get_mock(slug) for slug in QUIZZES]
