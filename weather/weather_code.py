# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

# Enter your API key here 
api_key = "f28e654cf78a932a10e58b89e87bb4aa"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = "Bangalore"

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))
	f = open("/home/pi/Desktop/final_year_project/weather/weather_text.txt","w")
	f.write("Today's temperature : "+str(current_temperature))    
	f.write("\nHumidity : "+str(current_humidiy))    
	f.write("\nDescription : "+str(weather_description))
	f.write("\nProgram complete ,done")    
	f.close()    
    

else: 
	print(" City Not Found ") 

