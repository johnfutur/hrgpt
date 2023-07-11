import requests
import json

# Define the new job details
new_applicant = {
        'id': 4,
        'name': 'John Futurs',
        'address': 'Denver, California',
        'phone': '629650450298',
        'prev_pos': 'Pyhthon Dev',
        'prev_salary': 2000
    }


# Convert the new job details to JSON format
new_applicant_json = json.dumps(new_applicant)

# Make a POST request to the endpoint
response = requests.post('https://jobslistapi.johnfuturs.repl.co/applicants', json=new_applicant_json)

# Check the response status code
if response.status_code == 201:
    print('New applicant successfully inserted.')
else:
    print('Failed to insert the new applicant.')
    

url = 'https://jobslistapi.johnfuturs.repl.co/applicants'
response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    print(products)
else:
    print('Error:', response.status_code)
