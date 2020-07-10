import argparse
import requests

#Welcome Message                                                                                                                                                                                                 
welcome = "Simple Web Request to get weather by zip code in the US."

#CLI Parser                                                                                                                                                                                                      
parser = argparse.ArgumentParser(description=welcome)

parser.add_argument('--zip', '-z', required=True, help="Zip Code to Get Weather")

parser.parse_args()

args = parser.parse_args()

zip = args.zip

#Endpoint
url = "http://api.openweathermap.org/data/2.5/weather?"

#API Key (free)                                                                                                                                                                                                  
api_key = "aace2be7c2713d5e8a6d908d015a0f81"

#Args                                                                                                                                                                                                            
querystring = {'appid':api_key,
                'zip':zip}

#Send Request
response = requests.request("GET", url, params=querystring, timeout=1)
data = response.json()

#Weather objects
weather = data['weather']                                                                                                                                                                                        
weather_index = weather[0]
weather_desc = weather_index['description']    

#City Name
name = data['name']

#Temp objects
main = data['main']
temp_orig = float(main['temp'])
feels_like_orig = float(main['feels_like'])

#Kelvin to Fahrenheit
temp = ((temp_orig - 273.15)*(9.0/5.0)) + 32
feels_like = ((feels_like_orig - 273.15)*(9.0/5.0)) + 32

#Print Output
print("Weather for " + name + " " + zip + ", is: " + str(weather_desc) + " with a temperature of: " + str(round(temp, 2)) + " F, but it feels like: " + str(round(feels_like, 2)) + " F.")
