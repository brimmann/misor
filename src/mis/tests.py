from django.test import TestCase
from misor_core.main import misor

class ModelResponseTest(TestCase):
    def test_urls_exists_for_all_models(self):
        for model_name in misor.get_models_dict():
            view_response = self.client.get(f'/mis/{model_name}/')
            create_response = self.client.get(f'/mis/{model_name}/create/')
            self.assertEqual(view_response.status_code, 200)
            self.assertEqual(create_response.status_code, 200)