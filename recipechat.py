import openai
import textwrap
import sys

api_key ="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"
openai.api_key = api_key
# Get the ingredients from the user
ingredients = input("Please enter a list of ingredients separated by commas: ")

# Use the ingredients to generate a list of food items
ingredient_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Please give me a list of food items that can be made with {ingredients}",
    temperature=0.5,
    max_tokens = 2048
)

# Print the list of food items
options = ingredient_response["choices"][0]["text"].strip()
print(options)

# Get the user's selection
selected = input("Enter the number of the food item you would like a recipe for: ")
print("List: ", selected)
selected = int(selected)-1  # Convert to index of option
selected_food = options.split("\n")[selected][3:]
print(selected_food)
# Use the selected food item to generate a recipe
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Please give me a recipe with instructions for {selected_food}, using only {ingredients} and basic seasonings",
    temperature=0.3,
    max_tokens=2048
)
#print(response["choices"])
recipe = response["choices"][0]["text"].strip()

print(recipe)