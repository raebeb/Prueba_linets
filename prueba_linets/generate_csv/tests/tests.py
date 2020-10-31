from django.test import TestCase
from generate_csv.models import MasterProductsConfigurable
from rest_framework.test import APIRequestFactory
import json

class MasterProductsConfigurableTest(TestCase):
    databases = {'legacy_db'}
    @classmethod
    def setUpTestData(cls):
        MasterProductsConfigurable.objects.create(model='test model', sku='TESTSKU', color_group_hex='color test')

    def test_model_label(self):
        product=MasterProductsConfigurable.objects.get(sku='TESTSKU')
        field_label = product._meta.get_field('model').verbose_name
        self.assertEquals(field_label,'model')

    def test_generate_csv_url_exists_at_desired_location(self): 
        resp = self.client.get('/generate_csv/') 
        self.assertEqual(resp.status_code, 200)

    def test_product_list_url_exists_at_desired_location(self): 
        resp = self.client.get('/generate_csv/api/product-list/') 
        self.assertEqual(resp.status_code, 200)

    def test_create_product_api(self):
        factory = APIRequestFactory()
        resp = factory.post('/generate_csv/api/product-create/', json.dumps({'sku': 'pruebasku2'}), content_type='application/json')
