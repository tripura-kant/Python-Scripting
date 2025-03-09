import sys

try:
    import requests
except ModuleNotFoundError:
    print(f'Install request module and try again')
    sys.exit(1)

APIURL = 'https://jsonplaceholder.typicode.com/posts/'

response = requests.get(url=APIURL, verify=True)
st_code = response.status_code
if st_code == 200:
    print(f"Successfully executed get method on api and status code is : {st_code}")
else:
    print(f'failed and status code is: {st_code}')
