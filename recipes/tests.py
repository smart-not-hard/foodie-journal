from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# from rest_framework import api
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser

from .serializers import RecipesSerializer
from .models import Recipe


class BModelTests(TestCase):
    def test_user_creation(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.email, "tester@email.com")
        self.assertIsNotNone(user.password)

    def test_recipe_content(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="easy",
        )
        recipe.save()

        self.assertEqual(recipe.title, "test")
        self.assertEqual(str(recipe.author), "tester")
        self.assertEqual(recipe.description, "test recipes")
        self.assertEqual(recipe.ingredients, "test")
        self.assertEqual(recipe.steps, "step one")

    

    def test_GET_recipe_difficulty_easy(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        easy_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="easy",
        )
        easy_recipe.save()

        hard_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="hard",
        )
        hard_recipe.save()

        easy_recipe = Recipe.objects.get(difficulty="easy")
        self.assertEqual(easy_recipe.difficulty, "easy")

    def test_GET_recipe_difficulty_hard(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        easy_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="easy",
        )
        easy_recipe.save()

        hard_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="hard",
        )
        hard_recipe.save()

        hard_recipe = Recipe.objects.get(difficulty="hard")
        self.assertEqual(hard_recipe.difficulty, "hard")


    def test_GET_recipe_type_breakfast(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        breakfast_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="breakfast",
            img_src_1="img",
            difficulty="easy",
        )
        breakfast_recipe.save()

        dinner_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="hard",
        )
        dinner_recipe.save()

        breakfast_recipe = Recipe.objects.get(meal_type="breakfast")
        self.assertEqual(breakfast_recipe.meal_type, "breakfast")
            
    def test_GET_recipe_type_dinner(self):
        user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        breakfast_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="breakfast",
            img_src_1="img",
            difficulty="easy",
        )
        breakfast_recipe.save()

        dinner_recipe = Recipe.objects.create(
            title="test",
            author=user,
            description="test recipes",
            ingredients="test",
            steps="step one",
            meal_type="dinner",
            img_src_1="img",
            difficulty="hard",
        )
        dinner_recipe.save()

        dinner_recipe = Recipe.objects.get(meal_type="dinner")
        self.assertEqual(dinner_recipe.meal_type, "dinner")