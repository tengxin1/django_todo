from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("404, 此id的问题不存在")
    print(question)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', {'context': question})

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        choices = question.choice_set.all()
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(id=choice_id)
    except Question.DoesNotExist as e:
        error_message = '问题内容不存在，检查问题id'
    except Choice.DoesNotExist as e:
        error_message = '问题对应的选项不存在'
        return render(request, 'polls/detail.html', context={
            'question': question,
            'error_message': error_message
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls: results', args=(question.id,)))

class SimpleView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()