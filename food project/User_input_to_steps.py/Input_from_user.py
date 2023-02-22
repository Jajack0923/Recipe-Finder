import json
import requests

#spoonacular.com API <-- Antoine

user_input = input('Hi, what would you like to eat today?\n') #user input for recipes

def Api():
	global url, querystring, headers
	url = "https://api.spoonacular.com/recipes/complexSearch"
	querystring = {"query":user_input} #parameters
	headers = { #contains api-key and host to acccess the API
		"x-api-key": "Your API key from Spoonacular",
		"X-RapidAPI-Host": "https://api.spoonacular.com/recipes/complexSearch"
		} 
Api()


def Read_and_Parse():
	global response
	response = requests.get(url, headers=headers, params=querystring) #get response from the API
	print(response.text)
	response = response.json() #read and parse text from the API 
Read_and_Parse()


length_of_results = len(response['results']) #Number of recipes in results
id_title = [] #Empty list of list to store the dict of id and title

def api_to_id():
	for i in range(length_of_results): #loop through the length of the list of results
		id = response['results'][i]['id'] #shows the id of the food
		title = response['results'][i]['title'] #shows the name of the food
		id_title_dict = {'id' : id , 'title' : title} #create a dict for id and the name
		id_title.append(id_title_dict) #adding the dict into a list
	
	return id_title

api_to_id()


#Remarks:
#line 17: .json() is to read and parse the stuff coming from the API
