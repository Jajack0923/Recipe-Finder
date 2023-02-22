import requests
import Input_from_user

fridge = ['salt', 'garlic', 'parsley', 'rosemary', 'tomatoes', 'dried white beans', 'sugar']

def Choices(): # Allows user to select which recipe they want to cook
	global food_list #food_list is the list of foods generated from the user input
	print('Here are the choices:\n')
	food_list = []
	two_dp_list = []
	all_id = []
	for i in range(len(Input_from_user.id_title)):
		id = Input_from_user.id_title[i]['id']
		all_id.append(id)

	for n in range(len(all_id)):	
		url = "https://api.spoonacular.com/recipes/{id}/ingredientWidget.json".format(id = all_id[n]) #.format() is used to change the id based on user input


		querystring = {"id":all_id[n]}

		headers = {
			"x-api-key": "Your API KEy",
			"X-RapidAPI-Host": url
			}

		response = requests.get(url, headers=headers, params=querystring)
		response = response.json() #read and parse text from the api

		length_of_results = len(response["ingredients"]) #length of the list of the values of ingridients

		ingredients_no_measurement = []

		for i in range(length_of_results):
			ingredient_name = response["ingredients"][i]["name"] #gets the name of the ingridient
			ingredients_no_measurement.append(ingredient_name)

		#missing_ingredients = list(set(fridge).difference(ingredients_no_measurement)) #takes difference between two sets but only gets elements in set fridge
		matching_ingredients = []
		for i in range(len(ingredients_no_measurement)):
			for a in range(len(fridge)):
				if fridge[a] == ingredients_no_measurement[i]:
					matching_ingredients = ingredients_no_measurement.pop(ingredients_no_measurement[i])	


		if len(ingredients_no_measurement) == 0:#if loop bcs so that it doesn't print 1 when the list is empty
			length_of_ingredients = 0 #if loop bcs so that it doesn't print 1 when the list is empty
		else:
			length_of_ingredients = len(ingredients_no_measurement) + 1 #+1 bcs computer starts counting from 0


		if len(missing_ingredients) == 0: #if loop bcs so that it doesn't print 1 when the list is empty
			length_of_missing = 0
		else:
			length_of_missing = len(missing_ingredients) + 1 #+1 bcs computer starts counting from 0

		perecentage_matchingness = (1 - ((length_of_ingredients -length_of_missing)/(length_of_ingredients))) * 100 #just some simple math. 1- so no need to make list for intersection between fridge and ingredients.
		two_dp_percentage = round(perecentage_matchingness, 2) #round to 2dp
		two_dp_list.append(two_dp_percentage)
		

	for c in range(len(Input_from_user.id_title)):
		choices_of_food = f"{c+1} : {Input_from_user.id_title[c]['title']} {two_dp_list[c]}"  # creates smtg like "1 : food Percentage matchingness" but not a dict
		food_list.append(choices_of_food) #creating a list 
Choices()
print('\n'.join(food_list))



def Print_Ingridients():
	global food_list, selection
	if len(food_list) == 0: #if no results then print this statement
		print("No results found. Please try again.")
	else: # if there are results then print this statement
		selection = input("\nPlease press the number of the dish you would like to make:\n") #Allows user to select which recipe they would like to try
		for i in range(len(food_list)): #loops through the length of the food list
			n = i + 1 # to start counting from 1
			if selection == str(n): #if the integer matches  then it prints the food recipe
				print(f"\n{Input_from_user.id_title[i]['title']}") #NOTE : need to print recipe for the food
			else:
				continue


Print_Ingridients()




