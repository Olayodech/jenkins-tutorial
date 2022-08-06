from mepottests import TestBase 
from flask import url_for
import unittest

class TestIndex(TestBase):
    
    def test_index(self):
        response = self.client.get(url_for('home.index'))
        self.assertEqual(response.status_code, 200)
        print(f'Response data is {response.data}')

if __name__=="__main__":
    unittest.main(verbosity=2)