'''
Authors: Shirel Biton, 207276452
         Shani Waizman, 316440262
         Kobaivanov Yakir, 313566390
'''
import unittest
from unittest.mock import Mock, patch
from src.postal_code_class import PostalCode

class MyTestCase(unittest.TestCase):
    '''
        Testing postal code places and time zone functions
    '''

    @patch('src.postal_code_class.requests.get')
    def test_valid_postal_code_valid_country_valid_username(self, mock_get):
        '''
        :param mock_get: mock the object behaviour
        :return:
        '''
        postal_code_information = ['Breitenwang', 'Ehenbichl', 'Lechaschau', 'Musau',
                                   'Oberletzen', 'Oberpinswang', 'Pflach', 'Reutte',
                                   'Unterletzen', 'Unterpinswang']

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = postal_code_information

        # assume
        postal_code = '6600'
        country = 'AT'
        user_name = 'shirel_biton'

        # expected
        expected = ['Breitenwang', 'Ehenbichl', 'Lechaschau', 'Musau',
                    'Oberletzen', 'Oberpinswang', 'Pflach',
                    'Reutte', 'Unterletzen', 'Unterpinswang']

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_invalid_postal_code_valid_country_valid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        postal_code_information = {'postalcodes': []}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = postal_code_information

        # assume
        postal_code = '6600000'
        country = 'AT'
        user_name = 'shirel_biton'

        # expected
        expected = {'postalcodes': []}

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
