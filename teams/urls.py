from django.urls import path
from teams.views import TeamView, Team_paramtsView

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:teams_id>/', Team_paramtsView.as_view()),
]
