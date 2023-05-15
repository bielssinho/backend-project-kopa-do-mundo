from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict

from teams.models import Team
from teams.utils import data_processing


# Create your views here.
class TeamView(APIView):
    def get(self, request: Request):
        teams = Team.objects.all()

        teams_list = [model_to_dict(team) for team in teams]

        return Response(teams_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        data_processing(request.data)

        team = Team.objects.create(**request.data)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)


class Team_paramtsView(APIView):
    def get(self, request: Request, teams_id: int) -> Response:
        try:
            team = Team.objects.get(pk=teams_id)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, teams_id: int) -> Response:
        try:
            team = Team.objects.get(pk=teams_id)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        data_processing(request.data)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, teams_id: int) -> Response:
        try:
            team = Team.objects.get(pk=teams_id)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
