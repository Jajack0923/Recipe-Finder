stopper = False #conditional variable for the while loop
fridge = [] #this is for the user to fill in
user_input_ingredients = fridge.append(str(input("Please enter one ingredient you currently have\n"))) #temporary ingredient that resets in while loop
temp_meas = str(input("Please enter it's measurement\n")) #temporary measurement that resets in while loop
stop_condition =str(input("Do you wish to add more ingredients?\nPlease enter YES or NO\n")).lower() #checks if while loop continues or not          

def Stopper():
	global stopper
	while stopper != True:
		user_input_ingredients
		temp_meas
		stop_condition 
		if stop_condition == 'no':
			stopper = True
		else:
			stopper = False

Stopper()