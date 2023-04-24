from django.shortcuts import render
from django.http import HttpResponse
from .models import Flashcards
import random
from django.views.generic import ListView
from .process import html_to_pdf


# Create your views here.


def random_flashcard(request, kwargs=None):
    number_of_flashcards = Flashcards.objects.count()
    random_id = random.randint(1, number_of_flashcards)

    if 'flashcard_displayed' in request.session:
        if len(request.session['flashcard_displayed']) == number_of_flashcards:
            return render(request, 'finish_page.html')

        if random_id not in request.session['flashcard_displayed']:
            request.session['flashcard_displayed'].insert(0, random_id)
            flashcard = Flashcards.objects.get(ID=random_id)

        else:
            while random_id in request.session['flashcard_displayed']:
                random_id = random.randint(1, number_of_flashcards)

            request.session['flashcard_displayed'].insert(0, random_id)
            flashcard = Flashcards.objects.get(ID=random_id)

    else:
        random_id = random.randint(1, number_of_flashcards)
        flashcard = Flashcards.objects.get(ID=random_id)
        request.session['flashcard_displayed'] = [random_id]

    request.session.modified = True

    context = {'random_flashcard': flashcard}

    return render(request, 'flashcard.html', context)


def show_certificate(request):
    pdf = html_to_pdf('result.html')

    return HttpResponse(pdf, content_type='application/pdf')


class FlashcardsView(ListView):
    template_name = 'main_page.html'
    model = Flashcards


class BlogPageView(ListView):
    template_name = 'Leitner_system.html'
    model = Flashcards


class AboutQuiz(ListView):
    template_name = 'about_quiz.html'
    model = Flashcards


class Start(ListView):
    template_name = 'start.html'
    model = Flashcards


class FinishPage(ListView):
    template_name = 'finish_page.html'
    model = Flashcards


def error_404(request, exception):
    return render(request, 'notfound.html')


def error_500(request):
    return render(request, 'notfound.html')
