from django.urls import path
from .views import random_flashcard, FlashcardsView, BlogPageView, AboutQuiz, Start, FinishPage, show_certificate

urlpatterns = [
    path('', FlashcardsView.as_view(), name='index'),
    path('leitner_system/', BlogPageView.as_view(), name='leitner_system'),
    path('about_quiz/', AboutQuiz.as_view(), name='about_quiz'),
    path('flashcards/', random_flashcard, name='flashcard'),
    path('start/', Start.as_view(), name='start'),
    path('finish_page/', FinishPage.as_view(), name='finish'),
    path('certificate/', show_certificate, name='certificate'),
]
