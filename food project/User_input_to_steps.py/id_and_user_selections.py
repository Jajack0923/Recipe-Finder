import requests
import Input_from_user



def Choices(): # Allows user to select which recipe they want to cook
	global food_list #food_list is the list of foods generated from the user input
	print('Here are the choices:\n')
	food_list = []
	
	for c in range(len(Input_from_user.id_title)):
		choices_of_food = f"{c+1} : {Input_from_user.id_title[c]['title']}"  # creates smtg like "1 : food" but not a dict
		food_list.append(choices_of_food) #creating a list 
Choices()


print('\n'.join(food_list)) # Joins the list togther and seperate it line by line
							#NOTE: Print the percentage matchingness as well and sort it


def Print_Ingridients():
	global food_list, selection
	if len(food_list) == 0: #if no results then print this statement
		print("No results found. Please try again.")
	else: # if there are results then print this statement
		selection = input("\nPlease press the number of the dish you would like to make:\n") #Allows user to select which recipe they would like to try
		#for i in range(len(food_list)): #loops through the length of the food list
			#n = i + 1 # to start counting from 1
			#if selection == str(n): #if the integer matches  then it prints the food recipe
				#print(f"\n{Input_from_user.id_title[i]['title']}") #NOTE : need to print recipe for the food
			#else:
				#continue


Print_Ingridients()




