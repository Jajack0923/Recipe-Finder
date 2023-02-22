import id_to_ingridients

#Idea: Can do .pop() from fridge when user decides to cook it or smtg so they dont have to input everytime --Jack
#Some of the comments can be removed. The comments im putting is just for you to understand what the code does --Jack

stopper = False #conditional variable for the while loop
fridge = ['salt', 'garlic', 'parsley', 'rosemary', 'tomatoes', 'dried white beans', 'sugar'] #this is for the user to fill in

#while stopper != True:
  #fridge.append(str(input("Please enter one ingredient you currently have\n")))  #temporary ingredient that resets in while loop
  #temp_meas = str(input("Please enter it's measurement\n"))  #temporary measurement that resets in while loop
  #stop_condition = str(input("Do you wish to add more ingredients?\nPlease enter YES or NO\n")).lower()  #checks if while loop continues or not
  #if stop_condition == "no":
    #stopper = True
  #else:
    #stopper = False


missing_ingredients = list(set(fridge).difference(id_to_ingridients.ingredients_no_measurement)) #takes difference between two sets but only gets elements in set fridge



def Percentage_matchingness():
    if len(id_to_ingridients.ingredients_no_measurement) == 0:#if loop bcs so that it doesn't print 1 when the list is empty
        length_of_ingredients = 0 #if loop bcs so that it doesn't print 1 when the list is empty
    else:
        length_of_ingredients = len(id_to_ingridients.ingredients_no_measurement) + 1 #+1 bcs computer starts counting from 0


    if len(missing_ingredients) == 0: #if loop bcs so that it doesn't print 1 when the list is empty
        length_of_missing = 0
    else:
        length_of_missing = len(missing_ingredients) + 1 #+1 bcs computer starts counting from 0

    perecentage_matchingness = (1 - ((length_of_ingredients -length_of_missing)/(length_of_ingredients))) * 100 #just some simple math. 1- so no need to make list for intersection between fridge and ingredients.
    two_dp_percentage = round(perecentage_matchingness, 2) #round to 2dp

    print(two_dp_percentage)










