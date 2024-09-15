from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from performance.models import Performance

class PerformanceTests(APITestCase):

    def setUp(self):
        self.performance1 = Performance.objects.create(
            player_id=1,
            passing_game=10,
            flying_ball=5,
            assists=3,
            goals=2,
            ball_control=8,
            group_defense=7,
            completion_of_action=6,
            team_attack=4
        )
        self.performance2 = Performance.objects.create(
            player_id=2,
            passing_game=12,
            flying_ball=6,
            assists=4,
            goals=3,
            ball_control=9,
            group_defense=8,
            completion_of_action=7,
            team_attack=5
        )
        self.list_url = reverse('performance-list')
        self.player_list_url = reverse('player-performance-list', kwargs={'player_id': 1})
        self.detail_url = reverse('performance-detail', kwargs={'player_id': 1, 'performance_id': self.performance1.pk})

    def test_get_performance_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_performance(self):
        data = {
            'player_id': 3,
            'passing_game': 14,
            'flying_ball': 7,
            'assists': 5,
            'goals': 4,
            'ball_control': 10,
            'group_defense': 9,
            'completion_of_action': 8,
            'team_attack': 6
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Performance.objects.count(), 3)
        self.assertEqual(Performance.objects.latest('pk').player_id, 3)

    def test_get_performance_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['player_id'], 1)
        self.assertEqual(response.data['passing_game'], 10)

    def test_put_performance(self):
        data = {
            'passing_game': 15,
            'flying_ball': 8
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.performance1.refresh_from_db()
        self.assertEqual(self.performance1.passing_game, 15)
        self.assertEqual(self.performance1.flying_ball, 8)

    def test_delete_performance(self):
        delete_url = reverse('performance-detail', kwargs={'player_id': 1, 'performance_id': self.performance1.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Performance.objects.count(), 1)
