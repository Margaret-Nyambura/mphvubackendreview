from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, Coach

class TeamTests(APITestCase):
    def setUp(self):
        self.coach = Coach.objects.create(name='John Doe')
        self.team = Team.objects.create(
            team_name='Warriors',
            sport='Basketball',
            coach_id=self.coach,
            image=None  # Provide an image if needed
        )
        self.team_list_url = reverse('team-list')
        self.team_detail_url = reverse('team-detail', kwargs={'team_id': self.team.team_id})

    def test_get_team_list(self):
        response = self.client.get(self.team_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['team_name'], 'Warriors')

    def test_get_team_detail(self):
        response = self.client.get(self.team_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['team_name'], 'Warriors')

    def test_create_team(self):
        data = {
            'team_name': 'Lions',
            'sport': 'Soccer',
            'coach_id': self.coach.id,
        }
        response = self.client.post(self.team_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Team.objects.get(team_id=response.data['team_id']).team_name, 'Lions')

    def test_update_team(self):
        data = {
            'team_name': 'Tigers',
            'sport': 'Football',
            'coach_id': self.coach.id,
        }
        response = self.client.put(self.team_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.get(team_id=self.team.team_id).team_name, 'Tigers')

    def test_delete_team(self):
        response = self.client.delete(self.team_detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # If DELETE is not supported
        self.assertEqual(Team.objects.count(), 1)  # Ensure the team is still there