from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
# from rest_framework import api
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .serializers import RecipesSerializer
from .models import Recipe
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
# class BModelTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         test_post = Recipe.objects.create(
#             title='test',
#             description='test recipes',
#             ingredients='test',
#             steps='step one',
#             meal_type='dinner',
#             img_src_1='img',
#             difficulty='easy',
#         )
#         test_post.save()

#     def test_recipe_content(self):
#         recipe = Recipe.objects.get(id=1)

#         self.assertEqual(recipe.title, 'Title of Recipe')
#         self.assertEqual(str(recipe.author), 'tester')
#         self.assertEqual(recipe.description, 'Words about the recipe')
# class TestCustomRecipe(TestCase):

#     def recipe_creation(self):
#         user = Recipe().objects.create_recipe(
#             title='test',
#             author='1',
#             description='test recipes',
#             ingredients='test',
#             steps='step one',
#             meal_type='dinner',
#             img_src_1='img',
#             difficulty='easy',
#         )

#         self.assertIsInstance(user, CustomUser)
#         self.assertEqual(user.email, 'tester@email.com')
#         self.assertIsNotNone(user.password)

#     def test_no_dupe_email(self):
#         user_1 = get_user_model().objects.create_user(
#             username='tester',
#             email='tester@email.com',
#             password='pass'
#         )

#         try:
#             user_2 = get_user_model().objects.create_user(
#                 username='nottester',
#                 email='tester@email.com',
#                 password='pass'
#             )
#         except IntegrityError:

#             print('all good')

#         else:
#             self.fail('no bueno')

# class RecipeTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         testuser1 = User.objects.create_user(
#             username='jb', password='jb')
#         testuser1.save()

#         test_post = Recipe.objects.create(
#             title='test',
#             author='1',
#             description='test recipes',
#             ingredients='test',
#             steps='step one',
#             meal_type='dinner',
#             img_src_1='img',
#             difficulty='easy',
#         )
#         test_post.save()

#     def test_recipe_create_content(self):
#         post = Recipe.objects.post(id=1)
#         expected_title = f'{test_post.title}'
#         expected_author = f'{test_post.author}'
#         expected_description = f'{test_post.description}'
#         expected_ingredients = f'{test_post.ingredients}'
#         expected_steps = f'{test_post.steps}'
#         expected_meal_type = f'{test_post.meal_type}'
#         expected_img_src_1 = f'{test_post.img_src_1}'
#         expected_difficulty = f'{test_post.difficulty}'

#         self.assertEqual(expected_title, 'test')
#         self.assertEqual(expected_description, 'test recipes')
#         self.assertEqual(expeced_author, 'testuser1')
#         self.assertEqual(expected_ingredients, 'test')
#         self.assertEqual(expected_steps, 'step one')
#         self.assertEqual(expected_meal_type, 'dinner')
#         self.assertEqual(expected_img_src_1, 'img')
#         self.assertEqual(expected_difficulty, 'easy')
    
#     def test_recipe_get_filter_content(self):
#         test_post = Recipe.objects.create(
#             title='test',
#             author='1',
#             description='test recipes',
#             ingredients='test',
#             steps='step one',
#             meal_type='dinner',
#             img_src_1='img',
#             difficulty='easy',
#         )
#         test_post.save()

#         get = Recipe.objects.get(id=1)
#         expected_title = f'{test_post.title}'
#         expected_description = f'{test_post.description}'
#         expected_ingredients = f'{test_post.ingredients}'
#         expected_steps = f'{test_post.steps}'
#         expected_meal_type = f'{test_post.meal_type}'
#         expected_img_src_1 = f'{test_post.img_src_1}'
#         expected_difficulty = f'{test_post.difficulty}'

#         self.assertEqual(expected_title, 'test')
#         self.assertEqual(expected_description, 'test recipes')
#         self.assertEqual(expected_ingredients, 'test')
#         self.assertEqual(expected_steps, 'step one')
#         self.assertEqual(expected_meal_type, 'dinner')
#         self.assertEqual(expected_img_src_1, 'img')
#         self.assertEqual(expected_difficulty, 'easy')
    
class TestCustomRecipe(TestCase):
    # user = get_user_model().objects.create_user(
    #         username='tester',
    #         # email='tester@email.com',
    #         password='pass'
    #     )
        
    test_post = Recipe.objects.create(
            title='test',
            author=CustomUser.username,
            description='test recipes',
            ingredients='test',
            steps='step one',
            meal_type='dinner',
            img_src_1='img',
            difficulty='easy',
        )
    test_post.save()

    factory = APIRequestFactory()
    request = factory.post('/recipes/create/', test_post)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Recipe.objects.count(), 1)
    self.assertEqual(Recipe.objects.get().title, 'test')