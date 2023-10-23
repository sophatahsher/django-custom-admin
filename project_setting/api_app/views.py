from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .form import GenerateRandomUserForm
from .tasks import create_random_user_accounts

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    print(f'-------------{latest_question_list}')
    template = loader.get_template("home/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))

def polls(request):
    #return HttpResponse("Hello Django")
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/details.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    




@api_view(['GET'])
def getData(request):
    question_list = [
        {
            "id": 1,
            "question_text": "Question A"
        },
        {
            "id": 2,
            "question_text": "Question B"
        }
    ]
    return Response(question_list, status=status.HTTP_200_OK)

@api_view(['POST'])
def findAllPolls(request):
    print(f'-----------------{request}')
    question_list = [
        {
            "id": 1,
            "question_text": "Question A"
        },
        {
            "id": 2,
            "question_text": "Question B"
        }
    ]
    return Response(question_list, status=status.HTTP_200_OK)

@api_view(['POST'])
def findOnePoll(request, question_id):

    question = {
            "id": 1,
            "question_text": "Question A"
        }
    return Response(question, status=status.HTTP_200_OK)
   
    
    

class UsersListView(ListView):
    template_name = 'task/users_list.html'
    model = User

class GenerateRandomUserView(FormView):
    
    

    template_name = 'task/generate_random_user.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')