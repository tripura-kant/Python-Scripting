import urllib.request
import json

# Define the URL of the JSON file
url = 'https://pyjsonsample.s3.amazonaws.com/pop.json'

# Fetch the data from the URL
with urllib.request.urlopen(url) as response:
    data = json.load(response)

# Extract the population dictionary
population = data.get("population", {})


# Define a function to get the population value from a tuple
def get_population(item):
    return item[1]


# Convert dictionary to a list of tuples and sort by population value using the function
sorted_population = sorted(population.items(), key=get_population)

# Print the sorted list
for country, pop in sorted_population:
    print(f'{country}: {pop}')
