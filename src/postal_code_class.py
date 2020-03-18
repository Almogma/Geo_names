'''
Authors: Shirel Biton, 207276452
         Shani Waizman, 316440262
         Kobaivanov Yakir, 313566390
'''
import requests

class PostalCode:
    '''
    return postal codes and places for the placename/postalcode
    '''
    @staticmethod
    def postal_code_places(postal_code, country, user_name):
        '''

        :param postal_code: string (postalcode or placename required)
        :param country: string (country name)
        :param user_name: string (user name of geo names api)
        :return: if the postal code, country or user name is not str return invalid input type,
                 if the parametes are correct return the place names other return a message.
        '''
        if isinstance(postal_code, str) is False or isinstance(country, str) is False:
            return "Invalid input type"
        if isinstance(user_name, str) is False:
            return "Invalid user type"

        url = 'http://'
        url = url + 'api.geonames.org/postalCodeLookupJSON?postalcode=' + postal_code
        url = url + '&country=' + country
        url = url + '&username=' + user_name
        api_result = requests.get(url)
        api_response = api_result.json()
        try:
            result = []
            for i in range(len(api_response['postalcodes'])):
                result.append(api_response['postalcodes'][i]['placeName'])
            if len(result) == 0:
                return api_response
            return result
        except KeyError:
            return api_response
        except TypeError:
            return api_response

    @staticmethod
    def time_zone(lat, lng, user_name):
        '''

        :param lat: string (latitude)
        :param lng: string (longitude)
        :param user_name: string (user name of geo names api)
        :return: if the postal code, country or user name is not str return invalid input type,
                 if the parameters are correct return country name, sunrise and sunset,
                 other return message.
        '''
        if isinstance(lat, str) is False or isinstance(lng, str) is False:
            return "Invalid input type"
        if isinstance(user_name, str) is False:
            return "Invalid user type"

        try:
            url = 'http://'
            url = url + 'api.geonames.org/timezoneJSON?lat=' + lat
            url = url + '&lng=' + lng
            url = url + '&username=' + user_name
            api_result = requests.get(url)
            api_response = api_result.json()
            return "country name: " + api_response['countryName'] + \
                   ", sunrise: " + api_response['sunrise'] + \
                   ", sunset" + api_response['sunset']

        except KeyError:
            return api_response['status']['message']

    @staticmethod
    def input_location(unit):
        if unit == 'p':
            postal_code = input("enter postal code for places names information: ")
            country = input("enter country name for places names information: ")
            user_name = input("enter user name for places names information: ")
            print(PostalCode.postal_code_places(postal_code, country, user_name))
        else:
            lat = input("enter lat for time zone information: ")
            lng = input("enter lng for time zone information: ")
            user_name = input("enter user name for time zone information: ")
            print(PostalCode.time_zone(lat, lng, user_name))

#http://api.geonames.org/timezoneJSON?lat=47.01&lng=10.2&username=demo
#print(PostalCode.postal_code_places(123, 'AT', 'shirel_biton'))
#print(PostalCode.postal_code_places('8775', 'CH', 'geosetter'))
#print(PostalCode.time_zone('47.01', '10.2', 'demo'))
