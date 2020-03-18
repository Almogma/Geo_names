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

    @patch('src.postal_code_class.requests.get')
    def test_valid_postal_code_invalid_country_valid_username(self, mock_get):
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
        postal_code = '6600'
        country = 'HELLO'
        user_name = 'shirel_biton'

        # expected
        expected = {'postalcodes': []}

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_invalid_postal_code_invalid_country_valid_username(self, mock_get):
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
        country = 'HELLO'
        user_name = 'shirel_biton'

        # expected
        expected = {'postalcodes': []}

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_invalid_postal_code_invalid_country_invalid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        postal_code_information = {'status': {'message': 'user does not exist.', 'value': 10}}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = postal_code_information

        # assume
        postal_code = '6600000'
        country = 'HELLO'
        user_name = 'aaa'

        # expected
        expected = {'status': {'message': 'user does not exist.', 'value': 10}}

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    def test_invalid_type_postal_code(self):
        '''

        :return:
        '''
        # assume
        postal_code = 123
        country = 'AT'
        user_name = 'shirel_biton'

        # expected
        expected = "Invalid input type"

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    def test_invalid_type_country(self):
        '''

        :return:
        '''
        # assume
        postal_code = '6600'
        country = 324
        user_name = 'shirel_biton'

        # expected
        expected = "Invalid input type"

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    def test_invalid_type_user_name(self):
        '''

        :return:
        '''
        # assume
        postal_code = '6600'
        country = 'AT'
        user_name = 1

        # expected
        expected = "Invalid user type"

        # action
        result = PostalCode.postal_code_places(postal_code, country, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_valid_lat_valid_lng_valid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        time_zone_information = {'sunrise': '2020-03-17 06:27', 'lng': 10.2, 'countryCode': 'AT',
                                 'gmtOffset': 1, 'rawOffset': 1, 'sunset': '2020-03-17 18:28',
                                 'timezoneId': 'Europe/Vienna', 'dstOffset': 2,
                                 'countryName': 'Austria', 'time': '2020-03-17 11:16', 'lat': 47.01}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = time_zone_information

        # assume
        lat = '47.01'
        lng = '10.02'
        user_name = 'shirel_biton'

        # expected
        expected = 'country name: Austria, sunrise: 2020-03-17 06:27, sunset2020-03-17 18:28'

        # action
        result = PostalCode.time_zone(lat, lng, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_invalid_lat_valid_lng_valid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        time_zone_information = {'status': {'message': 'error parsing parameter', 'value': 14}}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = time_zone_information

        # assume
        lat = 'abc'
        lng = '10.02'
        user_name = 'shirel_biton'

        # expected
        expected = 'error parsing parameter'

        # action
        result = PostalCode.time_zone(lat, lng, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_invalid_lat_invalid_lng_valid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        time_zone_information = {'status': {'message': 'error parsing parameter', 'value': 14}}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = time_zone_information

        # assume
        lat = 'abc'
        lng = 'def'
        user_name = 'shirel_biton'

        # expected
        expected = 'error parsing parameter'

        # action
        result = PostalCode.time_zone(lat, lng, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_invalid_lat_invalid_lng_invalid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        time_zone_information = {'status': {'message': 'invalid user', 'value': 14}}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = time_zone_information

        # assume
        lat = 'asd'
        lng = '@cg'
        user_name = '23sa'

        # expected
        expected = 'invalid user'

        # action
        result = PostalCode.time_zone(lat, lng, user_name)

        # assert
        self.assertEqual(result, expected)

    @patch('src.postal_code_class.requests.get')
    def test_valid_lat_invalid_lng_valid_username(self, mock_get):
        '''

        :param mock_get: mock the object behaviour
        :return:
        '''
        time_zone_information = {'status': {'message': 'error parsing parameter', 'value': 14}}

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = time_zone_information

        # assume
        lat = '47.01'
        lng = 'sdas'
        user_name = 'shirel_biton'

        # expected
        expected = 'error parsing parameter'

        # action
        result = PostalCode.time_zone(lat, lng, user_name)

        # assert
        self.assertEqual(result, expected)

    def test_invalid_type_lat(self):
        '''

        :return:
        '''
        # assume
        lat = 40
        lng = '10.2'
        user_name = 'shirel_biton'

        # expected
        expected = "Invalid input type"

        # action
        result = PostalCode.time_zone(lat, lng, user_name)

        # assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
