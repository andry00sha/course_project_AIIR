from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class DegreeTests(APITestCase):
    def test_degree_correct(self):
        """
        Ensure that operation with correct operands works
        :return:
        """

        url = reverse('degrator', args=["1_2-3_4", 2])
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "matrix": "1_2-3_4",
            "step": 2,
            "result": "[[ 7 10]\n [15 22]]"
        })
# Create your tests here.
