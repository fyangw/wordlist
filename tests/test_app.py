import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from flask_testing import TestCase
from app import app, word_list

class TestAppRoutes(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b'<div class="content">', response.data)

    def test_api_endpoint(self):
        # 测试正常请求
        response = self.client.get('/api/words/0')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('word', data)
        self.assertIn('translation', data)
        self.assertIn('phonetic', data)

        # 测试边界值
        invalid_response = self.client.get(f'/api/words/{len(word_list)+1}')
        self.assertEqual(invalid_response.status_code, 200)
        self.assertEqual(invalid_response.json["current_index"], len(word_list)-1)

if __name__ == '__main__':
    unittest.main()