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
    print(f"And here are the steps for {selected_recipe}:")
    for i in range(length_of_steps):
        print(f"Step {i+1}: ")
        print(f"{response[0]['steps'][i]['step']}\n")

Print_steps()