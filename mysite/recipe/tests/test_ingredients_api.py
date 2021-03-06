from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient, Recipe

from recipe.serializers import IngredientSerializer

ING_URL = reverse('recipe:ingredient-list')


class PublicTagsApiTests(TestCase):
    """Test the publicly avaiable ingredients API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that loging is required for retrieving ingredients"""
        res = self.client.get(ING_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """Test the private ingredients API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@londondevapp.com',
            password='testpass',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_ingredients(self):
        """Test that login is required for retrieving ingredients"""
        Ingredient.objects.create(user=self.user, name='Kale')
        Ingredient.objects.create(user=self.user, name='Salt')

        res = self.client.get(ING_URL)

        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_ingredients_limited_to_user(self):
        """Test that ingredients returned are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            email='other@londondevapp.com',
            password='testpass',
        )

        Ingredient.objects.create(user=user2, name='Vinegar')
        ingredient = Ingredient.objects.create(user=self.user, name='Turmeric')

        res = self.client.get(ING_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)

    def test_create_ingredient_successful(self):
        """Test creating a new ingredient"""
        payload = {'name': 'Test Ingredient'}
        self.client.post(ING_URL, payload)

        exists = Ingredient.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_ingredient_invalid(self):
        """Test creating a new ingredient with an invalid payload"""
        payload = {'name': ''}
        res = self.client.post(ING_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_ingredients_assigned_to_recipes(self):
        """Test filtering ingredients by those assigned to recipes"""
        ingredient1 = Ingredient.objects.create(
            user=self.user, name='Apples'
        )

        ingredient2 = Ingredient.objects.create(
            user=self.user, name='Turkey'
        )
        recipe = Recipe.objects.create(
            title='Eggs benedict',
            time_minutes=30,
            price=12.00,
            user=self.user
        )
        recipe.ingredients.add(ingredient1)

        res = self.client.get(ING_URL, {'assigned_only': 1})

        ser1 = IngredientSerializer(ingredient1)
        ser2 = IngredientSerializer(ingredient2)
        self.assertIn(ser1.data, res.data)
        self.assertNotIn(ser2.data, res.data)

    def test_retrieve_ingredients_assigned_unique(self):
        """Test filtering ingredients by those assigned to recipes"""
        ingredient = Ingredient.objects.create(
            user=self.user, name='Apples'
        )
        Ingredient.objects.create(user=self.user, name='Turkey')
        recipe1 = Recipe.objects.create(
            title='Eggs benedict',
            time_minutes=30,
            price=12.00,
            user=self.user
        )
        recipe1.ingredients.add(ingredient)

        recipe2 = Recipe.objects.create(
            title='Pizza',
            time_minutes=30,
            price=12.00,
            user=self.user
        )
        recipe2.ingredients.add(ingredient)

        res = self.client.get(ING_URL, {'assigned_only': 1})

        self.assertEqual(len(res.data), 1)
