from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Recipe

class BooksModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Recipe.objects.create(
            title = 'Title of Recipe',
            author = test_user,
            description = 'Words about the recipe'
        )
        test_post.save()

    def test_recipe_content(self):
        recipe = Recipe.objects.get(id=1)

        self.assertEqual(recipe.title, 'Title of Recipe')
        self.assertEqual(str(recipe.author), 'tester')
        self.assertEqual(recipe.description, 'Words about the recipe')
        