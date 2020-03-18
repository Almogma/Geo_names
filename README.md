# CICD_Geo_names

This project is designed for developers who want to use the services of Geo names API. 
The data is performed by URL queries, and mainly using REST webservices. 

### Prerequisites

Required installations:
* Python interpreter (version 3.7)
* requests
* pylint

```
* In order to install requests you should enter this line in the project terminal  - pipenv install requests.
* In order to install pylint you should enter this line in the project terminal - 
pip install pylint.
```

### How to install the project - 
1. Clone this repository to your computer by using the command "git clone": https://github.com/Almogma/CICD_Geo.git" 
2. Open the project in your preferred workspace
3. Run Main

There is a option to choose the wanted feature of the avaliable options:

### Feature 1 - place name lokup with postal code
This feature introduces the places which are connected to the given postal code.
The searhing is performed by the URL: api.geonames.org/postalCodeLookupJSON? with the parameters: postal code, country, user name. 

```
Example - 
HTTP get request:
http://api.geonames.org/postalCodeLookupJSON?postalcode=6600&country=AT&username=shirel_biton

response:
Reutte","lng":10.70065200805664,"countryCode":"AT","postalcode":"6600","adminName1":"Tirol","placeName":"Unterpinswang","lat":47.500470170782684}]}
```

### Feature 2 - time zone -  
This feature introduces sunrise and sunset time in a specific lat and lng.
The searhing is performed by the URL: api.geonames.org/timezone? with the parameters: lat, lng and user name. 

```
Example - 
HTTP GET requests - http://api.geonames.org/timezoneJSON?lat=47.01&lng=10.2&username=shirel_biton

{"sunrise":"2020-03-18 06:25","lng":10.2,"countryCode":"AT","gmtOffset":1,"rawOffset":1,"sunset":"2020-03-18 18:29","timezoneId":"Europe/Vienna","dstOffset":2,"countryName":"Austria","time":"2020-03-18 12:56","lat":47.01}
```

## information source

http://www.geonames.org/export/web-services.html


## Authors

**[Shirel Biton](https://github.com/shirelBiton)** 

**[Shani Waizman](https://github.com/shaniwaizman)**

**[Kobaivanov Yakir](https://github.com/yakirk1)** 
