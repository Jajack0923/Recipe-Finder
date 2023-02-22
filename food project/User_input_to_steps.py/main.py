import requests
import id_and_user_selections
import Input_from_user

def Recipe_to_id():
	global selected_id, selected_recipe
	for i in range(len(id_and_user_selections.food_list)): #loops through the length of the list 
		if int(id_and_user_selections.selection)-1 == i: #if loop to find the recipe that the user selected
			selected_id = Input_from_user.id_title[i]['id'] #takes the id of the recipe selected by the user
			selected_recipe = Input_from_user.id_title[i]['title']
Recipe_to_id()

def Api():
	global url, querystring, headers
	url = "https://api.spoonacular.com/recipes/{id}/ingredientWidget.json".format(id = selected_id) #.format() is used to change the id based on user input


	querystring = {"id":selected_id}

	headers = {
		"x-api-key": "e518ff541c914d118d2cb375c4d484d3",
		"X-RapidAPI-Host": url
		}
Api()

def Get_and_parse():
	global response
	response = requests.get(url, headers=headers, params=querystring)
	response = response.json() #read and parse text from the api
Get_and_parse()


length_of_results = len(response["ingredients"]) #length of the list of the values of ingridients

ingredients_with_measurement = []
ingredients_no_measurement = []

def Id_to_ingredients():
	global selected_recipe
	for i in range(length_of_results):
		ingredient_name = response["ingredients"][i]["name"] #gets the naem of the ingridient
		value = response["ingredients"][i]["amount"]["metric"]["value"] 
		unit = response["ingredients"][i]["amount"]["metric"]["unit"] #value and unit gets the amount needed for it
		ingredient = f"{ingredient_name} : {value} {unit}" #creates smtg like "a : 50 g"
		ingredients_no_measurement.append(ingredient_name)
		ingredients_with_measurement.append(ingredient) 

	print(f"\nHere are the Ingredients needed for {selected_recipe}:")
	print("\n".join(ingredients_with_measurement))

Id_to_ingredients()


#Gets the steps for the recipes selected

def Api_2():
	global url, querystring, headers
	url = "https://api.spoonacular.com/recipes/{id}/analyzedInstructions".format(id = selected_id) #.format() is used to change the id based on user input


	querystring = {"id":selected_id}

	headers = {
		"x-api-key": "e518ff541c914d118d2cb375c4d484d3",
		"X-RapidAPI-Host": url
		}
Api_2()

def Get_and_parse2():
    global response
    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
Get_and_parse2()

length_of_steps = len(response[0]['steps'])

def Print_steps():
    print(f"\nHere are the steps for {selected_recipe}:")
    for i in range(length_of_steps):
        print(f"Step {i+1}: ")
        print(f"{response[0]['steps'][i]['step']}\n")

Print_steps()
#next is to print the steps to cook the recipe
#create main so a store them in functions so that call them at appropriate times
#create text like "These are the ingredients needed"