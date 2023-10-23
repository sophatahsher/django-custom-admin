from django.urls import path, include

from . import views

app_name = 'api_app'

urlpatterns=[
    #path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path("", views.index, name="index"),
    path("polls/", views.polls, name="polls"),
    path("polls/<int:question_id>/", views.details, name="details"),
    path("polls/<int:question_id>/results/", views.results, name="results"),
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),

    # api
    path("polls/", views.getData, name="findAllPolls")
]