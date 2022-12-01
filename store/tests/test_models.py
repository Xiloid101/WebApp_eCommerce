from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='FPS', slug='fps')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'FPS')

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='FPS', slug='fps')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='doom', created_by_id=1,
                               slug='doom', price='15.00', image='default')

    def test_products_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'doom')
