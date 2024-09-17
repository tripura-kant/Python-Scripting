import requests

# Define the URL of the JSON file
url = 'https://pyjsonsample.s3.amazonaws.com/pop.json'

# Fetch the data from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data directly using requests' built-in method
    data = response.json()

    # Extract the population dictionary
    population = data.get("population", {})


    # print(population)

    # Define a function to return the population value
    def get_population_value(item):
        return item[1]


    # Sort countries by population in ascending order using the defined function
    sorted_population = sorted(population.items(), key=get_population_value)

    # Print the sorted list
    for country, pop in sorted_population:
        print(f'{country}: {pop}')
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
